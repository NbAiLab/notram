import glob
from nltk import ngrams
import random, json, glob, os, codecs, random
import numpy as np
import glob
import ftfy

import argparse
from os import path

from tokenizers import BertWordPieceTokenizer, tokenizers

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('tokenizer', help='Absolute path to "tokenizer".json fil')
    parser.add_argument('sentence', help='Sentence to be tokenized')
    args = parser.parse_args()
    tokenizer = tokenizers.Tokenizer.from_file(args.tokenizer)
    astr=args.sentence
    tokenized = tokenizer.encode(str(astr))
    print("                                          ")
   

    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Setning: " + astr )


    print("---------------------------------------------------------------------------------------------------------------------------------")
    cnt=0
    thestr=""

    for i in tokenized.tokens:
        if (cnt == len(tokenized.tokens)-1):
            mystr=i+"("+str(tokenized.ids[cnt])+") "
            thestr+=mystr
        else:
            mystr = i + "(" + str(tokenized.ids[cnt]) + "),"
            thestr += mystr
        cnt+=1
    print("Tokenisering: "+thestr)