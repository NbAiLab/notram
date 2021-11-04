import sys
import os
import math
import numpy as np
import glob
import argparse
import math
import subprocess

from os import path
import unicodedata
from string import printable
import ftfy
import jsonlines
import json
import pickle
import fasttext
import hashlib
import sys
import shutil
from datetime import date,datetime

from tqdm import tqdm
import csv
from urllib.parse import urlparse
import collections
import logging
import gzip

def fileexists(absfile):
    if os.path.isfile(absfile):
        return True
    else:
        return False


def directoryexists(dir):
    if os.path.isdir(dir):
        return True
    else:
        return False

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus_input_dir', help='Input dir with files to be language split', required=True, type=str)
    parser.add_argument('--corpus_output_dir', help='Master output dir for language splitted files', required=True, type=str)
    parser.add_argument('--languages_separated', help='languages to be separated, default="no,nn,en,sv,da,is,fo"', required=False,
                        type=str,default='no,nn,en,sv,da,is,fo')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    outdir=""
    lastchar = str(args.corpus_output_dir)[-1]
    if lastchar == "/":
        outdir=str(args.corpus_output_dir)[:-1]
    else:
        outdir = str(args.corpus_output_dir)

    dirlist = glob.glob(args.corpus_input_dir + '/*.json')
    print("start creating language split for: " + args.corpus_input_dir)
    print("Output from split process stored in:  " + args.corpus_output_dir + "/language_splits")
    masteroutputdir=args.corpus_output_dir.strip() + "/language_splits"
    # if directoryexists(masteroutputdir) == True:
    #     shutil.rmtree(masteroutputdir)
    os.makedirs(masteroutputdir, exist_ok=True)

    for f in dirlist:
        print("processing file: " +f)
        with open(f) as infile:
            for line in infile:
                #print("processing line: \n\n" + line + "\n\n")
                #print(masteroutputdir)
                if is_json(line) == False:
                    continue

                j = json.loads(line)
                lang =j['lang_fasttext']
                if lang in args.languages_separated:
                    outputdir = masteroutputdir + "/" + lang
                else:
                    outputdir = masteroutputdir + "/other"

                if directoryexists(outputdir) == False:
                    os.makedirs(outputdir)

                fp=open(outputdir+ "/" +f.split("/")[-1],"a")
                fp.write(line)
                fp.close()

    subfolders = [ f.path for f in os.scandir(masteroutputdir) if f.is_dir() ]
    for fdir in subfolders:
        #print(fdir)
        dirlist = glob.glob(fdir +  '/*.json')
        for f in dirlist:
            #print(f)
            fp = open(f, "a")
            fp.write("\n")
            fp.close()



