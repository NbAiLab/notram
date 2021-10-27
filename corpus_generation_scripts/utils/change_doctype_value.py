import sys
import os
import math
import numpy as np
import glob
import argparse

from os import path
import unicodedata
from string import printable
import ftfy
import jsonlines
import json

import sys
import shutil
from datetime import date,datetime

def printwithtime(ostring):
    now = datetime.now()
    mystrdate=now.strftime("%Y/%m/%d %H:%M:%S")
    print(mystrdate + "\t\t"+ ostring)

def changedoctype(inputfile,doctype_from,doctype_to):
    tmpfile="/tmp/" + inputfile.split("/")[-1]
    outputfilefp = jsonlines.open(tmpfile, "w")
    with open(inputfile, "r") as reader:
        for l in reader:
            j = json.loads(l)
            if 'doc_type' in j and j['doc_type']== doctype_from:
                j['doc_type'] = doctype_to
            outputfilefp.write(j)
    outputfilefp.close()
    shutil.move(tmpfile,inputfile)
    return True

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--corpus_input_file', help='Source corpus file', required=True, type=str)
    parser.add_argument('--existing_doctype_value', help='original doc type in file', required=True, type=str)
    parser.add_argument('--new_doctype_value', help='destination doc type in file', required=True, type=str)

    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = parse_args()
    changedoctype(args.corpus_input_file,args.existing_doctype_value,args.new_doctype_value)





