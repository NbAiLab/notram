import sys
import os
import math
import numpy as np
import glob
import argparse
from os import path

from xmlHandler import xmlHandler
from altoProcessor import altoProcessor

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('listofbooks', help='File with path to all books')

    args = parser.parse_args()
    bookProcessor=altoProcessor()
    bookProcessor.buildPublishedAndLanguageDict("publishedLangUrn.txt")

    with open(args.listofbooks) as fp:
        line=fp.readline().strip()
        cnt=1
        while line:
            line=line.strip('\'')
            print(str(cnt) + "\t" + line)
            res=bookProcessor.initBook(line)
            print(res)
            if res == True:
                bookProcessor.ReadBook()
                bookProcessor.printSingleFiles("tmp")
                line = fp.readline().strip()
                cnt+=1
            else:
                line = fp.readline().strip()
                cnt += 1

