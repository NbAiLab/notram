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



def counthyphens(mystr):
    hypcount=0
    prevchar='a'
    for c in mystr:
        if c == '"' and prevchar !="\\":
            hypcount += 1
        prevchar=c

    return hypcount

def countsingequotes(mystr):
    hypcount=0
    prevchar='a'
    for c in mystr:
        if c == "'" and prevchar !="\\":
            hypcount += 1
        prevchar=c

    return hypcount


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sourcejsonlfile', help='source filename')
    parser.add_argument('destjsonlfile', help='repaired file name will be overwritten')

    args = parser.parse_args()
    writer=jsonlines.open(args.destjsonlfile, mode='w')


    cnttotal=0
    print("fixing (. is 10000 records) ",flush=True)
    #fflush(stdout)

    maxlen = 100000

    with open(args.sourcejsonlfile) as reader:
            for l in reader:
                cleanl = ''.join(c for c in l if c.isprintable())
               
                try:
                    j=json.loads(cleanl)
                    j['id'] = str(j['id'])
                    #Check if this is a deduplicated file. If so, it should be trimmed to maxlen
                    #If there is no text field - just ignore this
                    text = j.get('text', "")
                    currentlen = len(text)

                    if currentlen > maxlen:
                        text = j['text']
                        chunks = [text[i:i+maxlen] for i in range(0, len(text), maxlen)]
                        for n,c in enumerate(chunks):
                            k = {}
                            k['id'] = j['id']+"_"+str(n)
                            k['text'] = c
                            writer.write(k)
                        print(f'Text longer than {maxlen}. Split in {n+1} chunks.')
                    else:
                        writer.write(j)
                    
                    cnttotal += 1
                    if ((cnttotal % 10000) == 0):
                        print(".", end="", flush=True)
                except:
                    print("erroneous json record ["+l +"]")
                    continue
    writer.close()
    print("\n")
    print("The file: " + args.sourcejsonlfile + " contained " +str(cnttotal) + " jsonl records! These are written to file: " + args.destjsonlfile)







