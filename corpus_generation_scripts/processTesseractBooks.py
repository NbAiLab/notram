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

import json


removehead=True
removetail=True
publang = {}

pagesorganized = [None] * 4000
bookparagraphs = []


def splittopages(thebook)->str:
    pages=[]
    pagestr=""
    start=True
    for l in thebook:

        if l[0] == chr(12):
            if removetail == True:
                pagestr=pagestr.rstrip()
            
            pages.append(pagestr.lstrip())
            pagestr=""
            start=True
        else:
            if removehead== True and start == True and len(l) <= 2:
                pagestr=pagestr
            else:
                if len(l) > 2:
                    if len(pagestr) > 0 and (pagestr[-1] == '\n'):
                        pagestr = pagestr[:-1]
                    if len(pagestr) > 0 and (pagestr[-1] == '-'):
                        pagestr=pagestr[:-1]
                        pagestr = pagestr + l.rstrip()
                    elif len(pagestr) <= 2:
                        pagestr = l.lstrip()
                    else:
                        pagestr = pagestr  + " " + l.rstrip()
                    pagestr += "\n"
                else:
                    if len(pagestr) <= 2:
                        pagestr = l.lstrip()
                    else:
                        pagestr = pagestr + l
                start= False

    return pages

def concatenatewithnext():
    global pagesorganized
    cntpages=0
    while pagesorganized[cntpages] != None:
        p=pagesorganized[cntpages]
        cntpara=len(pagesorganized[cntpages]) - 1
        if cntpara >=0:
            pa = p[cntpara]
            lastchar = pa.strip()[-1]
            if lastchar != "." and pagesorganized[cntpages+1] != None and len(pagesorganized[cntpages+1])>0:
                nextfirst = pagesorganized[cntpages + 1].pop(0)
                pa=pa.strip()
                hyp=False
                if (pa[-1]) == "-":
                    pa=pa[:-1]
                    hyp=True

                concstr=""
                if (hyp == True):
                    concstr = pa.strip() + nextfirst.strip()
                else:
                    concstr = pa.strip() + " " + nextfirst.strip()
                #concstr = pa.strip() + " " + nextfirst.strip()
                #print("concstr " + concstr)
                p[cntpara] = concstr

        cntpages+=1


def countpages(thebook)->int:
    pagecount = 1
    for l in thebook:
        if l[0] == chr(12):
            pagecount += 1
    return pagecount

def cleanpages(pages)->bool:
    global  pagesorganized
    pagenumber = 1
    for p in pages:
        paragraphstmp=p.split("\n")
        paragraphs=[]
        for pa in paragraphstmp:
            #print("Paragraph: " + pa)
            if (len(pa.strip()) >0):
                paragraphs.append(pa)
        pagesorganized[pagenumber-1]=paragraphs
        pagenumber += 1
    return True

def removefooters():
    global pagesorganized
    for p in pagesorganized:
        if p != None:
            llen=len(p)
            cnt=0
            for pa in p:
                cnt+=1
                if (cnt== len(p)) and pa.strip().isdigit() == True:
                    p.pop()
                    #print(str(len(p)) + pa)

def removeheaders():
    global pagesorganized
    headerset=set()
    for p in pagesorganized:
        if p != None:
            paragraphs=p
            first=True
            for l in paragraphs:
                if (first ==True):
                    #print("xx" + l)
                    if l not in headerset:
                        headerset.add(l)
                    first=False

    for p in pagesorganized:
        if p != None:
            paragraphs=p
            first=True
            head=False
            for l in paragraphs:
                if (first ==True):
                    #print("xx" + l)
                    if l in headerset:
                        #print("Header:" + l)
                        head=True
                    first=False
            if head == True:
                paragraphs.pop(0)

def getPublishedYear(urn):
    result=publang.get(urn,None)
    if result == None:
        return "<unknown>"
    else:
        return result[0]

def buildPublishedAndLanguageDict(dictfile):
    with open(dictfile, "r") as f:
        for line in f:
            parts=line.strip().split("_")
            urn=parts[0] + "_" + parts[1]
            year=parts[2]
            if year == "" or year == None:
                year="<unknown>"
            lang=parts[3]
            if lang == "" or lang == None:
                lang="<unknown>"
            #print(urn + ":" + year + ":" + lang)
            publang[urn]=(year,lang)

def getLanguage(urn):
    result=publang.get(urn,None)
    if result == None:
        return "<unknown>"
    else:
        return result[1]

def detectLanguage(thestr):
    res = str(langid.classify(thestr))
    #res = langid.classify("File with path to all books")
    #print(res)
    detected_language = res.split(",")[0].replace("(","").replace("'","")
    if detected_language == 'no':
        detected_language = 'nob'
    if detected_language == 'nn':
        detected_language = 'nno'
    return detected_language

def writetojsonfile(outputfile):
    pagenumber = 1
    # sys.exit()
    detected_language = ""
    for p in pagesorganized:
        if p != None:
            # print("************************************ Start " + str(pagenumber) + " of " + str(pagecount) + "  ********************************")
            for pa in p:
                # print("Paragraph: " + pa.strip())
                if len(pa.strip()) > 20:
                    if detected_language == "":
                        detected_language = detectLanguage(pa.strip())
            # print("************************************ End  " + str(pagenumber) + " of " + str(pagecount) + "  ************************************")
            pagenumber += 1

    paragraphNumber = 0
    pageNumber = 1
    for p in pagesorganized:
        if p != None:
            # print("************************************ Start " + str(pagenumber) + " of " + str(pagecount) + "  ********************************")
            blockNumber = 1
            for pa in p:
                paragraph = {"paragraph_id": str(paragraphNumber),
                             "page": str(pageNumber),
                             "block": str(blockNumber),
                             "text": ftfy.fix_text(ftfy.fix_text(str(pa.strip())))}
                blockNumber += 1
                paragraphNumber += 1
                bookparagraphs.append(paragraph)
            # print("************************************ End  " + str(pagenumber) + " of " + str(pagecount) + "  ************************************")
            pageNumber += 1

    bookurn = args.book.split("/")[-1].split(".")[0]
    currentjsonObject = {"id": bookurn,
                         "doc_type": "book",
                         "scan_date": str("01012021"),
                         "publish_date": str("0101" + getPublishedYear(bookurn)),
                         "language_reported": getLanguage(bookurn),
                         "language_detected": detected_language,
                         "tesseract_version": "4.1.1",
                         "paragraphs": bookparagraphs}

    currjptr = open(outputfile, "w")
    json.dump(currentjsonObject, currjptr, ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('book', help='Path to book')
    args = parser.parse_args()
    buildPublishedAndLanguageDict("publishedLangUrn.txt")
    pagecount=1
    currentbook=[]
    with open(args.book,"r", encoding="utf-8") as f:
        for line in f.readlines():
            currentbook.append(line)


    pages=splittopages(currentbook)
    pagecount=countpages(currentbook)
    cleanpages(pages)
    removeheaders()
    removefooters()
    concatenatewithnext()
    bookurn = args.book.split("/")[-1].split(".")[0]
    writetojsonfile(bookurn + ".json")
