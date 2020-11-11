#Cleaning up newspaper xml corpus
# These are the unpacked files in the 3/ directory
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import xml.dom.minidom
import lxml.etree as ET
import codecs
import ftfy

def main(args):
    minimum_number_of_words_in_an_article = 1
    all_articles = ""
    valid_segment_count = 0
    total_article_count = 0
    files_with_errors = 0
    f = None    
    xmlpath = os.path.join(args.input_path,'3/??/',args.language,'*.xml')
    
    #Working
    #xmlpath = "data/rawfiles/3/so/nno/20080830-964624.xml"
    
    #Not working
    #xmlpath = "data/rawfiles/3/fi/nno/20110812-5698262.xml"
    #xmlpath = "data/rawfiles/3/na/nno/20090422-4277069.xml"
    
    parser = ET.XMLParser(recover=True, encoding="iso-8859-1")
    for f in glob.glob(xmlpath):
        #print(f'Processing {f}')
        content = ""
        with codecs.open(f, 'rb') as xmlfile:
            try:
                document = ET.parse(xmlfile, parser=parser)
            except ET.ParseError as e:
                print("Unable to parse file "+f)
                print(f'Error is: {str(e)}')
                files_with_errors += 1
                continue

        for d in document.findall('body/div'):
            total_article_count += 1
            type = d.attrib['type']
            if type == "text":
                for p in list(d):
                    content +=  "\n" + str(p.text)

            if type == "caption":
                for p in list(d):
                    content +=  "\n" + str(p.text)
            
            elif type == "ingress":
                content +=  "\n" + str(d.text)
            
            elif type == "title" and d.attrib['level'] == "1":
                content += "\n" + str(d.text)
            
            elif type == "title" and d.attrib['level'] == "2":
                for p in list(d):
                    content +=  "\n" + str(p.text)

        #All 
        articles = content.split('\n')

        for article in articles:
            if len(str(article).split()) >= minimum_number_of_words_in_an_article:
                valid_segment_count += 1
                all_articles += str(article).strip() + '\n'

    if not f:
        print(f'No valid files found in {xmlpath}')
        sys.exit()

    print("Finished parsing the articles. Cleaning up")

    #Get rid of all double linespaces and doublewhitespace
    for _ in [0,5]:
        all_articles = all_articles.replace("\n\n","\n")
        all_articles = all_articles.replace("  "," ")
    

    #The xml files is a mix of iso-8859-1 and utf-8. Ftfy fixes this for us
    all_articles = ftfy.fix_text(all_articles)
    
    print("Finished fixing the unicode errors")

    with open(args.output_file, 'w+', encoding="utf-8") as f:
        f.write(all_articles)
    
    #Print some statistics
    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {total_article_count}')
    print(f'Number of valid segments: {valid_segment_count}')
    print(f'Total number of files: {len(glob.glob(xmlpath))}')
    print(f'Files with errors: {files_with_errors}')
    
    #To count the number of word, we Split the file into lines to avoid memory issues
    all_articles_lines = all_articles.split("\n")
    del all_articles

    word_num = 0
    for l in all_articles_lines:
        word_line_num = len(l.split())
        word_num += word_line_num

    print(f'Number of words: {word_num}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_path', required=True, type=str, help='Input path')
    parser.add_argument('-o', '--output_file', required=True, type=str, help='Output file')
    parser.add_argument('-l', '--language', default='nob', type=str, help='Language. Two possible values: nob(default) or nno')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

