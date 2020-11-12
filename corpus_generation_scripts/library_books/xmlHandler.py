import argparse
import io
import os
import xml.etree.ElementTree as ET
import xml.etree as ETtree
from xml.dom import minidom
#from StringIO import StringIO


# import lxml.etree as etree

import sys
import codecs


class xmlHandler:
    Root = ET.Element("data")
    Tree = ET.ElementTree(Root)
    cnt = 0
    kind = 'a'
    outfile = ""

    def __init__(self, inputXmlFile=None, rootNodeName=None):
        if (inputXmlFile == None) and (rootNodeName == None):
            self.Root = ET.Element("data")
            self.Root.tag = "data"
            self.Tree = ET.ElementTree(self.Root)
            self.Tree.tag = "data"
        elif (inputXmlFile == None) and (rootNodeName != None):
            self.Root = ET.Element(rootNodeName)
            self.Root.tag = rootNodeName
            self.Tree = ET.ElementTree(self.Root)
            self.Tree.tag = rootNodeName
        else:
            self.Tree = ET.parse(inputXmlFile)
            self.Root = self.Tree.getroot()

    # def openWithIgnoreNameSpaces(self, inputXmlFile):
    #     it = ET.iterparse(StringIO(xml))
    #     for _, el in it:
    #         if '}' in el.tag:
    #             el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
    #     self.Root = it.root


    def replace_non_ascii(self, text):
        return ''.join([i if ord(i) < 128 else ' ' for i in text])

    def getRootNode(self):
        return self.Root

    def fromString(self,xmlstring,rootNodeName):
        self.Tree = ET.fromstring(xmlstring)

        self.Root = ET.Element(rootNodeName)
        self.Root.tag = rootNodeName


    def printTreeToFile1(self, ofilename):
        self.Tree.write(ofilename)

    def printElement(self, elem):
        print ("Text:" + str(elem.text))
        print("Tag:" + elem.tag)
        print("Attrib:" + str(elem.attrib))

    def printTree1(self):
        for elem in self.Root:
            self.printElement(elem)
            assert isinstance(elem, object)
            for subelem in elem:
                assert isinstance(subelem, object)
                self.printElement(self, subelem)

    def printElementNodeToFile(self, level, elem):
        antall = level * 3
        cnt = 0
        str1 = ""
        filler = ""

        while cnt < antall:
            str1 += " "
            filler += " "
            cnt += 1
        #print("AA" + elem.text.encode('utf-8').strip() + "bb")
        if  elem.text is None:
            strElemText = ""
        elif elem.text == "None":
            strElemText = ""
        else:
            strElemText = str(elem.text).strip().strip('\t')
        strAttribText = ""
        if str(elem.attrib) == "{}":
            strAttribText = ""
        else:
            strAttribText+=" "
            dictlen=len(elem.attrib)
            cnt=1
            for k in elem.attrib.keys():
                res = k + "=\"" + str(elem.attrib.get(k)) +"\""
                strAttribText+=res
                if (cnt != dictlen):
                    strAttribText+=" "
                cnt+=1


        if elem is not None:
            filler += " "

            if str(elem.attrib) == "{}":
                str1 += "<" + elem.tag + ">" + '\n' + filler + strElemText
            else:
                str1 += "<" + elem.tag + " " + strAttribText + ">" + '\n' + filler + strElemText
        else:
            if str(elem.attrib) == "{}":
                str1 += "<" + elem.tag + ">" + strElemText
            else:
                str1 += "<" + elem.tag + " " + strAttribText + ">" + strElemText

        if level > 0:
            self.outfile.write("\n")
        self.outfile.write(str1.strip('\n').strip('\t'))
        rightLevel = True
        for subelem in elem:
            rightLevel = False
            self.printElementNodeToFile(level + 1, subelem)
        str1 = ""
        cnt = 0
        while cnt < antall:
            str1 += " "
            cnt += 1
        if (rightLevel == True):
            str1 = "</" + elem.tag + ">"
        else:
            self.outfile.write("\n")
            str1 += "</" + elem.tag + ">"
        self.outfile.write(str1.strip('\n'))

    def printElementNode(self, level, elem):

        antall = level * 3
        cnt = 0
        str1 = ""
        filler = ""
        while cnt < antall:
            str1 += " "
            cnt += 1
        if str(elem.text) == "None":
            strElemText = ""
        else:
            strElemText = str(elem.text)
        strAttribText = ""
        if str(elem.attrib) == "{}":
            strAttribText = ""
        else:
            strAttribText += " "
            dictlen = len(elem.attrib)
            cnt = 1
            for k in elem.attrib.keys():
                res = k + "=\"" + str(elem.attrib.get(k)) +"\""
                strAttribText += res
                if (cnt != dictlen):
                    strAttribText += " "
                cnt += 1

        if elem:
            filler += " "

            if str(elem.attrib) == "{}":
                str1 += "<" + elem.tag + ">" + '\n' + filler + strElemText
            else:
                str1 += "<" + elem.tag + " " + strAttribText + ">" + '\n' + filler + strElemText
        else:
            if str(elem.attrib) == "{}":
                str1 += "<" + elem.tag + ">" + strElemText
            else:
                str1 += "<" + elem.tag + " " + strAttribText + ">" + strElemText
        if level > 0:
            print("\n")
        print(str1)
        rightLevel = True
        for subelem in elem:
            rightLevel = False
            self.printElementNode(level + 1, subelem)
        str1 = ""
        cnt = 0
        while cnt < antall:
            str1+=" "
            cnt += 1
        if rightLevel:
            str1="</" + elem.tag + ">"
        else:
            print("\n")
            str1+= "</" + elem.tag + ">"
        print(str1.strip('\n'))

    def printTree(self):
        self.printElementNode(0, self.Root)

    def printTreeToFile(self, outfileName):
        self.outfile = open(outfileName, "w")
        self.printElementNodeToFile(0, self.Root)
        self.outfile.close()

    def addNode(self, node):
        self.Root.append(node)

    def addSubNode(self, node, node2):
        node.append(node2)

    def prettyPrint2(self, fileName):
        xmlstr = minidom.parseString(ET.tostring(self.Root)).toprettyxml(indent=" ")
        with open(fileName, "w") as f:
            f.write(xmlstr)
        f.close()

    def prettyPrint(self, fileName):

        reparsed = minidom.parseString(ET.tostring(self.Root))
        pprint = ('\n'.join([line for line in reparsed.toprettyxml(indent=' ' * 2).split('\n') if line.strip(' ')]))
        if os.path.isfile(fileName) and os.path.getsize(fileName) > 0:
            os.remove(fileName)
        with open(fileName, "w") as f:
            f.write(self.replace_non_ascii(pprint))
        f.close()

    def makeElement(self, tag, text=None, attr=None):
        if (attr != None):
            item = ET.Element(tag, attr)
        else:
            item = ET.Element(tag)
        item.tag = tag
        if (text != None):
            item.text = text
        return item

    def addSubElement(self, node, itemType, text=None, attr=None):
        itemSub = ET.SubElement(node, itemType)
        itemSub.tag = itemType
        if (attr != None):
            itemSub.attrib = attr
        if (text != None):
            itemSub.text = text
        return node

    def printAllMatchingNodes(self, match):
        for elem in self.Root:
            for subelem in elem.findall(match):
                print(subelem.attrib)

    def findAllNodes2(self, match):
        results = []
        for elem in self.Root:
            self.printElement(elem)
            for subelem in elem.findall(match):
                results.append(subelem)
        return results

    def findAllNodes(self, match):
        results = []
        for subelem in self.Tree.findall(match):
            results.append(subelem)
        return results

    def findInSub(self,node,match):
        results = []
        for subelem in node.findall(match):
            results.append(subelem)
        return results

    def printCnt(self):
        print(self.cnt)

    @staticmethod
    def setKind(fullName):
        print("setting kind:" + fullName)
        xmlHandler.kind = fullName
