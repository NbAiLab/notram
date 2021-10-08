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

#Surpress warning
fasttext.FastText.eprint = lambda x: None

PRETRAINED_MODEL_PATH = '/usr/local/bin/fasttext/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

def main(args):
    myfile = args.input_file
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
    print(args.input_file)
    print(counter.most_common())


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(description="Loops through a json file and adds language and confidence,")
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_folder', required=True, type=str, help='Output folder')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
    
