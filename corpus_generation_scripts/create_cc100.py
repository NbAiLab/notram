#!/usr/bin/env python3

import sys
import glob
import os
import re
import argparse
import pandas as pd
import jsonlines
import ftfy
from tqdm import tqdm


def main(args):
    print('Starting to read text/csv file...')
    artid = 0
    myarticle = {}
    myarticle['doc_type'] = str(args.doc_type)
    myarticle['id'] = artid
    myarticle['language_reported'] = args.language_reported
    myarticle['paragraphs'] = []

    with jsonlines.open(args.output_file, 'w') as writer:
        with open(args.input_file) as f:
            pid = 0
            for n, line in tqdm(enumerate(f)):
                if line != "\n":
                    p = {}
                    p['paragraph_id'] = pid
                    p['text'] = str(ftfy.fix_text(line.rstrip("\n")))
                    myarticle['paragraphs'].append(p)
                    pid += 1
                else:
                    writer.write(myarticle)
                    artid += 1
                    pid = 0
                    myarticle = {}
                    myarticle['doc_type'] = str(args.doc_type)
                    myarticle['id'] = str(artid)
                    myarticle['language_reported'] = str(
                        args.language_reported)
                    myarticle['paragraphs'] = []

            # Just writes the last article as well
            writer.write(myarticle)

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {n}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Process the CC100 corpus. Output is UTF-8 JSON lines ")
    parser.add_argument('--language_reported', required=True, type=str,
                        help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True,
                        type=str, help='For instance cc100_no')
    parser.add_argument('--input_file', required=True,
                        type=str, help='Input file')
    parser.add_argument('--output_file', required=True,
                        type=str, help='Output file')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
