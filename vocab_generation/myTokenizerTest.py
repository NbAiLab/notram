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
    parser.add_argument('tokenizer', help='tokenizer.json')
    parser.add_argument('Inputfile', help='textfile to be tokenized')
    args = parser.parse_args()
    values = [0] * 1000

    with open(args.Inputfile, 'r') as fp:
        contenttmp = fp.read()
        content = contenttmp
        ftfy.fix_text(content)
        print("Loading tokenizer: " + str(args.tokenizer))
        tokenizer = tokenizers.Tokenizer.from_file(args.tokenizer + ".json")
        tokenizer.save(args.tokenizer + "_vocab.txt")
        tokenized = tokenizer.encode(str(content))
        print(tokenized)
        print(type(tokenized))
        # print(tokenized.ids)
        # theTokens=tokenized.tokens.split(",")
        # for i in theTokens:
        #  print(i)
        fp.close()
        print("****** Pairs *****")
    with open(args.Inputfile, 'r') as fp:
        contenttmp = fp.readline()
        content = contenttmp
        ftfy.fix_text(content)
        wordcount = 0
        # content = contenttmp.decode('utf-8', 'ignore').encode("utf-8")
        while contenttmp:
            wordcount += 1
            tokenized = tokenizer.encode(str(content))
            nooftokens = len(tokenized.ids)
            values[nooftokens] += 1
            pstr = str(content)
            print(pstr + str("\t") + str(tokenized.tokens) + str("\t") + str(tokenized.ids))
            contenttmp = ""

            contenttmp = fp.readline()

            content = contenttmp
            ftfy.fix_text(content)
    # content = contenttmp.decode('utf-8', 'ignore').encode("utf-8")
    print("                                        ")
    print("============================================================================")
    print("The file " + args.Inputfile + " contains " + str(wordcount) + " words")
    print("============================================================================")

    for i in range(100):
        if values[i] != 0:
            print(str(values[i]) + " words contains " + str(i) + " tokens")

    print("============================================================================")
