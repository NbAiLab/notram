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
    parser.add_argument('book', help='Path to book')


    args = parser.parse_args()


    bookProcessor=altoProcessor()
    bookProcessor.buildPublishedAndLanguageDict("publishedLangUrn.txt")
    res = bookProcessor.initBook(args.book)
    if res == True:
        bookProcessor.ReadBook()
        #bookProcessor.printSingleFiles("tmp")
        bookProcessor.printSingleFiles("/disk4/folder1/nancy/content/text/book/text")



