# coding=utf-8
import sys
import os
import math
import numpy as np
import glob
import argparse
from os import path

from xmlHandler import xmlHandler

content=""
globalAntallOver98=0
globalAntallOrd=0

def findAllTextBlocks(filen,urn):
    blockList=[]
    handler = xmlHandler(inputXmlFile=filen, rootNodeName="alto")
    res = handler.findAllNodes("Layout/Page/PrintSpace/TextBlock")
    for block in res:
        blockList.append(block.attrib['ID'])
    findTextInTextBlocks(handler,urn,blockList)

def findTextInTextBlocks(hdl,urn,bList):
    global globalAntallOrd
    global content
    global globalAntallOver98

    for block in bList:
        searchString="Layout/Page/PrintSpace/TextBlock[@ID='" + block +"']"
        res = hdl.findAllNodes(searchString)
        for i in res:
            res3 = hdl.findInSub(i, "TextLine/String")
            localstr=""
            sumwc=0
            antallOver98=0
            antallOver95 = 0
            for k in res3:
                if 'SUBS_TYPE' not in k.attrib:
                    localstr += k.attrib['CONTENT'].strip()
                    localwc = float(k.attrib['WC'].strip())
                    sumwc += localwc
                    localstr += " "
                    if (localwc >= 0.98):
                        antallOver98 += 1
                        globalAntallOver98 += 1
                    if (localwc >= 0.95):
                        antallOver95 += 1
                    globalAntallOrd += 1

                elif 'SUBS_TYPE' in k.attrib and k.attrib['SUBS_TYPE'].strip() =='HypPart2':
                    localstr += k.attrib['SUBS_CONTENT'].strip()
                    localwc = float(k.attrib['WC'].strip())
                    sumwc += localwc
                    localstr += " "
                    if (localwc >= 0.98):
                        antallOver98 += 1
                        globalAntallOver98 += 1
                    if (localwc >= 0.95):
                        antallOver95 += 1
                    globalAntallOrd += 1
                elif 'SUBS_TYPE' in k.attrib and k.attrib['SUBS_TYPE'].strip() == 'HypPart1':
                    localwc = float(k.attrib['WC'].strip())
                    sumwc += localwc
                    if (localwc >= 0.98):
                        antallOver98 += 1
                        globalAntallOver98 += 1
                    if (localwc >= 0.95):
                        antallOver95 += 1
                    globalAntallOrd += 1

            if (len(res3)>0):
                content+=urn + "_" + block + "_" + str(round(antallOver98/len(res3),2)) + "\n"
                content+=localstr + "\n"
                #globalAntallOrd += 1
                #print(urn + "_" + block + "_" + str(round(antallOver98/len(res3),2)) )
                #print(localstr)
                #print("\n")


def main(inputDir):

    infiles = sorted(glob.glob(inputDir + '/digibok_[0-9]*_[0-9]*.xml'))
    currentUrn=infiles[0].split('/')[-1].split('_')[0] + "_" + infiles[0].split('/')[-1].split('_')[1]
    for i in infiles:
        findAllTextBlocks(i,currentUrn)
    print(currentUrn+ "_"+ str(round(globalAntallOver98/globalAntallOrd,2)))
    print(content)


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
