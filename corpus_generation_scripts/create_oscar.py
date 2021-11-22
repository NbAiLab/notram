#!/usr/bin/env python3

import sys
import glob
import os
import re
import argparse
import pandas as pd
import jsonlines
import ftfy


def main(args):
    all_articles = []
    lines = []
    valid_article_count = 0

    # Read the file
    print('Starting to read text/csv file...')
    with open(args.input_file) as f:
        i = 0
        p = 0
        myarticle = {}
        myarticle['doc_type'] = str(args.doc_type)
        myarticle['id'] = str(args.doc_type)+"_"+str(i)
        myarticle['language_reported'] = str(args.language_reported)
        myarticle['paragraphs'] = []
        
        for line in f:
            if line == "\n":
                i += 1
                all_articles.append(myarticle)
                myarticle = {}
                myarticle['doc_type'] = str(args.doc_type)
                myarticle['id'] = str(args.doc_type)+"_"+str(i)
                myarticle['language_reported'] = str(args.language_reported)
                myarticle['paragraphs'] = []
                p = 0
            else:
                par = {}
                par['paragraph_id'] = p
                par['text'] = str(ftfy.fix_text(line.rstrip("\n")))
                myarticle['paragraphs'].append(par)
                p += 1

        #Append the last line as well 
        all_articles.append(myarticle)

    with jsonlines.open(args.output_file, 'w') as writer:
        writer.write_all(all_articles)

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {len(all_articles)}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Process the OSCAR corpus. This corpus has one document per line. No paragraphs. Output is an UTF-8 JSON lines ")
    parser.add_argument('--language_reported', required=True,
                        type=str, help='Language reported')
    parser.add_argument('--doc_type', required=True, type=str, help='Doctype')
    parser.add_argument('--input_file', required=True,
                        type=str, help='Input file')
    parser.add_argument('--output_file', required=True,
                        type=str, help='Output file')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
