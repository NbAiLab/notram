####################################################################################
# Convert vgdebatt to jsonl.
# This corpus is in json format
# Output is a jsonl  UTF-8 file with one post per line
####################################################################################

from bs4 import BeautifulSoup
import requests
import ftfy, glob, argparse, os
import jsonlines
from tqdm import tqdm
from datetime import datetime

def main(args):
    #Create the new file. Overwrite if it exits
    f = open(args.output_file, "w+") 
    f.close()

    #Get a list of documents in the folder
    filelist = glob.glob(args.input_folder+'/*.jsonl', recursive=True)
    
    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        for f in tqdm(filelist):
            print(f'Processing {f}')
            with jsonlines.open(f) as reader:
                for post in reader:
                    try:
                        written = 0
                        myarticle = {}
                        myarticle['doc_type'] = args.doc_type
                        myarticle['id'] = args.doc_type+"_"+ str(post['id']) 
                        myarticle['user'] = str(post['user']) 

                        myarticle['language_reported'] = args.language_reported
                        myarticle['paragraphs'] = []
                        myarticle['publish_date'] = str(post['publish_date'])
                        myarticle['post_time'] = str(post['post_time'])
                        myarticle['url'] = str(post['url'])
                        myarticle['forum'] = str(post['forum'])

                        for p in post['paragraphs']:
                            paragraph = {}
                            paragraph['paragraph_id'] = p['paragraph_id']
                            paragraph['text'] = p['text'].strip()
                            
                            myarticle['paragraphs'].append(paragraph)
                           
                        writer.write(myarticle)
                        n += 1
                    except:
                        print("****Error processing this post:")
                        print(post)

    print(f'{n} posts from {len(filelist)} files are written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()    
    parser.add_argument('--language_reported', required=False, default="N/A", type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True, type=str, help='For instance tweet')
    parser.add_argument('-o', '--output_file', required=True, help='Output file name. Will overwrite it exists')
    parser.add_argument('-i', '--input_folder', required=True, help='Input folder. Will read all files in folder')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
#print(soup.prettify()) # print the parsed data of html
