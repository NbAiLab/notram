#!/opt/anaconda3/bin/python

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
    filelist = glob.glob(args.input_folder+'/*', recursive=True)

    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        for f in tqdm(filelist):
            with jsonlines.open(f) as reader:
                for facebookpost in reader:
                    written = 0
                    myarticle = {}
                    myarticle['doc_type'] = args.doc_type
                    myarticle['id'] = args.doc_type+"_" + \
                        str(facebookpost['post_id'])+"_" + \
                        str(facebookpost['page_id'])
                    myarticle['language_reported'] = args.language_reported
                    myarticle['paragraphs'] = []
                    myarticle['publish_date'] = datetime.strptime(
                        facebookpost['created_time'], '%Y-%m-%dT%H:%M:%S+00:00').strftime('%Y%m%d')
                    myarticle['created_time'] = facebookpost['created_time']
                    myarticle['post_id'] = facebookpost['post_id']
                    myarticle['page_id'] = facebookpost['page_id']
                    myarticle['url'] = facebookpost['link']
                    myarticle['title'] = facebookpost['name']
                    myarticle['content_type'] = facebookpost['type']

                    message = facebookpost.get('message', ' ')
                    if message == None:
                        message = ' '

                    alltext = list(filter(bool, message.splitlines()))

                    pid = 0
                    for p in alltext:
                        paragraph = {}
                        text = " ".join(p.split())
                        text = ''.join(c for c in text if c.isprintable())
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
        description="Convert the WEB64 Facebook corpus to jsonl. This corpus is in json format. Output is a jsonl  UTF-8 file with one post per line")
    parser.add_argument('--language_reported', required=False, default="N/A",
                        type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True,
                        type=str, help='For instance government')
    parser.add_argument('--output_file', required=True,
                        help='Output file name. Will overwrite it exists')
    parser.add_argument('--input_folder', required=True,
                        help='Input folder. Will read all files in folder')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
