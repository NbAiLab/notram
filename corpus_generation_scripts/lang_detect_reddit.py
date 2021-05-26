#!/opt/anaconda3/bin/python

import fasttext
import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy
from tqdm import tqdm
import csv
from urllib.parse import urlparse
import collections

PRETRAINED_MODEL_PATH = '/usr/local/bin/fasttext/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

#For simplicity, the output-folder is set as a static here
outputfolder = "/nfsmounts/datastore/corpus/v2/source_1/reddit/"


def main(args):
    myfile = args.input_file
    languages = []
    with jsonlines.open(myfile) as reader:
        with jsonlines.open(outputfolder+"en/"+os.path.basename(args.input_file)+"_en", mode='w') as en_writer:
            with jsonlines.open(outputfolder+"no/"+os.path.basename(args.input_file)+"_no", mode='w') as no_writer:
                with jsonlines.open(outputfolder+"sv/"+os.path.basename(args.input_file)+"_sv", mode='w') as sv_writer:
                    with jsonlines.open(outputfolder+"da/"+os.path.basename(args.input_file)+"_da", mode='w') as da_writer:
                        with jsonlines.open(outputfolder+"is/"+os.path.basename(args.input_file)+"_is", mode='w') as is_writer:

                            for n,obj in enumerate(reader):
                                #print(obj['body'])
                                predictions = model.predict([obj['body'].replace("\n","")]) 
                                lang = str(predictions[0][0][0]).replace("__label__","")
                                conf = predictions[1][0][0]


                                if len(obj['body']) >= 20 and conf>= 0.7:
                                    if lang == "en":
                                        en_writer.write(obj)
                                    if lang == "no":
                                        no_writer.write(obj)
                                    if lang == "sv":
                                        sv_writer.write(obj)
                                    if lang == "da":
                                        da_writer.write(obj)
                                    if lang == "is":
                                        is_writer.write(obj)
                                    
                                    languages.append(lang)


    counter=collections.Counter(languages)
    print(counter.most_common())



def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    args = parser.parse_args()
    return args
 

if __name__ == "__main__":
    args = parse_args()
    main(args)

