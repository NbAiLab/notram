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

    # Get a list of documents in the folder
    if args.year != "":
        filelist = glob.glob(args.input_folder+'/*' +
                             args.year+"*", recursive=True)
    else:
        filelist = glob.glob(args.input_folder+'/*', recursive=True)

    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        for f in tqdm(filelist):
            with jsonlines.open(f) as reader:
                for redditpost in reader:
                    written = 0
                    myarticle = {}
                    myarticle['doc_type'] = args.doc_type
                    myarticle['id'] = args.doc_type+"_" + redditpost['id']
                    myarticle['language_reported'] = args.language_reported
                    myarticle['paragraphs'] = []
                    myarticle['publish_date'] = datetime.utcfromtimestamp(
                        int(redditpost['created_utc'])).strftime('%Y%m%d')
                    myarticle['created_utc'] = redditpost['created_utc']
                    myarticle['subreddit_id'] = redditpost['subreddit_id']
                    myarticle['author'] = redditpost['author']
                    myarticle['parent_id'] = redditpost['parent_id']

                    alltext = list(
                        filter(bool, redditpost['body'].splitlines()))

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

    print(f'{n} posts from {len(filelist)} files are written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Create the Reddit corpus from the downloaded archive. Output is an UTF-8 JSON lines")
    parser.add_argument('--language_reported', required=False, default="N/A",
                        type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True,
                        type=str, help='For instance government')
    parser.add_argument('--year', default="", type=str,
                        help='Selects only one year')
    parser.add_argument('-o', '--output_file', required=True,
                        help='Output file name. Will overwrite it exists')
    parser.add_argument('-i', '--input_folder', required=True,
                        help='Input folder. Will read all files in folder')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
# print(soup.prettify()) # print the parsed data of html
