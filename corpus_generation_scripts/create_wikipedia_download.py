#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import ftfy
import glob
import argparse
import os
import jsonlines
from tqdm import tqdm
from datetime import datetime


def main(args):
    # Create the new file. Overwrite if it exits
    f = open(args.output_file, "w+")
    f.close()

    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        with jsonlines.open(args.input_file) as reader:
            for wikipost in tqdm(reader):
                written = 0
                myarticle = {}
                myarticle['doc_type'] = args.doc_type
                myarticle['id'] = args.doc_type + \
                    "_" + wikipost['title']+"_"+str(n)
                myarticle['language_reported'] = args.language_reported
                myarticle['paragraphs'] = []
                myarticle['title'] = wikipost['title']

                sectiontext = ' '.join(wikipost['section_texts'])
                alltext = list(filter(bool, sectiontext.splitlines()))

                pid = 0
                for p in alltext:
                    paragraph = {}
                    text = " ".join(p.split())
                    text = ftfy.fix_text(text)

                    paragraph['paragraph_id'] = pid
                    paragraph['text'] = text

                    myarticle['paragraphs'].append(paragraph)
                    pid += 1

                writer.write(myarticle)
                n += 1

    print(f'{n} posts are written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Process the downloaded Wikipedia files. Output is an UTF-8 JSON lines")
    parser.add_argument('--language_reported', required=False, default="N/A",
                        type=str, help='Language reported. Can be nob, nno, no, da, sv, is or N/A')
    parser.add_argument('--doc_type', required=True, type=str,
                        help='For instance wikipedia_download_no')
    parser.add_argument('--year', default="", type=str,
                        help='Selects only one year')
    parser.add_argument('-o', '--output_file', required=True,
                        help='Output file name. Will overwrite it exists')
    parser.add_argument('-i', '--input_file',
                        required=True, help='Input file.')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)

