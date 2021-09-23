####################################################################################
# Create jsonl from the Lovdata CD
# This content does have double breaks between each artile. Some meta-info is collected from the file names 
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy
import os
from tqdm import tqdm

def main(args):
    #Get list of file
    files = glob.glob(args.input_folder+"*.txt")
    
    with jsonlines.open(args.output_file, 'w') as writer:
        artid = 0

        for myfile in files:
            with open(myfile,"r") as f: 
                artid += 1
                basename = os.path.basename(myfile).split('.txt')[0]        
                print(f'Starting to parse {basename}')
                pid=0
                myarticle = {}
                myarticle['doc_type'] = str(args.doc_type)+"_"+basename
                myarticle['id'] = args.doc_type + "_"+str(artid)
                myarticle['language_reported'] = args.language_reported
                myarticle['paragraphs'] = [] 

                for n, line in tqdm(enumerate(f)): 
                    if line != "\n":
                        p = {}
                        p['paragraph_id'] = pid
                        p['text'] = str(ftfy.fix_text(line.rstrip("\n")))
                        myarticle['paragraphs'].append(p)
                        pid += 1

                    else:
                        writer.write(myarticle)
                        artid += 1
                        pid = 0
                        myarticle = {}
                        myarticle['doc_type'] = str(args.doc_type)+"_"+basename
                        myarticle['id'] = args.doc_type + "_" + str(artid)
                        myarticle['language_reported'] = str(args.language_reported)
                        myarticle['paragraphs'] = [] 
                
                #Just writes the last article as well
                writer.write(myarticle)

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {artid}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--language_reported', required=True, type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True, type=str, help='For instance cc100_no')
    parser.add_argument('--input_folder', required=True, type=str, help='Input file')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

