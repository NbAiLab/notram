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
import uuid
import sys
import shutil
from datetime import date,datetime

def printwithtime(ostring):
    now = datetime.now()
    mystrdate=now.strftime("%Y/%m/%d %H:%M:%S")
    print(mystrdate + "\t\t"+ ostring)

def changedoctype(inputfile,doctype_from,doctype_to):
    values_changed = 0
    num_lines = 0
    
    unique_filename = str(uuid.uuid4())
    tmpfile="/tmp/" + unique_filename
    outputfilefp = jsonlines.open(tmpfile, "w")
    with open(inputfile, "r") as reader:
        for l in reader:
            num_lines += 1
            j = json.loads(l)
            if 'doc_type' in j and j['doc_type']== doctype_from:
                j['doc_type'] = doctype_to
                values_changed += 1
            outputfilefp.write(j)
    outputfilefp.close()
    shutil.move(tmpfile,inputfile)
    print(f"Finished {inputfile}. {values_changed} of {num_lines} values_changed")
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





