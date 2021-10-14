####################################################################################
# Covert the transferred Lovdata corpus to jsonl.
# This corpus is formed as a document per line. All paragraphs are randomised with no meta information
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy

def main(args):
    all_articles = []
    lines = []
    valid_article_count = 0

    #Read the file
    print('Starting to read text/csv file...')
    with open(args.input_file) as f:
        i = 0
        for line in f: 
            myarticle = {}
            myarticle['doc_type'] = str(args.doc_type)
            myarticle['id'] = str(args.doc_type)+"_"+str(i)
            myarticle['language_reported'] = str(args.language_reported)
            myarticle['paragraphs'] = [] 
        
            p = {}
            p['paragraph_id'] = 0
            p['text'] = str(ftfy.fix_text(line.rstrip("\n")))
        
            myarticle['paragraphs'].append(p)            

            valid_article_count += 1
            all_articles.append(myarticle)
            i += 1

    with jsonlines.open(args.output_file, 'w') as writer:
        writer.write_all(all_articles)


    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {len(all_articles)}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--language_reported', required=False, default="N/A",type=str, help='Language reported')
    parser.add_argument('--doc_type', required=True, type=str, help='Doctype')
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

