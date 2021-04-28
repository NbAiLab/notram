####################################################################################
# Create jsonl from mupdf-created Maalfrid documents
# This corpus is formed as a document per file. Every page is a document
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy
from tqdm import tqdm
import csv
from urllib.parse import urlparse

def main(args):
    ##Set in parameters later
    files = glob.glob('/mnt/lv_ai_1_ficino/sprakbanken_test_output/*.*')
    input_file = "/mnt/lv_ai_1_ficino/pdf_warcinfo.csv"
    
    
    print("starting to load csv meta-file")
    df = pd.read_csv(input_file, encoding='utf-8', dtype='string')
    print("Finished loading csv meta-file")

        

    artid = 0
    
    with jsonlines.open(args.output_file, 'w') as writer:

        for input_file in files:
            with open(input_file) as f:    
                hash = os.path.basename(f).replace(".txt","")
                item = df[df.content_hash == hash].iloc[0]
                domain = urlparse(item['target_uri']).netloc
                name, ext = domain.split('.')[-2:]
                myarticle = {}
                myarticle['doc_type'] = "maalfrid_"+name
                myarticle['id'] = "maalfrid_"+name+"_"+hash
                myarticle['target_url'] = item['target_uri']
                myarticle['language_reported'] = args.language_reported
                myarticle['paragraphs'] = [] 
            
                pid = 0
                for n, line in tqdm(enumerate(f)): 
                    if line != "\n":
                        p = {}
                        p['paragraph_id'] = pid
                        p['text'] = str(ftfy.fix_text(line.rstrip("\n")))
                        myarticle['paragraphs'].append(p)
                        pid += 1

                #Write the article
                writer.write(myarticle)


    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {n}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--language_reported', required=False, default="N/A", type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doctype', required=True, type=str, help='For instance cc-100')
    parser.add_argument('--input_folder', required=True, type=str, help='Input folder')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

