import argparse
import glob
from os import path
import string
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('Inputfile', help='Inn fil')
    args = parser.parse_args()
    fileptr = open(args.Inputfile, "r")
    cnt=0
    linecnt=0
    watch=276875
    printset = set(string.printable)
    for line in fileptr:
        linecnt+=1
        cnt=0
        for ch in line:
            val = ord(ch)
            if (ord(ch)<= 31) and (val!= 10):
                print("Not printable: " + str(linecnt) + ":" + str(cnt) + " " + str(ch) + " " + str(ord(ch)))
            isprintable = set(str(ch)).issubset(printset)
            if (isprintable == True):
                J=1
                #print("Printable: " +str(cnt) + " " + str(ch))
            elif ch in "æøåÆØÅé":
                J=1
                #print("Printable: " + str(cnt) + " " + str(ch))
            else:
                if (linecnt > watch-10) and (linecnt < watch+10 ):
                    print("Not printable: " +str(linecnt) + ":" +str(cnt) + " " + str(ch) + " " + str(ord(ch)) )
            cnt+=1
