####################################################################################
# Cleaning up parliament speech files
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
from collections import Counter
import random 
from itertools import islice
import glob
import pandas as pd

#Norwegian Spacy
#import spacy
#from spacy.lang.nb.examples import sentences
#nlp = spacy.load('nb_core_news_sm')




def main(args):
    num_samples = 3000
    cur_sample = 0
    lastscore = 2
    data = pd.DataFrame(columns=['above96', 'confidence', 'text'])

        
    metafiles = glob.glob('/nfsmounts/meta2/disk4/folder1/nancy/content/text/v3/text_meta_source_1/book/2019/*/*/*.meta')
    #metafiles = glob.glob('/nfsmounts/meta2/disk4/folder1/nancy/content/text/newspaper/nonpdf/text/2015/01/01/*/*.meta')
    #print(metafiles)
    
    for mfile in metafiles:
        mobj = pd.read_json(mfile, typ='index')

        tfile = mfile.replace(".meta",".txt")
        if len(mobj.paragraphs) != 0:
            article = pd.read_csv(tfile, sep='\r', skip_blank_lines=False, encoding='utf-8',squeeze=True, header=None,quotechar=None, quoting=3, dtype='str')
        
        for n, p in enumerate(mobj.paragraphs):
            if float(p['confidence']) <= 0.95:
                plength =len(article[n].split())
                if plength > 10 and plength < 100 and lastscore != 0 and cur_sample<num_samples:
                    print(f'0 - {mfile} - {article[n]}')
                    data = data.append({'above96': '0', 'confidence': p['confidence'], 'text': article[n]}, ignore_index=True)
                    lastscore = 0
                    cur_sample += 1


        for n,p in enumerate(mobj.paragraphs):
            if float(p['confidence']) > 0.96:
                plength =len(article[n].split())
                if plength > 10 and plength < 100 and lastscore != 1 and cur_sample<num_samples:
                    print(f'1 - {mfile} - {article[n]}')
                    data = data.append({'above96': '1', 'confidence': p['confidence'], 'text': article[n]}, ignore_index=True)
                    lastscore = 1
                    cur_sample += 1
   
    #Shuffle
    data = data.sample(frac = 1) 
    
    #Print
    data.to_csv(args.output_file, index=False)
    #print(data)

    #print(f'A total number of {num_samples} for both bokmål and nynorsk is written to file {args.output_file}')



def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
   args = parse_args()
   main(args)

