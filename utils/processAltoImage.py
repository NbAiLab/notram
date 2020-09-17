# coding=utf-8
import sys
import os
import math
import numpy as np
import glob
import argparse
from os import path

from xmlHandler import xmlHandler


def findAllTextBlocks(filen,urn):
    blockList=[]
    handler = xmlHandler(inputXmlFile=filen, rootNodeName="alto")
    res = handler.findAllNodes("Layout/Page/PrintSpace/TextBlock")
    for block in res:
        blockList.append(block.attrib['ID'])
    findTextInTextBlocks(handler,urn,blockList)

def findTextInTextBlocks(hdl,urn,bList):
    for block in bList:
        searchString="Layout/Page/PrintSpace/TextBlock[@ID='" + block +"']"
        res = hdl.findAllNodes(searchString)
        for i in res:
            res3 = hdl.findInSub(i, "TextLine/String")
            localstr=""
            sumwc=0
            for k in res3:
                if 'SUBS_TYPE' in k.attrib and k.attrib['SUBS_TYPE'].strip() =='HypPart':
                    print("kkkkk")


                localstr+=k.attrib['CONTENT'].strip()
                localwc = float(k.attrib['WC'].strip())
                sumwc+=localwc
                localstr += " "
            if (len(res3)>0):
                print(urn + " " + block + " " + " " + str(round(sumwc/len(res3),2)) )
                print(localstr)
                print("\n")


def main(inputDir):
    infiles = sorted(glob.glob(inputDir + '/digibok_[0-9]*_[0-9]*.xml'))
    print(infiles)
    sys.exit()
    currentUrn=infiles[0].split('/')[-1].split('.')[0]

    for i in infiles:
        findAllTextBlocks(i,currentUrn)




def getStringFromTextblock(hdl,composedBlockNode,indexNo, outputDir):
    res = hdl.findAllNodes("Description/sourceImageInformation/fileName")
    if len(res) == 0:
        print("Filename not found")

    adjustedBasename = os.path.splitext(os.path.basename(res[0].text))[0]
    res=hdl.findInSub(composedBlockNode,"TextBlock/TextLine")
    str=""

    for i in res:
        res3 = hdl.findInSub(i, "String")
        for k in res3:
            str+=k.attrib['CONTENT'].rstrip()
            str += " "

    outputFile=''.join((outputDir,"/",adjustedBasename, "_", indexNo, ".txt"))
    with open(outputFile, "w") as f:
        f.write(str)
    f.close()
    return str


if __name__ == '__main__':
    main(sys.argv[1])
    #findAllTextBlocks(sys.argv[1])
    #main(sys.argv[1],sys.argv[2])
