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
import pickle

import hashlib
import sys
import shutil
from datetime import date,datetime



def printwithtime(ostring):
    now = datetime.now()
    mystrdate=now.strftime("%Y/%m/%d %H:%M:%S")
    print(mystrdate + "\t\t"+ ostring)


def fileexists(absfile):
    if os.path.isfile(absfile):
        return True
    else:
        return False


def directoryexists(dir):
    if os.path.isdir(dir):
        return True
    else:
        return False


def md5(fstr):
    # fstr.encode("UTF-8")
    hash_md5 = hashlib.md5()
    hash_md5.update(fstr.encode('UTF-8'))
    return (hash_md5.hexdigest())


def writepickledfile(sumdict, picklefile):
    output = open(picklefile, 'wb')
    pickle.dump(sumdict, output)
    output.close()


def readpickledFile(picklefile):
    pkl_file = open(picklefile, 'rb')
    hashdict = pickle.load(pkl_file)
    pkl_file.close()
    return hashdict


def max(a, b):
    if (a > b):
        return a
    else:
        return b


def combine_dicts(dict1, dict2):
    for k, v in dict2.items():
        if k not in dict1:
            val=(v,0)
            dict1[k] = val
        else:
            if v > dict1[k][0]:
                val = (v, 0)
                dict1[k] = val
    return dict1


def fileexists(absfile):
    if os.path.isfile(absfile):
        return True
    else:
        return False


def indexlevel_1(jsonlfilename, indexfilename):
    printwithtime("Indexing level 1 file:" + jsonlfilename + " to " + indexfilename)
    hashdict = {}
    with open(jsonlfilename, "r") as reader:
        cnttotal = 0
        for l in reader:
            j = json.loads(l)
            # printwithtime(j)
            jlen = j['doc_length']
            for pa in j['paragraphs']:
                patxt = pa['text']
                # printwithtime(patxt)
                hsh = md5(patxt)
                if hsh in hashdict:
                    if hashdict[hsh] < jlen:
                        hashdict[hsh] = jlen
                else:
                    hashdict[hsh] = jlen

            cnttotal += 1
            if ((cnttotal % 10000) == 0):
                print(".", end="", flush=True)

        print("\n")
        printwithtime("Finished level 1 indexing of " + jsonlfilename)
        #printwithtime("Writing index to pickled file " + indexfilename)
        #writepickledfile(hashdict, indexfilename)
        return hashdict

def buildaggregatedindex(indexfiledir, outputaggregatdindexfilename):
    dirlist = glob.glob(indexfiledir + '/*.idx', recursive=False)
    sumdict = {}
    for f in dirlist:
        printwithtime("Using level 1 index file:" + f)
        with open(f, "r") as reader:
            currentdict = readpickledFile(f)
            newdict = combine_dicts(sumdict, currentdict)
            sumdict = newdict

    printwithtime("Start Writing accumulated index to pickled file " + outputaggregatdindexfilename)
    writepickledfile(sumdict,outputaggregatdindexfilename)
    printwithtime("Finished Writing accumulated index to pickled file " + outputaggregatdindexfilename)
    return sumdict

def printaggregatedindex(sumdict,outputaggregatdindexfilename):
    printwithtime("Start Writing accumulated index to pickled file " + outputaggregatdindexfilename)
    writepickledfile(sumdict, outputaggregatdindexfilename)
    printwithtime("Finished Writing accumulated index to pickled file " + outputaggregatdindexfilename)


def appenddict(sumdict,appdict):
    newdict = combine_dicts(sumdict, appdict)
    return newdict

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus_output_dir', help='Dir for resulting corpus files', required=True, type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = parse_args()
    start = datetime.now()
    printwithtime("Start")
    cnttotal = 0
    outputdir = args.corpus_output_dir
    outputindexdir = outputdir + "/tmp"
    filelistfile = outputdir + "/filelist.txt"
    if directoryexists(outputindexdir ) == False:
        os.makedirs(outputindexdir )
    else:
        shutil.rmtree(outputindexdir)
        os.makedirs(outputindexdir)

    if (fileexists(filelistfile) == False):
        printwithtime("Filelist does not exist for dir: " + args.corpus_output_dir)
        exit(-1)

    filelistfp = open(filelistfile, "r")
    listoffilestoinclude = filelistfp.readlines()
    filelistfp.close()
    relativesettoinclude=set()
    relativefilenamesok = True
    for l in listoffilestoinclude:
        if l.split("/")[-1].strip() in relativesettoinclude:
            relativefilenamesok=False
        else:
            relativesettoinclude.add(l.split("/")[-1].strip())


    if relativefilenamesok == True:
        printwithtime("Relative file names are ok for: " + args.corpus_output_dir)
    else:
        printwithtime("Relative file names are not ok for: " + args.corpus_output_dir)

    sumdict = {}
    for l in listoffilestoinclude:
        relindexfilename=l.strip().replace("/","_").split(".")[0] + ".idx"
        indexfilename = outputindexdir + "/" +relindexfilename
        ldict=indexlevel_1(l.strip(), indexfilename)
        sumdict=appenddict(sumdict,ldict)

    #aggdict = buildaggregatedindex(outputindexdir, outputdir + "/aggregatedindex.aidx" )
    printaggregatedindex(sumdict,outputdir + "/aggregatedindex.aidx" )
    aggdict=sumdict
    printwithtime("Aggregated dictionary size: " + str(len(aggdict)))
    printwithtime("Start writing corpus files")
    #print(aggdict)
    for l in listoffilestoinclude:
        outfilename = ""
        if relativefilenamesok == True:
            outfilename = outputdir + "/" + l.split("/")[-1].strip()
        else:
            outfilename=outputdir + "/" + l.strip().replace("/","_")

        outputfilefp = jsonlines.open(outfilename, "w")
        srcfilename = l.strip()
        printwithtime("Writing corpus file: " +  outfilename)
        with open(srcfilename, "r") as reader:
            cnttotal = 0
            for l in reader:
                j = json.loads(l)
                # printwithtime(j)
                outputstring = ""
                jlen = j['doc_length']
                for pa in j['paragraphs']:
                    patxt = pa['text']
                    # printwithtime(patxt)
                    hsh = md5(patxt)
                    if hsh in aggdict:
                        if aggdict[hsh][0] == jlen and aggdict[hsh][1] == 0:
                            val=(jlen,1)
                            aggdict[hsh] = val
                            outputstring += " " + patxt
                cnttotal+=1
                if (cnttotal % 10000) == 0:
                    print(".", end="", flush=True)

                if len(outputstring) >0:
                    jsonObject = {"id": j['id'], "text": outputstring.strip()}
                    outputfilefp.write(jsonObject)
        outputfilefp.close()
        print("\n")
    printwithtime("End writing corpus files")
    shutil.rmtree(outputindexdir)
    end = datetime.now()
    delta= end -start
    durstr="Duration in real time: " + str(delta)
    printwithtime(durstr)

    printwithtime("Finished")
    # fflush(stdout)
