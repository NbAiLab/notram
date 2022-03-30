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
import langid
import jsonlines
import datetime
import json
import glob


def counthyphens(mystr):
    hypcount = 0
    prevchar = 'a'
    for c in mystr:
        if c == '"' and prevchar != "\\":
            hypcount += 1
        prevchar = c

    return hypcount


def countsingequotes(mystr):
    hypcount = 0
    prevchar = 'a'
    for c in mystr:
        if c == "'" and prevchar != "\\":
            hypcount += 1
        prevchar = c

    return hypcount


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sourcejsonldir', help='source filedir')
    args = parser.parse_args()
    for f in glob.glob(args.sourcejsonldir + "/*.json*"):
        writer = jsonlines.open("tmp.jsonlcpy", mode='w')
        cnttotal = 0
        print("Fixing file:" + f + "(. is 10000 records) ", flush=True)
        with open(f) as reader:
            for l in reader:
                cleanl = ''.join(c for c in l if c.isprintable())

                try:
                    j = json.loads(cleanl)
                    writer.write(j)

                    cnttotal += 1
                    if ((cnttotal % 10000) == 0):
                        print(".", end="", flush=True)
                except:
                    print("erroneous json record [" + l + "]")
                    continue
        writer.close()
        os.rename("tmp.jsonlcpy",f)

        print("The file: " + f + " contained " + str(cnttotal) + " jsonl records! These are written to file " )

