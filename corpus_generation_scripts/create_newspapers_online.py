#!/usr/bin/env python3

import sys, glob, os, re, argparse
import pandas as pd
import xml.dom.minidom
import lxml.etree as ET
import codecs
import ftfy
from pathlib import Path
from tqdm import tqdm
import jsonlines

def main(args):
    all_articles = []
    files_with_errors = 0
    f = None    
    
    input_files = get_input_files(args.input_path)
    if args.language_reported:
        xml_files = [x for x in input_files if str(args.language_reported +'/') in str(x)]
    else:
        xml_files = input_files

    print (f'Processing {len(xml_files)} files')
    
    #Default parsing is iso-8859-1  works always but might not be correct
    #After evaluating - this is the safeste way to parse these files
    parser = ET.XMLParser(recover=True, encoding="iso-8859-1")
    #utfparser = ET.XMLParser(recover=True, encoding="utf-8")

    for f in tqdm(xml_files):
        basename = os.path.basename(f).replace(".xml","")
        with codecs.open(str(f), 'rb') as xmlfile:
            try:
                document = ET.parse(xmlfile, parser=parser)
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
            
        for n,d in enumerate(document.findall('body/div')):
            myarticle = {}
            myarticle['doc_type'] = args.doc_type
            myarticle['id'] = basename + "-"+str(n)
            myarticle['language_reported'] = str(args.language_reported)
            myarticle['paragraphs'] = [] 

            type = d.attrib['type']
            if type == "text":
                for id,paragraph in enumerate(list(d)):
                    if paragraph.text:
                        p = {}
                        p['paragraph_id'] = id
                        p['text'] = str(ftfy.fix_text(paragraph.text))
                        myarticle['paragraphs'].append(p)
       
            if len(myarticle['paragraphs']) > 0:
                all_articles.append(myarticle)
    
    if not f:
        print(f'No valid files found in {args.input_path}')
        sys.exit()

    with jsonlines.open(args.output_file, 'w') as writer:
        writer.write_all(all_articles)
    
    print("Finished parsing the articles.")
    
    #Print some statistics
    print(f'Saved file: {args.output_file}')
    print(f'Total number of files: {len(all_articles)}')
    print(f'Files with errors: {files_with_errors}')
    

def get_input_files(input_folder):
    return list(Path(input_folder).rglob('*.xml'))

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Processing the newspaper corpus published by Språkbanken. Output is an UTF-8 JSON lines")
    parser.add_argument('-i','--input_path', required=True, type=str, help='Input path')
    parser.add_argument('-o', '--output_file', required=True, type=str, help='Output file')
    parser.add_argument('--doc_type', required=True, type=str, help='Doc type')
    parser.add_argument('-l', '--language_reported', required=True, type=str, help='Language. nob, nno or . Folder names determine language.')

    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)





