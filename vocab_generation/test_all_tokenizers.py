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
    toknames=[]
    filenames=[]
    singletokens=[]
    totaltokens=[]
    totalwordcount=[]

    for tok in glob.glob('tokenizers/*.json'):


        for tfile in glob.glob('testfiles_1000w/*.txt'):
            values = [0] * 1000
            with open(tfile, 'r') as fp:
                contenttmp = fp.read()
                content = contenttmp
                ftfy.fix_text(content)
                #print("Loading tokenizer: " + str(tok))
                tokenizer = tokenizers.Tokenizer.from_file(tok)

                tokname=tok.split(".")[0].split("/")[1]
                print("============================================================================")
                #astr="Freddy ved Nasjonalbiblioteket har laget denne, vi tester Æ Ø Å æ ø å ."
                astr="Denne gjengen håper at de sammen skal bidra til å gi kvinnefotballen i Kristiansand et lenge etterlengtet løft."
                #tokenizer._save_pretrained("model/"+tokname)
                tokenized = tokenizer.encode(str(astr))
                #print(tokenized)
                #print(type(tokenized))

                print("\"" + astr + "\"\t ----->\t " + str(tokenized.tokens) + " ----> " + str(tokenized.ids) )
                # theTokens=tokenized.tokens.split(",")
                # for i in theTokens:
                #  print(i)
                fp.close()
                #print("****** Pairs *****")
                sumTokens=0
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
                    sumTokens+= nooftokens
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
            print("The file " + tfile + " contains " + str(wordcount) + " words and " + str(sumTokens) + " tokens")
            print(str(values[1]) + " of " + str(wordcount) + " words in file are single tokens, percentage: " + str(values[1]/wordcount))
            print("============================================================================")
            if tokname not in toknames:
                toknames.append(tokname)
            if  tfile.split("/")[1] not in filenames:
                filenames.append(tfile.split("/")[1])
            singletokens.append(values[1])
            totaltokens.append(sumTokens)
            totalwordcount.append(wordcount)



            # for i in range(100):
            #     if values[i] != 0:
            #         print(str(values[i]) + " words contains " + str(i) + " tokens")

            print("============================================================================")
        #print(str(tok) + "\t\t" + str(boktokens)  + "\t\t"  + str(avistokens) + "\t\t"  + str(jusstokens) + "\t\t"  + str(rapptokens))
    longesttokname=0
    for i in toknames:
        if len(i) > longesttokname:
            longesttokname=len(i)
    numberoftabs=int(longesttokname/8)
    cnt_tok=0
    cnt=0
    print( "---------------------------------------------------------------------------------------------------------------------------------")
    print("Tokenizer" + "\t\t\t\t"+ "Juss" + "\t\t\t"+ "avis" + "\t\t\t"+ "Rapport"  + "\t\t\t"+ "Roman" )
    print("---------------------------------------------------------------------------------------------------------------------------------")
    while (cnt_tok < len(toknames)):
        tname=""
        tokspacelen=int(len(toknames[cnt_tok])/8)
        tname = toknames[cnt_tok]
        j=0
        #print(numberoftabs)
        while tokspacelen<=numberoftabs:
            tname+="\t"
            tokspacelen+=1

        print(tname +  str(totaltokens[cnt])+ "("+ str(singletokens[cnt])+")" + "\t\t" + str(totaltokens[cnt+1])+ "("+ str(singletokens[cnt+1])+")" + "\t\t" + str(totaltokens[cnt+2])+ "("+ str(singletokens[cnt+2])+")" \
              + "\t\t" + str(totaltokens[cnt+3])+ "("+ str(singletokens[cnt+3])+")" + "\t\t" )
        cnt_tok += 1
        cnt+=4
    print("---------------------------------------------------------------------------------------------------------------------------------")