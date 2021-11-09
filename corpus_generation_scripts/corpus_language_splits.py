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
    parser.add_argument('--corpus_input_file', help='Input file to be language split', required=True, type=str)
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



    print("start creating language split for: " + args.corpus_input_file)
    print("Output from split process stored in:  " + args.corpus_output_dir + "/language_splits")
    masteroutputdir=outdir.strip() + "/language_splits"
    relativefilename=args.corpus_input_file.split("/")[-1]
    subfolders = args.languages_separated.split(",")
    os.makedirs(masteroutputdir, exist_ok=True)
    indexdict = {}
    writtento={}

    for fdir in subfolders:
        outputdir=masteroutputdir +"/" + fdir +"/"
        if directoryexists(outputdir) == False:
            os.makedirs(outputdir)
        indexdict[fdir] = open(outputdir+ relativefilename,"w")
        writtento[fdir]=False

    if  directoryexists(masteroutputdir + "/other") == False:
            os.makedirs(masteroutputdir + "/other")
    indexdict['other'] = open(masteroutputdir + "/other/" + relativefilename,"w")
    writtento['other'] = False

    f=args.corpus_input_file
    print("processing file: " +f)
    cnt=0
    with open(f) as infile:
        for line in infile:
            #print("processing line: \n\n" + line + "\n\n")
            #print(masteroutputdir)
            cnt += 1
            if (cnt % 1000000000) == 0:
                print(".", end="", flush=True)

            if is_json(line) == False:
                print("disgarding line")
                continue

            j = json.loads(line)
            lang =j['lang_fasttext']
            if lang in args.languages_separated:
                indexdict[lang].write(line)
                writtento[lang] = True
            else:
                indexdict['other'].write(line)
                writtento['other'] = True
    print()


    for myfile in indexdict.keys():
        if writtento[myfile]== False:
            thename=indexdict[myfile].name
            indexdict[myfile].close()
            if (fileexists(thename)) == True:
                os.unlink(thename)
        else:
            indexdict[myfile].write("\n")
            indexdict[myfile].close()
