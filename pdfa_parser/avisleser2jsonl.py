#!/usr/bin/env python
import argparse
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

from tqdm import tqdm

LOGGER = None
NOW = datetime.now()


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


def main(args):
    logger = get_logger()
    logger.info(f"Started at {NOW.strftime('%Y-%m-%d %H:%M:%S')}")
    base = args.input_dir
    output = args.output_dir
    logger.info(f"Ensure ASCII is set to {args.ensure_ascii}")
    logger.info(f"Input dir is '{args.input_dir}/{args.input_dir_glob}'")
    logger.info(f"Output dir is '{args.output_dir}'")
    # date_page_re = re.compile(r"_(\d{8})_.*_(\d{3})_[\w.]", re.I)
    date_page_re = re.compile(r"_(\d{8})_.*_(\d{2,3})(?:_\w+|\.txt)", re.I)
    total = len(list(Path(base).glob(args.input_dir_glob)))
    progress = tqdm(Path(base).glob(args.input_dir_glob), total=total)
    for path in progress:
        parts = path.parts[1:-1]
        jsonl_name = f"{path.parts[-1]}.jsonl"
        jsonl_path = Path.joinpath(*map(Path, (output, ) + parts))
        jsonl_path.mkdir(parents=True, exist_ok=True)
        progress.set_description(f"{path.parts[-1]: <60}")
        with (jsonl_path / jsonl_name).open(mode="w") as jsonl:
            for text_file in tqdm(path.glob("*.txt")):
                file_id = text_file.stem
                date_page = date_page_re.search(text_file.name)
                if date_page:
                    date, page_num = date_page.groups()
                else:
                    date = page_num = ""
                    if args.report_parsing_error:
                        logger.error(
                            f"Failed extracting date and page number from "
                            f"{text_file.name}"
                        )
                with text_file.open() as file:
                    paragraphs = []
                    for paragraph in file.read().split("\n\n"):
                        paragraph = paragraph.strip()
                        if paragraph:
                            paragraphs.append({
                                'paragraph_id': len(paragraphs),
                                'page': page_num,
                                'text': paragraph
                            })
                json_line = {
                    'id': file_id,
                    'doc_type': args.doc_type,
                    'publish_date': date,
                    'pymupdf_version': args.pymupdf_version,
                    'title': '',
                    'paragraphs': paragraphs,
                }
                jsonl_contents = json.dumps(
                    json_line, ensure_ascii=args.ensure_ascii
                ) + "\n"
                match = None
                if args.output_filename_re:
                    filename_re = re.compile(rf"{args.output_filename_re}", re.IGNORECASE)
                    match = filename_re.match(text_file.name)
                    if match:
                        if args.output_dir_dates and date:
                            jsonl_path_out = jsonl_path / date[:4] / date[4:6] / date[6:]
                            jsonl_path_out.mkdir(parents=True, exist_ok=True)
                        else:
                            jsonl_path_out = jsonl_path
                        with (jsonl_path_out / f"{match.group()}.jsonl").open(mode="a") as jsonl_file:
                            jsonl_file.write(jsonl_contents)
                if args.output_filename_re is None or match is None:
                    jsonl.write(jsonl_contents)
    logger.info(f"Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f""
    f"Convert extracted plain text from avisleser (mupdf) to JSON lines"""
    f"", epilog=f"""Example usage:
    {__file__} --input_dir mupdf --output_dir jsonl
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--input_dir', default='./mupdf',
        metavar='input_dir', help='Input directory')
    parser.add_argument('--input_dir_glob', default='*/*/*/*/',
        metavar='input_dir_glob', help='Input directory glob')
    parser.add_argument('--output_dir', default='./jsonl',
        metavar='output_dir', help='Output directory')
    parser.add_argument('--output_dir_dates', default=False,
        metavar='output_dir_dates', help='If filename contains YYYYMMDD dates, use them to create subfolders')
    parser.add_argument('--output_filename_re',
        metavar='output_filename_re', help="""
        Output filename re to match when generating the filename. Useful to group by several pages of the same issueo of a newspaper
        For example, "[^_]+_[^_]+_[^_]+_[0-9]{8}_[0-9]+_[0-9]+_[0-9]+" will
        match names such as "aandalsnesavis_null_null_20210105_96_2_1", placing
        the corresponding JSON line entry in the file
        "aandalsnesavis_null_null_20210105_96_2_1.jsonl"
        """)
    parser.add_argument('--doc_type', default='newspaper_pdf',
        metavar='doc_type', help='Document type')
    parser.add_argument('--pymupdf_version', default='1.18.10',
        metavar='pymupdf_version', help='PyMuPDF version')
    parser.add_argument('--report_parsing_error', default=True, type=bool,
        metavar='report_parsing_error', help='Report filename parsing errors')
    parser.add_argument('--ensure_ascii', default=False, type=bool,
        metavar='ensure_ascii', help='Do not escape non-ASCII characters')
    args = parser.parse_args()
    main(args)
