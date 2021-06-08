####################################################################################
# Cleaning up Norwegian Wikipedia
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import jsonlines
import ftfy

def main(args):
    all_articles = []
    valid_article_count = 0

    #Read the file
    print('Starting to read json-file...')
    df = pd.read_json(args.input_file)
    print(f'Finished loading {len(df)} articles.')
    
    #df = df[0:100]
    print('Starting to parse json file...')
    
    for index, row in df.iterrows():
        #There are some encoded line breaks in here that seems to confuse Spacey. Replace them
        wikiarticle = row['text'].replace("\n\n","<p>")
        wikiarticle = wikiarticle.replace("\n"," ")
        wikiarticle = wikiarticle.replace("<p>","\n").strip().strip('\n\r')
        
        #All 
        
        myarticle = {}
        myarticle['doc_type'] = str(args.doc_type)
        myarticle['id'] = index
        myarticle['language_reported'] = str(args.language_reported)
        myarticle['paragraphs'] = [] 
        
        for id,paragraph in enumerate(wikiarticle.split('\n')):
            p = {}
            p['paragraph_id'] = id
            p['text'] = str(ftfy.fix_text(paragraph))
            myarticle['paragraphs'].append(p)

        valid_article_count += 1
        all_articles.append(myarticle)

    with jsonlines.open(args.output_file, 'w') as writer:
        writer.write_all(all_articles)


    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {index+1}')
    print(f'Number of valid articles: {valid_article_count}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--language_reported', required=True, type=str, help='Language reported')
    parser.add_argument('--doc_type', required=True, type=str, help='Doc type')
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

