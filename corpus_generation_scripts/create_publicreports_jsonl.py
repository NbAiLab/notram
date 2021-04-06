####################################################################################
# Create Public Report jsonl from downloaded text files
# This corpus is formed as a document per line. No paragraphs.
# Output is an UTF-8 file with one article per line
####################################################################################

import sys
import glob
import os
import re
import argparse
import pandas as pd
import os
import jsonlines
import ftfy
import glob


def main(args):
    all_articles = []
    lines = []
    valid_article_count = 0


    if os.path.isdir(args.input_file):
        filelist = glob.glob(args.input_file+"*.txt")
    else:
        filelist = [args.input_file]
    
    for fl in filelist:
        # Read the file
        print(f'Parsing {fl}')
        with open(fl) as f:
            myarticle = {}
            myarticle['doctype'] = str(args.doctype)
            head, tail = os.path.split(args.input_file)
            myarticle['id'] = str(tail)
            if args.language_reported:
                myarticle['language_reported'] = str(args.language_reported)
            myarticle['paragraphs'] = []

            i = 0
            for line in f:
                if line.strip() != "":
                    p = {}
                    p['paragraph_id'] = i
                    p['text'] = str(ftfy.fix_text(line.rstrip("\n")))
                    myarticle['paragraphs'].append(p)
                    i += 1

        all_articles.append(myarticle)

    with jsonlines.open(args.output_file, 'w') as writer:
        writer.write_all(all_articles)

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {len(all_articles)}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--language_reported', required=False,
                        default='', type=str, help='Language reported')
    parser.add_argument('--doctype', required=True, type=str, help='Doctype')
    parser.add_argument('--input_file', required=True,
                        type=str, help='Input file')
    parser.add_argument('--output_file', required=True,
                        type=str, help='Output file')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
