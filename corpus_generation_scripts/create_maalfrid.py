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
import csv
from urllib.parse import urlparse


def main(args):
    # Set in parameters later
    files = glob.glob(args.input_folder+"*.txt")
    meta_file = args.meta_file

    print("Starting to load csv meta-file")
    df = pd.read_csv(meta_file, encoding='utf-8', dtype='string')
    print("Finished loading csv meta-file")

    artid = 0
    emptyid = 0

    with jsonlines.open(args.output_file, 'w') as writer:

        for input_file in tqdm(files):
            with open(input_file) as f:
                content_hash = os.path.basename(input_file).replace(".txt", "")
                try:
                    item = df[df.content_hash == content_hash].iloc[0]
                    domain = urlparse(item['target_uri']).netloc
                    name, ext = domain.split('.')[-2:]
                except:
                    print("was not found setting empty id "+str(emptyid))
                    item = {}
                    item['target_uri'] = "Not set"
                    item['content_hash'] = "notgiven_"+str(emptyid)
                    name = "unknown"
                    emptyid += 1

                current_page = 0
                myarticle = {}
                myarticle['doc_type'] = args.doc_type+"_"+name
                myarticle['id'] = "maalfrid_" + \
                    content_hash+"_"+str(current_page)
                myarticle['target_url'] = item['target_uri']
                myarticle['language_reported'] = args.language_reported
                myarticle['page'] = current_page
                myarticle['paragraphs'] = []

                pid = 0

                for n, line in enumerate(f):

                    if "^L" not in line:
                        if line != "\n":
                            p = {}
                            p['paragraph_id'] = pid

                            p['text'] = str(ftfy.fix_text(line.rstrip("\n")))
                            myarticle['paragraphs'].append(p)
                            pid += 1
                    else:
                        # Make sure to write the page before starting a new
                        writer.write(myarticle)
                        artid += 1
                        pid = 0
                        current_page += 1
                        myarticle = {}
                        myarticle['doc_type'] = args.doc_type+"_"+name
                        myarticle['id'] = "maalfrid_" + \
                            content_hash+"_"+str(current_page)
                        myarticle['target_url'] = item['target_uri']
                        myarticle['language_reported'] = args.language_reported
                        myarticle['page'] = current_page
                        myarticle['paragraphs'] = []

                # Write the article if the page is not empty
                if myarticle['paragraphs']:
                    writer.write(myarticle)

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {n}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Create jsonl from mupdf-created Maalfrid documents. Output is an UTF-8 JSON lines")
    parser.add_argument('--language_reported', required=False, default="N/A",
                        type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True,
                        type=str, help='For instance maalfrid')
    parser.add_argument('--input_folder', required=True,
                        type=str, help='Input folder')
    parser.add_argument('--meta_file', required=True, type=str,
                        help='Meta file from Språkbanken in csv format')
    parser.add_argument('--output_file', required=True,
                        type=str, help='Output file')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
