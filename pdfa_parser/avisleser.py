#!/usr/bin/env python
import argparse
import faulthandler
import io
import logging
import os
import re
import signal
import statistics
import string
import sys
import traceback
from collections import Counter
from collections.abc import Iterable
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Iterator, List, NoReturn, Optional, Tuple, Any, Union
# import warnings; warnings.filterwarnings("ignore")

from joblib import Parallel, delayed
from joblib import Memory

import fitz
from pdfminer.high_level import extract_pages, extract_text_to_fp
from pdfminer.layout import LTTextContainer, LTAnno, LTChar, LAParams, LTPage
from sentence_splitter import SentenceSplitter, split_text_into_sentences
from tqdm import tqdm

SPACES_RE = re.compile(r"[ ][ ]+")
STARTEND_RE = re.compile(r"(\n\s+)")
HYPHENS_RE = re.compile(r"([a-zæåø])-\s+([a-zæåø])")
HYPHENSHASH_RE = re.compile(r"([a-zæåø])-#\s+([a-zæåø])")
LINEBREAK_RE = re.compile(r"[\n]")
LINEBREAKS_RE = re.compile(r"[\n]{2,}")
SPLITTER = SentenceSplitter(language='no')
LOGGER = None
NOW = datetime.now()


class TimeoutException(Exception): pass


@contextmanager
def time_limit(seconds, description=None):
    def signal_handler(signum, frame):
        raise TimeoutException(description or "Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def get_logger() -> logging.Logger:
    """
    Get a logger
    """
    global LOGGER
    if LOGGER is None:
        LOGGER = logging.getLogger(__name__)
        LOGGER.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d - %H:%M:%S"
        )
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        LOGGER.addHandler(console)
    return LOGGER


def process_text_container(element: LTTextContainer) -> Tuple[List[str], float]:
    fontnames = []
    fontsize = 0
    if isinstance(element, Iterable):
        for text_line in element:
            if isinstance(text_line, Iterable):
                for character in text_line:
                    if isinstance(character, LTChar):
                        fontnames.append((character.fontname, character.size))
                        if fontsize < character.size:
                            fontsize = character.size
            elif isinstance(text_line, LTChar):
                fontnames.append((text_line.fontname, text_line.size))
                if fontsize < text_line.size:
                    fontsize = text_line.size
    elif isinstance(element, LTChar):
        fontnames.append((element.fontname, element.size))
        if fontsize < element.size:
            fontsize = element.size
    return fontnames, fontsize


def traverse(element: Union[Iterable, LTTextContainer]) -> Tuple[List[str], float]:
    fontnames = []
    fontsize = 0
    if isinstance(element, LTTextContainer):
        return process_text_container(element)
    elif isinstance(element, Iterable):
        for item in element:
            element_output = traverse(item)
            if element_output:
                element_fontnames, element_fontsize = element_output
                fontnames += element_fontnames
                if fontsize < element_fontsize:
                    fontsize = element_fontsize
    return fontnames, fontsize


def get_most_frequent_and_largest_fonts(
    pages: List[LTPage]
) -> Tuple[str, float]:
    all_fonts, fontsize = traverse(pages)
    fontnames = Counter(all_fonts)
    return (
        fontnames.most_common(1)[0][0][0] if fontnames else None,
        fontnames.most_common(1)[0][0][1] if fontnames else None,
        fontsize if fontsize > 0 else None
    )


def get_text_containers(element: Any) -> List[LTTextContainer]:
    containers = []
    if isinstance(element, LTTextContainer):
        return [element]
    elif isinstance(element, Iterable):
        for item in element:
            element_output = get_text_containers(item)
            if element_output:
                containers += element_output
    return containers


def get_text_line(
    text_line: List,
    line_number: int,
    font: str,
    size: float,
    previous_line_font: str,
) -> str:
    chars = ""
    line_font = ""
    if isinstance(text_line, Iterable):
        for character_number, character in enumerate(text_line):
            char = " "
            if isinstance(character, LTChar):
                char_font = getattr(character, "fontname")
                char_size = getattr(character, "size")
                if char_font == font or char_size == size:
                    char = character.get_text()
                # TODO: Identify subheadings
                # if (getattr(character, "fontname") != font
                #     and getattr(character, "fontname") != previous_line_font
                #     and getattr(character, "size") == size
                #     and line_number == 0
                #     and character_number == 0):
                #     char = f"\n→ {char}"
                # char += character.get_text()
                if char.strip():
                    line_font = getattr(character, "fontname", "")
            chars = f"{chars}{char}"
    else:
        try:
            chars = text_line.get_text()
        except:
            pass
    return chars, line_font


def get_text(pages: List[LTPage], font: str, size: float) -> str:
    text = ""
    for page_layout in pages:
        for box_id, element in enumerate(page_layout):
            if isinstance(element, LTTextContainer):
                last_font = ""
                for line_number, text_line in enumerate(element):
                    chars, last_font = get_text_line(text_line, line_number, font, size, last_font)
                    text = f"{text} {chars} "
                text = f"{text}\n"
    return text


def get_unstructured_text(pages: List[LTPage], font: str, size: float) -> str:
    text = ""
    for element in get_text_containers(pages):
        last_font = ""
        for line_number, text_line in enumerate(element):
            chars, last_font = get_text_line(text_line, line_number, font, size, last_font)
            text = f"{text} {chars} "
        text = f"{text}\n"
    return text


def get_all_texts(
    filename: Union[str, Path],
    line_margin: float=0.15,
    detect_vertical: bool=-0.8,
    boxes_flow: Optional[float]=None,
) -> str:
    laparams = LAParams(
        line_margin=line_margin,
        boxes_flow=boxes_flow,
        detect_vertical=detect_vertical,
        all_texts=True,
    )
    pages = list(extract_pages(filename, laparams=laparams))
    font, size, _ = get_most_frequent_and_largest_fonts(pages)
    text = get_unstructured_text(pages, font, size)
    if text.strip():
        return text, None
    with open(filename, 'rb') as file, io.StringIO() as buffer:
        extract_text_to_fp(file, buffer, laparams=laparams)
        text = buffer.getvalue().strip()
    html = None  # disabling HTML for now
    # with open(filename, 'rb') as file, io.StringIO() as buffer:
    #     extract_text_to_fp(
    #         file, buffer, laparams=laparams, output_type='html', codec=None
    #     )
    #     html = buffer.getvalue().strip()
    # return LINEBREAK_RE.sub(r" ", text), html
    return text, html


def reformat(text: str, single_hyphens: bool=True) -> str:
    text = SPACES_RE.sub(r" ", text)
    if single_hyphens:
        text = HYPHENS_RE.sub(r"\1\2", text)
    else:
        pass
        text = HYPHENSHASH_RE.sub(r"\1\2", text)
    text = "\n".join(line.strip() for line in text.split("\n"))
    text = LINEBREAKS_RE.sub("\n\n", text)
    blocks = []
    for block in text.split("\n\n"):
        lines = []
        for line in block.split("\n"):
            if all(char in string.digits for char in line if char != ""):
                lines.append("\n" + line.strip() + "\n")
            else:
                lines.append(line.strip())
        blocks.append(" ".join(lines).strip())
    text = "\n\n".join(blocks)
    text = "\n".join(line.strip() for line in text.split("\n"))
    return text


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def get_text_pdfminer(
    filename: str,
    line_margin: float=0.15,
    detect_vertical: bool=-0.8,
    all_texts: bool=False,
    boxes_flow: Optional[float]=None,
    same_sizes: Optional[bool]=False,
    occurrence_rate: Optional[bool]=None,
) -> str:
    text = ""
    html = None
    laparams = LAParams(
        line_margin=line_margin,
        boxes_flow=boxes_flow,
        detect_vertical=detect_vertical,
        all_texts=False
    )
    pages = list(extract_pages(filename, laparams=laparams))
    font, size, _ = get_most_frequent_and_largest_fonts(pages)
    text = get_text(pages, font, size)
    if len(text.strip()) == 0 and all_texts:
        text, html = get_all_texts(
            filename,
            line_margin=line_margin,
            boxes_flow=boxes_flow,
            detect_vertical=detect_vertical,
        )
    return reformat(text).strip(), html


def get_text_fitz(
    filename: str,
    line_margin: float=0.15,
    detect_vertical: bool=-0.8,
    all_texts: bool=False,
    boxes_flow: Optional[float]=None,
    same_sizes: Optional[bool]=False,
    occurrence_rate: Optional[bool]=None,
) -> str:
    faulthandler.enable()
    pdf = fitz.open(filename)
    text = []
    for page in pdf:
        fonts = []
        lengths = []
        page_dict = page.get_text("dict")
        for block in page_dict.get("blocks", []):
            for line in block.get("lines", []):
                line_text = ""
                chars = ""
                for span in line.get("spans", []):
                    span_font = span.get("font", "").split(",")[0].split("-")[0]
                    span_text = span.get("text", "")
                    chars = ""
                    for char in span_text:
                        if char.strip() != "":
                            fonts.append((span_font, span["size"], span["color"]))
                            chars += char
                    line_text += span_text.strip()
                if chars:
                    lengths.append(len(chars))
        if not fonts or not lengths:
            continue
        if occurrence_rate is not None:
            counts = Counter(fonts)
            freqs = [(i, counts[i] / len(fonts))
                     for i, count in counts.most_common()]
            font_tuples = set(
                font_tuple for font_tuple, freq in freqs
                if freq >= occurrence_rate
            )
            font, size, color = list(zip(*font_tuples))
        else:
            font, size, color = Counter(fonts).most_common(1)[0][0]
            font, size, color = [font], [size], [color]
        font, size, color = set(font), set(size), set(color)
        # if len(lengths) > 1:
        #     lengths_std = statistics.stdev(lengths)
        #     lengths_mean = statistics.mean(lengths)
        # else:
        #     lengths_std = 0  # Not sure about this
        #     lengths_mean = len(lengths)
        for block in page_dict.get("blocks", []):
            for line in block.get("lines", []):
                line_text = ""
                for span_index, span in enumerate(line.get("spans", [])):
                    span_text = span["text"].strip()
                    if (span_text
                        and any(span["font"].startswith(f) for f in font)
                        and any(span["color"] == c for c in color)
                        and (any(span["size"] == s for s in size)
                             or not same_sizes)
                        and span["flags"] in (0, 4, 6)
                        and line["wmode"] == 0
                        ):
                        line_text += span["text"]
                    if len(line_text) > 2 and line_text.rstrip()[-1] == "-":
                        line_text += "#"
                text.append(line_text)
                text.append(" ")
            text.append("\n")
        text.append("\n")
    text = reformat("".join(text), single_hyphens=False)
    if "-#" in text:
        text = text.replace("-#", "-")
    return text, None


def get_text_from_pdf(
    filename: str,
    pdfs_dir: Union[Path, str],
    output: Union[Path, str],
    overwrite: bool=False,
    bar: Optional[tqdm]=None,
    line_margin: float=0.15,
    detect_vertical: bool=-0.8,
    all_texts: bool=False,
    boxes_flow: Optional[float]=None,
    skip_empty: Optional[bool]=True,
    same_sizes: Optional[bool]=False,
    occurrence_rate: Optional[bool]=None,
) -> NoReturn:
    """Writes PDFs to text files"""
    logger = get_logger()
    if bar:
        bar.set_description(filename.name)
    if not pdfs_dir.endswith("/"):
        pdfs_dir = f"{pdfs_dir}/"
    dest = Path(output)
    dest_stem = str(filename).replace(str(pdfs_dir), "").rsplit(".pdf", 1)[0]
    text_dest = dest / f"{dest_stem}.txt"
    if not overwrite and text_dest.exists():
        return
    # Create the empty file if it doesn't exist
    text_dest.parent.mkdir(parents=True, exist_ok=True)
    with text_dest.open(mode="a") as _: pass
    description = f"{filename} ({sizeof_fmt(filename.stat().st_size)})"
    get_text = get_text_pdfminer if args.engine == "pdf2txt" else get_text_fitz
    text = ""
    html = None
    try:
        with time_limit(args.timeout, description=description):
            text, html = get_text(
                filename, line_margin, detect_vertical, all_texts, boxes_flow,
                same_sizes, occurrence_rate
            )
        if not text and skip_empty:
            dest = dest / "empty"
    except TimeoutException as exception:
        dest = dest / "timeout"
        text = traceback.format_exc()
        logger.error(description)
        logger.error(str(text))
    except Exception as exception:
        dest = dest / str(exception.__class__.__name__).lower()
        text = traceback.format_exc()
        logger.error(description)
        logger.error(str(text))
    # heading = get_text(pages, "size", size).strip()
    # heading = reformat(heading)
    # dest.mkdir(parents=True, exist_ok=True)
    text_dest.unlink(missing_ok=True)  # remove temporary file
    text_dest = dest / Path(f"{dest_stem}.txt")
    text_dest.parent.mkdir(parents=True, exist_ok=True)
    with text_dest.open(mode="w") as text_file:
        if args.split_sentences:
            for sentence in SPLITTER.split(text=text):
                text_file.write(
                    f"{sentence}\n".encode('utf-8', 'replace').decode()
                )
        else:
            text_file.write(text.encode('utf-8', 'replace').decode())
    # if html is not None:
    #     html_dest = dest / f"{dest_stem}.html"
    #     html_dest.parent.mkdir(parents=True, exist_ok=True)
    #     if not overwrite and html_dest.exists():
    #         return
    #     with html_dest.open(mode="w") as html_file:
    #         html_file.write(html.encode('utf-8', 'replace').decode())


def generate_paths(paths: List, progress_file: str) -> Path:
    with Path(progress_file).open(mode="w") as file:
        for path in paths:
            file.write(str(path) + "\n")
            yield path
    # for path in paths:
    #     if not str(path) in IGNORES:
    #         IGNORES.add(str(path))
    #         with RESUME_FILE.open(mode="a") as resume_file:
    #             resume_file.write(str(path) + "\n")
    #         if resume:
    #             yield path
    #     if not resume:
    #         yield path


def main(args: argparse.ArgumentParser) -> NoReturn:
    """Main function"""
    logger = get_logger()
    logger.info("Starting...")
    logger.info(f"Started at {NOW.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Reading pdfs: {args.pdfs_dir}/{args.pdfs_glob}")
    logger.info(f"Writing texts: {args.output_dir}")
    logger.info(f"Texts will{' NOT' if args.no_overwrite else ''} be overwritten")
    logger.info(f"All texts will{' NOT' if args.no_all_texts else ''} be extracted")
    logger.info(f"Progress file: {args.progress_file}")
    logger.info(f"Processing time out of {args.timeout} seconds")
    logger.info(
        f"Running using {'all' if args.n_jobs < 0 else args.n_jobs} processes"
    )
    if not args.total:
        logger.info("Calculating number of pdfs...")
        path = Path(args.pdfs_dir).rglob(args.pdfs_glob)
        total = len(list(None for p in path if p.is_file()))
        logger.info(f"Found {total} pdf files")
    else:
        total = args.total
        logger.info(f"Trusting there are {total} pdf files")
    path = Path(args.pdfs_dir).rglob(args.pdfs_glob)
    bar = tqdm(generate_paths(path, args.progress_file), total=total)
    Parallel(n_jobs=args.n_jobs)(
        delayed(get_text_from_pdf)(
            pdf,
            pdfs_dir=args.pdfs_dir,
            output=args.output_dir,
            overwrite=not args.no_overwrite,
            bar=bar if args.n_jobs == 1 else None,
            line_margin=args.line_margin,
            boxes_flow=args.boxes_flow,
            detect_vertical=False,
            all_texts=not args.no_all_texts,
            skip_empty=args.skip_empty,
            same_sizes=args.same_sizes,
            occurrence_rate=args.occurrence_rate or None,
        )
        for step, pdf in enumerate(bar))
    # bar.set_description("Done")
    logger.info("Done!")


if __name__ == '__main__':
    yesno = lambda x: str(x).lower() in {'true', 't', '1', 'yes', 'y'}
    parser = argparse.ArgumentParser(description=f""
    f"Extracts the text of the body of PDF's with column layout with "
    f"extractable text objects"
    f"", epilog=f"""Example usage:
    {__file__} ./pdfs "*.pdf" ./outputs --timeout 60 --n_jobs 8
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('pdfs_dir',
        help='Directory with the pdfs files'
    )
    parser.add_argument('pdfs_glob', default="*.pdf",
        help='Glob for the directory with the pdfs files'
    )
    parser.add_argument('output_dir',
        help='Directory to store output files'
    )
    parser.add_argument('--no_overwrite',
        action="store_true",
        help='Do not overwrite outputs'
    )
    parser.add_argument('--split_sentences',
        action="store_true",
        help='Split sentences'
    )
    parser.add_argument('--n_jobs',
        default=1, type=int,
        help='Number of multiprocessing jobs. Defaults to 1 (-1 for max)',
    )
    parser.add_argument('--timeout',
        default=30, type=int,
        help='Parsing timeout in seconds. Defaults to 30',
    )
    parser.add_argument('--line_margin',
        default=0.25, type=float,
        help='Line margin for PDFMiner.six LTParams. Defaults to 0.25',
    )
    parser.add_argument('--boxes_flow',
        default=-0.8, type=float,
        help='Boxes flow for PDFMiner.six LTParams. Defaults to -0.8',
    )
    parser.add_argument('--same_sizes',
        action="store_true",
        help='Filter out text when its size is not the same size as that of '
             'the most frequent font'
    )
    parser.add_argument('--occurrence_rate',
        default=0.0, type=float,
        help='Filter out text when the frequency of its font family and size '
             'pair is not at least OCCURRENCE_RATE percent [0.0 - 1.0] of the '
             'characters in a page. If not passed, only the most frequent pair '
             'of font family and size will be used'
    )
    parser.add_argument('--skip_empty',
        action="store_true",
        help='Ignore files if the extraction produced an empty text'
    )
    parser.add_argument('--no_all_texts',
        action="store_true",
        help='Do not extract from texts in or captioning images'
    )
    parser.add_argument('--engine',
        default="mupdf",
        help='Options are "pdf2txt" for PDFMiner or "mupdf" for MuPDF'
    )
    parser.add_argument('--progress_file',
        default=f'avisleser.{NOW.strftime("%Y%m%dT%H%M%S")}.log',
        help='Save the progress to a local file'
    )
    parser.add_argument('--total',
        default=0, type=int,
        help='Total number of files to process. Calculated if not passed',
    )
    args = parser.parse_args()
    main(args)
