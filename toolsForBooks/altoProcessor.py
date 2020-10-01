import argparse
import io
import os
import glob
import sys
import codecs
import subprocess
import time
import ftfy
import langid

from os import path
from xmlHandler import xmlHandler

import json

class altoProcessor:
    minimalNumberOfWordsInParagraph = 6
    currentUrn=""
    content = ""
    globalAntallOver98 = 0
    globalAntallOrd = 0
    globalSumWC = 0
    altoObjectDir=""
    rootNodeName = None
    handler = None
    publang={}
    totalNumberOfWords = 0
    outputfilePointers = {}
    infiles={}
    cleanContent=""
    paragraphs=[]
    docworksVersion=""
    abbyyVersion= ""
    detected_language=""

    def __init__(self, altoObjectDir,rootNodeName=None):
        self.altoObjectDir=altoObjectDir
        self.currentUrn=""
        if rootNodeName == None:
            self.rootNodeName = "alto"
        else:
            self.rootNodeName = rootNodeName
        self.content = ""
        self.globalSumWC = 0
        self.globalAntallOrd = 0
        self.handler = None
        self.globalAntallOver98 = 0
        self.minimalNumberOfWordsInParagraph = 6
        self.publang = {}
        self.outputfilePointers = {}
        self.totalNumberOfWords = 0
        self.infiles = {}
        self.cleanContent = ""
        self.paragraphs = []
        self.docworksVersion = ""
        self.abbyyVersion = ""
        self.detected_language = ""

    def __init__(self):
        self.altoObjectDir=""
        self.currentUrn = ""
        self.rootNodeName = "alto"
        self.content = ""
        self.globalSumWC = 0
        self.globalAntallOrd = 0
        self.handler = None
        self.globalAntallOver98 = 0
        self.minimalNumberOfWordsInParagraph = 6
        self.publang = {}
        self.outputfilePointers = {}
        self.totalNumberOfWords=0
        self.infiles = {}
        self.cleanContent = ""
        self.paragraphs = []
        self.docworksVersion = ""
        self.abbyyVersion = ""
        self.detected_language = ""

    def buildPublishedAndLanguageDict(self,dictfile):
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
                self.publang[urn]=(year,lang)

    def getPublishedYear(self,urn):
        result=self.publang.get(urn,None)
        if result == None:
            return "<unknown>"
        else:
            return result[0]

    def getLanguage(self,urn):
        result=self.publang.get(urn,None)
        if result == None:
            return "<unknown>"
        else:
            return result[1]


    def findTextInBlock(self,block):

        id=block.attrib['ID']
        
        textnodes = self.handler.findInSub(block, "TextLine/String")
        localstr = ""
        sumwc = 0
        antallOver98 = 0
        localwc = 0
        nowords=0
        for textnode in textnodes:
            #print(textnode.attrib['CONTENT'])
            if 'SUBS_TYPE' not in textnode.attrib:
                localstr += textnode.attrib['CONTENT'].strip()
                localwc = float(textnode.attrib['WC'].strip())
                sumwc += localwc
                self.totalNumberOfWords += 1

                localstr += " "
                nowords+=1
                if (localwc >= 0.98):
                    antallOver98 += 1
                    self.globalAntallOver98 += 1


            elif 'SUBS_TYPE' in textnode.attrib and textnode.attrib['SUBS_TYPE'].strip() == 'HypPart2':
                localstr += textnode.attrib['SUBS_CONTENT'].strip()
                localwc = float(textnode.attrib['WC'].strip())
                sumwc += localwc
                self.totalNumberOfWords += 1
                nowords += 1

                localstr += " "
                if (localwc >= 0.98):
                    antallOver98 += 1
                    self.globalAntallOver98 += 1

            elif 'SUBS_TYPE' in textnode.attrib and textnode.attrib['SUBS_TYPE'].strip() == 'HypPart1':
                localwc = float(textnode.attrib['WC'].strip())
                sumwc += localwc

                if (localwc >= 0.98):
                    antallOver98 += 1
                    self.globalAntallOver98 += 1


            if (len(localstr) >= self.minimalNumberOfWordsInParagraph):
                self.globalSumWC += localwc
                self.globalAntallOrd += 1


        #print(id,localstr,nowords)
        if (nowords >0):
            localstr = ftfy.fix_text(localstr)
            localstr=localstr.replace('\r', '').replace('\n', '').replace('\t', '')
            #print(id, localstr, nowords)
            localstr += "\n"
            self.content += localstr
            self.cleanContent += localstr
            self.paragraphs.append({"id": str(id), "confidence": str(round(sumwc / nowords, 2))})



    def findBookTextInTextBlocks(self,urn, bList):
        print(len(bList))

        for block in bList:
            print(block)
            searchString = "TextBlock[@ID='" + block + "']"
            res = self.handler.findAllNodes(searchString)
            print(len(res))
            res3 = []
            for i in res:
                res3 = self.handler.findInSub(i, "TextLine/String")
                localstr = ""
                sumwc = 0
                antallOver98 = 0


                for k in res3:
                    if 'SUBS_TYPE' not in k.attrib:
                        localstr += k.attrib['CONTENT'].strip().replace('\r', '').replace('\n', '')
                        localwc = float(k.attrib['WC'].strip())
                        sumwc += localwc
                        self.totalNumberOfWords += 1
                        if (len(res3) >= self.minimalNumberOfWordsInParagraph):
                            self.globalSumWC += localwc
                            self.globalAntallOrd += 1
                        localstr += " "
                        if (localwc >= 0.98):
                            antallOver98 += 1
                            self.globalAntallOver98 += 1


                    elif 'SUBS_TYPE' in k.attrib and k.attrib['SUBS_TYPE'].strip() == 'HypPart2':
                        localstr += k.attrib['SUBS_CONTENT'].strip().replace('\r', '').replace('\n', '')
                        localwc = float(k.attrib['WC'].strip())
                        sumwc += localwc
                        self.totalNumberOfWords += 1
                        if (len(res3) >= self.minimalNumberOfWordsInParagraph):
                            self.globalSumWC += localwc
                            self.globalAntallOrd += 1
                        localstr += " "
                        if (localwc >= 0.98):
                            antallOver98 += 1
                            self.globalAntallOver98 += 1

                    elif 'SUBS_TYPE' in k.attrib and k.attrib['SUBS_TYPE'].strip() == 'HypPart1':
                            localwc = float(k.attrib['WC'].strip())
                            sumwc += localwc
                            if (len(res3) >= self.minimalNumberOfWordsInParagraph):
                                self.globalSumWC += localwc
                                self.globalAntallOrd += 1
                            if (localwc >= 0.98):
                                antallOver98 += 1
                                self.globalAntallOver98 += 1

        if (len(blist) > 0):
            #self.content += urn + "_" + block + "_" + str(round(sumwc / len(res3), 2)) + "\n"
            localstr=ftfy.fix_text(localstr)
            localstr.replace('\r', '').replace('\n', '')
            self.content += localstr
            self.cleanContent += localstr
            self.paragraphs.append({"id":str(block),"confidence":str(round(sumwc / len(res3), 2))})
            print("id:" +str(block))
            print(localstr)
                #print("\n\n\n")

    def FindAllTextBlocksInBook(self,filen):
        blockList = []
        self.handler = xmlHandler(inputXmlFile=filen, rootNodeName="alto")
        if self.docworksVersion == "":
            docworksVersionNode = self.handler.findAllNodes("Description/OCRProcessing/preProcessingStep/processingSoftware/softwareVersion")
            self.docworksVersion = docworksVersionNode[0].text
        if self.abbyyVersion == "":
           abbyyVersionNode = self.handler.findAllNodes("Description/OCRProcessing/ocrProcessingStep/processingSoftware/softwareVersion")
           if abbyyVersionNode != []:
               self.abbyyVersion = abbyyVersionNode[0].text
           else:
               self.abbyyVersion = "none"
        #print (self.abbyyVersion +  "        " + self.docworksVersion)
        #self.handler.printElement(self.docworksVersion)
        #findInSub(self, node, match):
        MasterNodes=self.handler.findAllNodes("Layout/Page/PrintSpace")
        for masterNode in MasterNodes:
            blockResult = self.handler.findInSub(masterNode,"TextBlock")
            for block in blockResult:
                self.findTextInBlock(block)

        #blockResult = self.handler.findAllNodes("Layout/Page/PrintSpace/TextBlock")

        #self.findBookTextInTextBlocks(self.currentUrn, blockList)


    def initBook(self,altoObjectDir):
        self.paragraphs = []
        self.altoObjectDir = altoObjectDir
        self.content = ""
        self.cleanContent = ""
        self.globalSumWC = 0
        self.globalAntallOrd = 0
        self.handler = None
        self.globalAntallOver98 = 0
        self.totalNumberOfWords = 0
        self.docworksVersion = ""
        self.abbyyVersion = ""
        self.detected_language = ""
        self.infiles = sorted(glob.glob(self.altoObjectDir + '/digibok_[0-9]*_[0-9]*.xml'))
        if len(self.infiles) <= 1:
            return False
        #print(self.infiles[0])
        self.currentUrn = self.infiles[0].split('/')[-1].split('_')[0] + "_" + self.infiles[0].split('/')[-1].split('_')[1]
        return True

    def getBookUrn(self):
        return self.currentUrn

    def ReadBook(self):
        self.paragraphs = []
        self.content = ""
        self.cleanContent = ""
        self.globalSumWC = 0
        self.globalAntallOrd = 0
        self.handler = None
        self.globalAntallOver98 = 0
        self.docworksVersion = ""
        self.abbyyVersion = ""
        self.detected_language = ""
        #infiles = sorted(glob.glob(self.altoObjectDir + '/digibok_[0-9]*_[0-9]*.xml'))
        #currentUrn = infiles[0].split('/')[-1].split('_')[0] + "_" + infiles[0].split('/')[-1].split('_')[1]
        for i in self.infiles:
            self.FindAllTextBlocksInBook(i)
        #print(currentUrn + "_" + str(round(self.globalSumWC /self.globalAntallOrd, 2)))
        #print(self.content)

    def detectLanguage(self):
        res = str(langid.classify(self.cleanContent))
        #res = langid.classify("File with path to all books")
        #print(res)
        self.detected_language = res.split(",")[0].replace("(","").replace("'","")
        #print(self.detected_language)




    def printSingleFiles(self,outputdirin):
        year = self.getPublishedYear(self.getBookUrn())
        lang = self.getLanguage(self.getBookUrn())
        part2= self.currentUrn.split("_")[1]
        #print(part2)
        yearFromUrn=part2[0:4]
        monthFromUrn=part2[4:6]
        dayFromUrn = part2[6:8]
        outputdir=outputdirin + "/" + yearFromUrn + "/" + monthFromUrn + "/" + dayFromUrn
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
        filename= outputdir + "/"  + self.currentUrn +  ".txt"
        currfptr = open(filename, "w+")
        #currfptr.write(self.currentUrn + "_" + str(round(self.globalSumWC / self.globalAntallOrd, 2)) + "_" + lang + "\n")
        currfptr.write(self.content)
        currfptr.flush()
        currfptr.close()
        filenameMeta = outputdir + "/" + self.currentUrn + ".meta"
        currfptrMeta = open(filenameMeta, "w+")
        #detectedLanguage = detect(str(self.cleanContent))
        self.detectLanguage()
        if self.detected_language == 'no':
            self.detected_language = 'nob'
        if self.detected_language == 'nn':
            self.detected_language = 'nno'
        bookOcrWordconfidence=0
        if self.globalAntallOrd != 0:
            bookOcrWordconfidence=self.globalSumWC / self.globalAntallOrd
        averageNumberOfWordsPerParagraph = 0
        if (len(self.paragraphs) != 0):
            averageNumberOfWordsPerParagraph=self.totalNumberOfWords/len(self.paragraphs)
        percentageWords98confidence=0
        if self.totalNumberOfWords != 0:
            percentageWords98confidence=self.globalAntallOver98 / self.totalNumberOfWords

        jsonrecord={
            "urn": self.currentUrn,
            "publishYear":year,
            "language":str(lang),
            "languageDetected": self.detected_language,
            "docworksVersion":str(self.docworksVersion),
            "abbyyVersion":str( self.abbyyVersion ),
            "bookOcrWordconfidence":str(round(bookOcrWordconfidence, 2)),
            "percentageWords98confidence":str(round(percentageWords98confidence, 2)),
            "averageNumberOfWordsPerParagraph":str(round(averageNumberOfWordsPerParagraph,2)),
            "paragraphs":[]
        }
        jsonrecord['paragraphs']=self.paragraphs

        json.dump(jsonrecord, currfptrMeta)
        #print(jsonrecord)


        currfptrMeta.flush()
        currfptrMeta.close()

    def printTextInBook(self,outputdir):
        year = self.getPublishedYear(self.getBookUrn())
        lang = self.getLanguage(self.getBookUrn())
        #print(lang)
        #print(year)
        if year != "<unknown>":
            decade = year[0] + year[1] + year[2] + "0"
        else:
            decade = "unk"

        if lang != "nob" and lang != "non" :
            lang = "unk"

        decade_lang = decade + "_" + lang

        if (self.outputfilePointers.get(decade_lang,None) == None):
            filename= outputdir + "/"  + "book_" + decade_lang + ".txt"
            fptr = open(filename,"a+")
            self.outputfilePointers[decade_lang]=fptr

        currfptr = self.outputfilePointers.get(decade_lang,None)
        if self.globalAntallOrd != 0:
            currfptr.write(self.currentUrn + "_" + str(round(self.globalSumWC / self.globalAntallOrd, 2)) + "_" + lang + "\n")
        else:
            currfptr.write(self.currentUrn + "_" + str(0) + "_" + lang + "\n")
        currfptr.write(self.content)
        currfptr.flush()


    def closeAllFiles(self):
        for k in self.outputfilePointers:
            currfptr = self.outputfilePointers.get(k, None)
            if currfptr != None:
                currfptr.close()