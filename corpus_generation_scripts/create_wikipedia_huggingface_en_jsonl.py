####################################################################################
# Create Wikipedia jsonl from Hugging Face. Just wraps it in jsonl
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy
from datasets import list_datasets, load_dataset
import tqdm as tqdm

def main(args):
    wiki = load_dataset("wikipedia", "20200501.en", split='train')

    all_articles = []
    lines = []
    valid_article_count = 0

    with jsonlines.open(args.output_file, 'w') as writer:

        for n,article in enumerate(wiki): 
            current_page = 0
            myarticle = {}
            myarticle['doc_type'] = str(args.doc_type)
            myarticle['id'] = str(args.doc_type)+"_"+str(n)
            myarticle['language_reported'] = str(args.language_reported)
            myarticle['paragraphs'] = [] 
            
            parcoll = article['text'].split("\n")
            
            pid = 0
            for pline in parcoll: 
                text = str(ftfy.fix_text(pline).strip())
                
                if text != '' and text != '\n':
                    p = {}
                    p['paragraph_id'] = pid
                    p['text'] = text
                    myarticle['paragraphs'].append(p)            
                    pid += 1

            writer.write(myarticle)

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {n}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--language_reported', required=True, type=str, help='Language reported')
    parser.add_argument('--doc_type', required=True, type=str, help='Doctype')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

