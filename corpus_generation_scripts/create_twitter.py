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
    filelist = glob.glob(args.input_folder+'/*', recursive=True)

    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        for f in tqdm(filelist):
            with jsonlines.open(f) as reader:
                for tweet in reader:
                    try:
                        written = 0
                        myarticle = {}
                        myarticle['doc_type'] = args.doc_type
                        myarticle['id'] = args.doc_type+"_" + str(tweet['id'])
                        myarticle['language_reported'] = args.language_reported
                        myarticle['paragraphs'] = []
                        myarticle['publish_date'] = datetime.strptime(
                            tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y').strftime('%Y%m%d')
                        myarticle['created_time'] = tweet['created_at']
                        myarticle['post_id'] = tweet['id']
                        myarticle['user_id'] = tweet['user_id']

                        message = tweet.get('text', ' ')
                        if message == None:
                            message = ' '

                        alltext = list(filter(bool, message.splitlines()))

                        pid = 0
                        for p in alltext:
                            paragraph = {}
                            # Do some cleaning...
                            text = " ".join(p.split())
                            text = ''.join(c for c in text if c.isprintable())

                            text = ftfy.fix_text(text)

                            paragraph['paragraph_id'] = pid
                            paragraph['text'] = text

                            myarticle['paragraphs'].append(paragraph)
                            pid += 1

                        writer.write(myarticle)
                        n += 1
                    except:
                        print(tweet)

    print(f'{n} posts from {len(filelist)} files are written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Process the twitter corpus in json format. Output is an UTF-8 JSON lines")
    parser.add_argument('--language_reported', required=False, default="N/A",
                        type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True,
                        type=str, help='For instance tweet')
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
