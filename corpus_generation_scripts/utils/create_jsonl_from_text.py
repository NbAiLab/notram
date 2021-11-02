####################################################################################
# Create jsonl from a flat text file
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy
import os
from tqdm import tqdm

def main(args):
    with jsonlines.open(args.output_file, 'w') as writer:
        artid = 0
        with open(args.input_file,"r") as f: 
            for n,text in enumerate(f):
                myarticle = {}
                myarticle['id'] = args.doc_type + "_"+str(n)
                myarticle['doc_type'] = str(args.doc_type)
                myarticle['text'] = ftfy.fix_text(text.replace("\n",""))
                writer.write(myarticle)

    print(f'Saved file: {args.output_file}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc_type', required=True, type=str, help='Also used as refix to the id')
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

