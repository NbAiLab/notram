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
indexdict = {}

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True


def makesinglecorpusfile(datasetname,corpusfiledir,corpus_output_dir):
    global setname
    setname= datasetname

    dirlist = glob.glob(corpusfiledir.strip() + '/*.json')
    print("start reading corpus files")
    os.makedirs(corpus_output_dir+ "/complete_all/", exist_ok=True)
    for f in os.listdir(corpus_output_dir+ "/complete_all/"):
        os.remove(os.path.join(corpus_output_dir+ "/complete_all/", f))

    os.makedirs(corpus_output_dir + "/data", exist_ok=True)
    print(corpus_output_dir+ "/complete_all/" + datasetname + ".json")
    with open(corpus_output_dir+ "/complete_all/" + datasetname + ".json", 'w') as outfile:
        for fname in dirlist:
            print("reading " + fname)
            with open(fname) as infile:
                for line in infile:
                    if is_json(line) == True:
                        outfile.write(line)

    print("end reading corpus files")

    return


def shuffleandsplitcorpusfile(corpusfile):
    global numberofsplits
    global evalfp
    global trainfp
    global setname
    global indexdict

    tmpfile=corpusfile + ".shuf"
    print("Start shuffling " + corpusfile +" to " +tmpfile)
    shufcmd = 'shuf' + " " + corpusfile + " -o " + tmpfile
    print(shufcmd)
    process = subprocess.Popen(shufcmd,shell=True, stdout=subprocess.PIPE)
    process.wait()
    print("End shuffling")
    filesize=os.path.getsize(tmpfile)
    numberofsplits=math.floor(filesize/maxsplitsize) + 1
    makesplitfiles(corpusfile,numberofsplits)
    print("Start making splits:" + str(numberofsplits) + " for "+ tmpfile)

    with open(tmpfile,"r") as infile:
        for line in infile:
            addtosplitfile(line)
    print("End making splits")
    for myfile in indexdict.keys():
            indexdict[myfile].close()
    return

def makesplitfiles(corpusfile,numberofsplits):
    global splitpointers
    global evalfp
    global trainfp
    global setname
    global indexdict


    splitdir=os.path.dirname(os.path.dirname(corpusfile)) + "/" + "data"
    print("---"+splitdir)
    os.makedirs(splitdir,exist_ok=True)

    for f in os.listdir(splitdir):
        os.remove(os.path.join(splitdir, f))
    os.makedirs(splitdir, exist_ok=True)
    complete_all=os.path.dirname(os.path.dirname(corpusfile)) + "/" + "complete_all"

    evalfp = open(os.path.dirname(complete_all)+"/complete_all/"+ "validate.json", "w")
    trainfp = open(os.path.dirname(complete_all)+ "/complete_all/"+ "train.json", "w")
    cnt=1
    indexdict={}
    prefixname=corpusfile.split("/")[-1].split(".")[0]
    while (cnt<= numberofsplits):
        filename = splitdir + "/train"+ "-shard-" +str(cnt).zfill(4) +"-of-"+ str(numberofsplits).zfill(4) + ".json"
        splitpointers[cnt]=filename
        indexdict[str(cnt)]=open(filename,"w")
        cnt+=1

def addtosplitfile(line):
    global lastusedfileno
    global sizeeval
    global evalfp
    global trainfp
    global maxevallimit
    global indexdict

    #print(str(sizeeval) + " " + str(maxevallimit))
    if (len(line.encode('utf-8')) + sizeeval) <= maxevallimit:
        sizeeval+=len(line.encode('utf-8'))
        evalfp.write(line)
        return
    #print("XXX"+ str(splitpointers[lastusedfileno]) + "XXX")
    trainfp.write(line)
    #fp=open(splitpointers[lastusedfileno],"a")
    fp=indexdict[str(lastusedfileno)]
    fp.write(line)

    lastusedfileno+=1
    if lastusedfileno > numberofsplits:
        lastusedfileno=1


def fileexists(absfile):
    if os.path.isfile(absfile):
        return True
    else:
        return False

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus_output_dir', help='Output dir where all output goes', required=True, type=str)
    parser.add_argument('--corpus_split_size_in_byte', help='Size of chards', required=False, type=str)
    parser.add_argument('--corpus_eval_size_in_byte', help='Size of evauation set', required=False, type=str)

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
    if args.corpus_split_size_in_byte is not None:
        maxsplitsize = int(args.corpus_split_size_in_byte)
    if args.corpus_eval_size_in_byte is not None:
        maxevallimit = int(args.corpus_eval_size_in_byte)
    lastchar=str(args.corpus_output_dir)[-1]

    outdir=""
    if lastchar == "/":
        outdir=str(args.corpus_output_dir)[:-1]
    else:
        outdir = str(args.corpus_output_dir)

    datasetname=outdir.split("/")[-1]
    corpusfiledirfile = args.corpus_output_dir + "/dirspesification.txt"
    if (fileexists(corpusfiledirfile) == False):
        print("dirspesification.txt does not exist for dir: " + args.corpus_output_dir)
        exit(-1)

    dirlistfp = open(corpusfiledirfile, "r")
    indir = dirlistfp.readlines()
    corpusfiledir=indir[0]

    makesinglecorpusfile(datasetname,corpusfiledir,args.corpus_output_dir)
    shuffleandsplitcorpusfile(args.corpus_output_dir + "/complete_all/" + datasetname + ".json")
    # cnt=1
    # while (cnt <= numberofsplits):
    #     fp = open(splitpointers[cnt], "a")
    #     fp.write('\n')
    #     fp.close()
    #     cnt+=1
    shutil.copy(args.corpus_output_dir + "/" + "complete_all/validate.json",args.corpus_output_dir + "/" + "data/validate-shard-0001-of-0001.json")
    print("Start gzip")
    gzipsplitfiles(args.corpus_output_dir + "/data" )
    complete_all = args.corpus_output_dir + "/" + "complete_all"

    evalfp.close()
    gzipsplitfiles(complete_all)
    trainfp.close()
    print("End gzip")
    print("generating datacard")
    cardcmd = './generatedatacard.sh' + " " + "template_datacard.md" + " " + setname + " " + str(numberofsplits) + " " + "no-NN,no-NB,sv-SE,da-DK,fi-FI,fo-FO,is-IS"  + " " +  args.corpus_output_dir
    #print(cardcmd)
    process = subprocess.Popen(cardcmd, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print("generating dataloader")
    loadercmd = './generatedataloader.sh' + " " + "template_dataloader.py" + " " + setname + " " + str(numberofsplits)   + " " +  args.corpus_output_dir
    process = subprocess.Popen(loadercmd, shell=True, stdout=subprocess.PIPE)
    process.wait()

    datacardfrom="README.md"
    # datacardto = args.corpus_output_dir + "/"+ "README.md"
    # dataloaderfrom=setname+".py"
    # dataloaderto = args.corpus_output_dir + "/"+ setname + ".py"
    # shutil.move(dataloaderfrom, dataloaderto)
    # shutil.move(datacardfrom, datacardto)

