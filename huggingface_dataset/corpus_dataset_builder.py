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
from joblib import Parallel, delayed
from tqdm import tqdm
import csv
from urllib.parse import urlparse
import collections
import logging
import gzip

NUMBEROFDUMMYEVAL=2
NUMBEROFDUMMYTRAIN=2

CNTDUMMYTRAIN=0
CNTDUMMYEVAL=0


DUMMYEVALNAME=""
DUMMYTRAINNAME=""
DUMMYEVALFP=None
DUMMYTRAINFP=None



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
dummy_dir=""

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True


def makesinglecorpusfile(datasetname,corpusfiledir,corpus_output_dir):
    global setname
    setname= datasetname

    dirlist = glob.glob(corpusfiledir.strip() + '/*.json*')
    print("start reading corpus files")
    os.makedirs(corpus_output_dir+ "/complete_all/", exist_ok=True)
    for f in os.listdir(corpus_output_dir+ "/complete_all/"):
        os.remove(os.path.join(corpus_output_dir+ "/complete_all/", f))

    os.makedirs(corpus_output_dir + "/data", exist_ok=True)
    #print(corpus_output_dir+ "/complete_all/" + datasetname + ".json")
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
    global DUMMYEVALFP
    global DUMMYTRAINFP
    global dummydir


    splitdir=os.path.dirname(os.path.dirname(corpusfile)) + "/" + "data"
    print("---"+splitdir)
    os.makedirs(splitdir,exist_ok=True)

    # dummydir = os.path.dirname(os.path.dirname(corpusfile)) + "/" + "dummy_data"
    # print("---" + dummydir)
    # os.makedirs(dummydir, exist_ok=True)


    for f in os.listdir(splitdir):
        os.remove(os.path.join(splitdir, f))
    os.makedirs(splitdir, exist_ok=True)
    complete_all=os.path.dirname(os.path.dirname(corpusfile)) + "/" + "complete_all"


    evalfp = open(os.path.dirname(complete_all)+"/complete_all/"+ "validation.json", "w")
    trainfp = open(os.path.dirname(complete_all)+ "/complete_all/"+ "train.json", "w")

    DUMMYEVALFP = jsonlines.open(os.path.dirname(os.path.dirname(corpusfile)) + "/complete_all/"+ "validation-shard-0001-of-0001.json", "w")
    DUMMYTRAINFP = jsonlines.open(os.path.dirname(os.path.dirname(corpusfile)) + "/complete_all/"+ "train-shard-0001-of-"+ str(numberofsplits).zfill(4) + ".json", "w")

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
    global NUMBEROFDUMMYEVAL
    global NUMBEROFDUMMYTRAIN
    global CNTDUMMYTRAIN
    global CNTDUMMYEVAL


    usedindummyeval=False

    if CNTDUMMYEVAL < NUMBEROFDUMMYEVAL:
        if is_json(line) == True:
            myjson=json.loads(line)
            text=myjson['text']
            if len(text.split(".")) > 2:
                dummytext=text.split(".")[0] + "." + text.split(".")[1] + "."
                myjson['text']=dummytext
            usedindummyeval = True
            DUMMYEVALFP.write(myjson)
            CNTDUMMYEVAL+=1

    if usedindummyeval== False and CNTDUMMYTRAIN < NUMBEROFDUMMYTRAIN:
        if is_json(line) == True:
            myjson = json.loads(line)
            text = myjson['text']
            if len(text.split(".")) > 2:
                dummytext = text.split(".")[0] + "." + text.split(".")[1] + "."
                myjson['text'] = dummytext

            DUMMYTRAINFP.write(myjson)
            CNTDUMMYTRAIN += 1

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
    parser.add_argument('--input_folder', help='Folder with all cleaned input json files', required=True, type=str)
    parser.add_argument('--output_folder', help='Folder for  deduplicated jsonl files', required=True, type=str)

    parser.add_argument('--corpus_split_size_in_byte', help='Size of chards', required=False, type=str)
    parser.add_argument('--corpus_eval_size_in_byte', help='Size of evauation set', required=False, type=str)

    args = parser.parse_args()
    return args

def makesinglegzipfile(infile):
    with open(infile, 'rb') as f_in:
        with gzip.open(infile + ".gz", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(infile)
    return True

def gzipsplitfiles(indir):
    filenames=os.listdir(indir)
    out = Parallel(n_jobs=20)(delayed(makesinglegzipfile)(indir + "/" +i) for i in filenames)
    return


if __name__ == '__main__':
    args = parse_args()

    if args.corpus_split_size_in_byte is not None:
        maxsplitsize = int(args.corpus_split_size_in_byte)
    if args.corpus_eval_size_in_byte is not None:
        maxevallimit = int(args.corpus_eval_size_in_byte)
    lastchar=str(args.output_folder)[-1]

    outdir=""
    if lastchar == "/":
        outdir=str(args.output_folder)[:-1]
    else:
        outdir = str(args.output_folder)
    datasetname=outdir.split("/")[-1]

    lastchar = str(args.input_folder)[-1]
    indir = ""
    if lastchar == "/":
        indir = str(args.input_folder)[:-1]
    else:
        indir = str(args.input_folder)

    corpusfiledirfile = ""

    corpusfiledir = indir

    makesinglecorpusfile(datasetname,corpusfiledir,outdir)
    shuffleandsplitcorpusfile(outdir + "/complete_all/" + datasetname + ".json")
    shutil.copy(outdir + "/" + "complete_all/validation.json",outdir + "/" + "data/validation-shard-0001-of-0001.json")
    print("Start gzip data")
    gzipsplitfiles(outdir + "/data" )
    complete_all = outdir + "/" + "complete_all"
    evalfp.close()
    trainfp.close()
    DUMMYEVALFP.close()
    DUMMYTRAINFP.close()
    print("End gzip data")
    print("Running stats")

    statscmd='python generate_stats.py --input_file ' +  outdir + "/" + "complete_all/train.json" + " --output_file " + outdir + "/stats.md"
    print(statscmd)
    process = subprocess.Popen(statscmd, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print("End running stats")
    print("Start gzip complete_all")
    gzipsplitfiles(complete_all)
    print("End gzip complete_all")

    print("generating datacard")
    cardcmd = './generatedatacard.sh' + " " + "template_datacard.md" + " " + setname + " " + str(numberofsplits) + " " + "no-NN,no-NB,sv-SE,da-DK,fi-FI,fo-FO,is-IS"  + " " +  outdir
    #print(cardcmd)
    process = subprocess.Popen(cardcmd, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print("generating dataloader")
    loadercmd = './generatedataloader.sh' + " " + "template_dataloader.py" + " " + setname + " " + str(numberofsplits)   + " " +  outdir
    process = subprocess.Popen(loadercmd, shell=True, stdout=subprocess.PIPE)
    process.wait()

    #print(" end generating dummy zip")
    #datacardfrom="README.md"
    # datacardto = args.corpus_output_dir + "/"+ "README.md"
    # dataloaderfrom=setname+".py"
    # dataloaderto = args.corpus_output_dir + "/"+ setname + ".py"
    # shutil.move(dataloaderfrom, dataloaderto)
    # shutil.move(datacardfrom, datacardto)

