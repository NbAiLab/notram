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
    # date_page_re = re.compile(r"_(\d{8})_.*_(\d{3})_[\w.]", re.I)
    date_page_re = re.compile(r"_(\d{8})_.*_(\d{2,3})(?:_\w+|\.txt)", re.I)
    total = len(list(Path(base).glob("*/*/*/*/")))
    progress = tqdm(Path(base).glob("*/*/*/*/"), total=total)
    for path in progress:
        parts = path.parts[1:-1]
        jsonl_name = f"{path.parts[-1]}.jsonl"
        jsonl_path = Path.joinpath(*map(Path, (output, ) + parts))
        jsonl_path.mkdir(parents=True, exist_ok=True)
        progress.set_description(f"{path.parts[-1]: <60}")
        with (jsonl_path / jsonl_name).open(mode="w") as jsonl:
            for text_file in path.glob("*.txt"):
                file_id = text_file.stem
                date_page = date_page_re.search(text_file.name)
                if date_page:
                    date, page_num = date_page.groups()
                else:
                    date = page_num = ""
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
                    'doc_type': 'newspaper_pdf',
                    'publish_date': date,
                    'pymupdf_version': '1.18.10',
                    'title': '',
                    'paragraphs': paragraphs,
                }
                jsonl.write(json.dumps(json_line) + "\n")
    logger.info(f"Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f""
    f"Converting extracted text from avisleser (mupdf) to JSON lines"""
    f"", epilog=f"""Example usage:
    {__file__} --input_dir mupdf --output_dir jsonl
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--input_dir', default='./mupdf',
        metavar='input_dir', help='Input directory')
    parser.add_argument('--output_dir', default='./jsonl',
        metavar='output_dir', help='Output directory')

    args = parser.parse_args()
    main(args)
