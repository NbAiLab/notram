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

EVALNAME="eval.json"
maxsplitsize=1073741824
#maxsplitsize=102400

maxevallimit=1073741824
#maxevallimit=102400

splitpointers=[" "]*200000
numberofsplits=0
lastusedfileno=1
evalfile="eval.json"
sizeeval=0
evalfp=None
TRAINNAME="train.json"
trainfp=None

setname=""

def makesinglecorpusfile(datasetname,corpusfiledir,corpus_output_dir):
    global setname
    setname=datasetname
    dirlist = sorted(glob.glob(corpusfiledir + '/*.jsonl'))
    with open(corpus_output_dir+ "/" + datasetname + ".json", 'w') as outfile:
        for fname in dirlist:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

    return


def shuffleandsplitcorpusfile(corpusfile):
    global numberofsplits
    global evalfp
    global trainfp
    global setname
    tmpfile=corpusfile + ".shuf"
    print("Start shuffling")
    shufcmd = 'shuf' + " " + corpusfile + " -o " + tmpfile
    process = subprocess.Popen(shufcmd,shell=True, stdout=subprocess.PIPE)
    process.wait()
    print("End shuffling")
    filesize=os.path.getsize(tmpfile)
    numberofsplits=math.floor(filesize/maxsplitsize) + 1
    makesplitfiles(corpusfile,numberofsplits)
    print("Start making splits")
    with open(tmpfile,"r") as infile:
        for line in infile:
            addtosplitfile(line)
    print("End making splits")

    return

def makesplitfiles(corpusfile,numberofsplits):
    global splitpointers
    global evalfp
    global trainfp
    global setname
    splitdir=os.path.dirname(corpusfile) + "/" + "splits"
    os.makedirs(splitdir,exist_ok=True)

    for f in os.listdir(splitdir):
        os.remove(os.path.join(splitdir, f))
    evalfp = open(splitdir + "/" + setname + "_" + EVALNAME, "w")
    trainfp = open(splitdir + "/" + setname + "_" + TRAINNAME, "w")
    cnt=1

    prefixname=corpusfile.split("/")[-1].split(".")[0]
    while (cnt<= numberofsplits):
        filename = splitdir + "/"+ prefixname + "-shard-" +str(cnt).zfill(4) +"-of-"+ str(numberofsplits).zfill(4) + ".json"
        splitpointers[cnt]=filename
        cnt+=1

def addtosplitfile(line):
    global lastusedfileno
    global sizeeval
    global evalfp
    global trainfp
    global maxevallimit
    #print(str(sizeeval) + " " + str(maxevallimit))
    if (len(line.encode('utf-8')) + sizeeval) <= maxevallimit:
        sizeeval+=len(line.encode('utf-8'))
        evalfp.write(line)
        return
    #print("XXX"+ str(splitpointers[lastusedfileno]) + "XXX")
    trainfp.write(line)
    fp=open(splitpointers[lastusedfileno],"a")
    fp.write(line)
    fp.close()
    lastusedfileno+=1
    if lastusedfileno > numberofsplits:
        lastusedfileno=0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus_dataset_name', help='Name of dataset', required=True, type=str)
    parser.add_argument('--corpus_file_dir', help='Path to corpusfile', required=True, type=str)
    parser.add_argument('--corpus_output_dir', help='Path to corpus output dir', required=True, type=str)
    args = parser.parse_args()
    return args

def gzipsplitfiles(indir):
    filenames=os.listdir(indir)
    for f in filenames:
        with open(indir + "/" +f, 'rb') as f_in:
            with gzip.open(indir + "/" +f + ".gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(indir + "/" +f)

if __name__ == '__main__':

    args = parse_args()
    makesinglecorpusfile(args.corpus_dataset_name,args.corpus_file_dir,args.corpus_output_dir)
    shuffleandsplitcorpusfile(args.corpus_output_dir + "/" + args.corpus_dataset_name + ".json")
    cnt=1
    while (cnt <= numberofsplits):
        fp = open(splitpointers[cnt], "a")
        fp.write('\n')
        fp.close()
        cnt+=1
    gzipsplitfiles(args.corpus_output_dir + "/splits" )
    evalfp.close()
    trainfp.close()
    evalnamefrom = args.corpus_output_dir + "/splits" + "/" + args.corpus_dataset_name + "_" + EVALNAME + ".gz"
    evalnameto = args.corpus_output_dir  + "/" + args.corpus_dataset_name + "_" + EVALNAME + ".gz"
    trainnamefrom = args.corpus_output_dir + "/splits" + "/" + args.corpus_dataset_name + "_" + TRAINNAME + ".gz"
    trainnameto = args.corpus_output_dir + "/" + args.corpus_dataset_name + "_" + TRAINNAME + ".gz"

    shutil.move(evalnamefrom,evalnameto)
    shutil.move(trainnamefrom, trainnameto)