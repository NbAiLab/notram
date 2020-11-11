####################################################################################
# Cleaning up newspaper xml corpus
# These are the unpacked files in the 3/ directory
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import xml.dom.minidom
import lxml.etree as ET
import codecs
import ftfy
from pathlib import Path
from tqdm import tqdm

def main(args):
    minimum_number_of_words_in_an_article = 1
    all_articles = ""
    valid_segment_count = 0
    total_article_count = 0
    files_with_errors = 0
    f = None    
    
    input_files = get_input_files(args.input_path)
    if args.language:
        xml_files = [x for x in input_files if str(args.language +'/') in str(x)]
    else:
        xml_files = input_files

    print (f'Processing {len(xml_files)} files')
    
    parser = ET.XMLParser(recover=True, encoding="iso-8859-1")
    utfparser = ET.XMLParser(recover=True, encoding="utf-8")

    for f in tqdm(xml_files):
        #print(f'Processing {f}')
        content = ""
        with codecs.open(str(f), 'rb') as xmlfile:
            try:
                #Default parsing is iso-8859-1  works always but might not be correct
                document = ET.parse(xmlfile, parser=parser)
                #If in utf-8 parse with utf-8 instead
                if document.docinfo.encoding == "utf-8":
                    document = ET.parse(xmlfile, parser=utfparser)
                    print("utf-8")
                else:
                    print("iso-8869")

            except ET.ParseError as e:
                print(f'Unable to parse file {f}')
                print(f'Error: {str(e)}')
                files_with_errors += 1
                continue
            except Exception as e:
                print(f'Unable to parse file {f}')
                print(f'Error: {str(e)}')
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
        
        #Add an extra line break after each article
        all_articles += '\n'
    
    if not f:
        print(f'No valid files found in {args.input_path}')
        sys.exit()

    print("Finished parsing the articles. Cleaning up")

    #Get rid of double whitespace
    all_articles = " ".join(all_articles.split(' '))
    

    #The xml files is a mix of iso-8859-1 and utf-8. Ftfy fixes this for us
    all_articles = ftfy.fix_text(all_articles)
    
    print("Finished fixing the unicode errors")

    with open(args.output_file, 'w+', encoding="utf-8") as f:
        f.write(all_articles)
    
    #Print some statistics
    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {total_article_count}')
    print(f'Number of valid segments: {valid_segment_count}')
    print(f'Total number of files: {len(xmlfiles)}')
    print(f'Files with errors: {files_with_errors}')
    
    #To count the number of word, we Split the file into lines to avoid memory issues
    all_articles_lines = all_articles.split("\n")
    del all_articles

    word_num = 0
    for l in all_articles_lines:
        word_line_num = len(l.split())
        word_num += word_line_num

    print(f'Number of words: {word_num}')

def get_input_files(input_folder):
    #return glob.glob(os.path.join(input_folder, '*.txt'))
    return list(Path(input_folder).rglob('*.xml'))

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_path', required=True, type=str, help='Input path')
    parser.add_argument('-o', '--output_file', required=True, type=str, help='Output file')
    parser.add_argument('-l', '--language', default=None, type=str, help='Language. Default is all languages. Two possible values: nob or nno. Determined by file name')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)





