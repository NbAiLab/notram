####################################################################################
# Convert the MC4 to our json-format.
# This corpus is in ascii json format
# Output is an UTF-8 file with one document per line
####################################################################################

import requests
import ftfy, glob, argparse, os
import jsonlines
from tqdm import tqdm
from datetime import datetime
from slugify import slugify
import json

def main(args):
    #Create the new file. Overwrite if it exits
    f = open(args.output_file, "w+") 
    f.close()

    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        with jsonlines.open(args.input_file) as reader:
            for mc4post in tqdm(reader):
                written = 0
                myarticle = {}
                myarticle['doc_type'] = args.doc_type
                myarticle['id'] = args.doc_type+"_"+ args.language_reported+"_"+slugify(mc4post['url']) 
                myarticle['language_reported'] = args.language_reported
                myarticle['url'] = mc4post['url']
                myarticle['timestamp'] = mc4post['timestamp']
                myarticle['paragraphs'] = []
                myarticle['publish_date'] = datetime.strptime(mc4post['timestamp'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y%m%d')
                alltext = list(filter(bool, mc4post['text'].splitlines()))
                
                pid = 0
                for p in alltext:
                    paragraph = {}
                    text =  " ".join(p.split())
                    text = ftfy.fix_text(text)

                    paragraph['paragraph_id'] = pid
                    paragraph['text'] = text
                    
                    myarticle['paragraphs'].append(paragraph)
                    pid += 1
                   
                writer.write(myarticle)
                n += 1
                
    print(f'{n} posts are written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--language_reported', required=False, default="N/A", type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True, type=str, help='For instance government')
    parser.add_argument('-o', '--output_file', required=True, help='Output file name. Will overwrite it exists')
    parser.add_argument('-i', '--input_file', required=True, help='Input file name.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
#print(soup.prettify()) # print the parsed data of html
