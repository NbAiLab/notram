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

    args = parser.parse_args()

    for tok in glob.glob('generated_tokenizers/*.json'):
        for tfile in glob.glob('testfiles_1000w/*.txt'):
            values = [0] * 1000
            with open(tfile, 'r') as fp:
                contenttmp = fp.read()
                content = contenttmp
                ftfy.fix_text(content)
                #print("Loading tokenizer: " + str(tok))
                tokenizer = tokenizers.Tokenizer.from_file(tok)

                tokname=tok.split(".")[1]
                print("============================================================================")
                astr="Freddy ved Nasjonalbiblioteket har laget denne . Tester Æ Ø Å æ ø å ."
                #tokenizer._save_pretrained("model/"+tokname)
                tokenized = tokenizer.encode(str(astr))
                #print(tokenized)
                #print(type(tokenized))

                print("\"" + astr + "\"\t ----->\t " + str(tokenized.ids) )
                # theTokens=tokenized.tokens.split(",")
                # for i in theTokens:
                #  print(i)
                fp.close()
                #print("****** Pairs *****")
            with open(tfile, 'r') as fp:
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
                    #print(pstr + str("\t") + str(tokenized.tokens) + str("\t") + str(tokenized.ids))
                    contenttmp = ""

                    contenttmp = fp.readline()

                    content = contenttmp
                    ftfy.fix_text(content)
                fp.close()
            # content = contenttmp.decode('utf-8', 'ignore').encode("utf-8")
            print("                                        ")

            print ("Tokenizer" + str(tok))
            print("The file " + tfile + " contains " + str(wordcount) + " words")
            print(str(values[1]) + " of " + str(wordcount) + " words in file are single tokens, percentage: " + str(values[1]/wordcount))
            print("============================================================================")


            # for i in range(100):
            #     if values[i] != 0:
            #         print(str(values[i]) + " words contains " + str(i) + " tokens")

            print("============================================================================")
