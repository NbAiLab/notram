#!/opt/anaconda3/bin/python

#####################################
## Loops through a json file and adds language and confidence
#####################################


import fasttext
import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy
from tqdm import tqdm
import csv
from urllib.parse import urlparse
import collections
import logging
import json

#Surpress warning
fasttext.FastText.eprint = lambda x: None

PRETRAINED_MODEL_PATH = '/usr/local/bin/fasttext/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

def main(args):
    if args.log_file:
        logging.basicConfig(filename=args.log_file, format='%(message)s', level=logging.INFO)
    myfile = args.input_file
    print(f'Starting to process: {args.input_file}')
    output_folder = args.output_folder
    languages = []
    with jsonlines.open(myfile) as reader:
        with jsonlines.open(os.path.join(output_folder,os.path.basename(args.input_file)), mode='w') as writer:
            for n,obj in enumerate(reader):
                text = ""
                for p in obj['paragraphs']:
                    text = text + p['text']
                
                predictions = model.predict(text.replace("\n",""))
                lang = str(predictions[0][0]).replace("__label__","")
                conf = predictions[1][0]
                obj['lang_fasttext'] = lang
                obj['lang_fasttext_conf'] = conf
                writer.write(obj)
                languages.append(lang)


    counter=collections.Counter(languages)
    print("\n")
    print(f'Finished processing {args.input_file}')
    print(args.input_file)
    print(counter.most_common())

    if args.log_file:
        output = {}
        output['filename'] = args.input_file
        output['langcount'] = counter.most_common()
        logging.info(json.dumps(output))

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(description="Loops through a json file and adds language and confidence,")
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_folder', required=True, type=str, help='Output folder')
    parser.add_argument('--log_file', required=False, type=str, default=None, help='Writes to log file if specified')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
    
