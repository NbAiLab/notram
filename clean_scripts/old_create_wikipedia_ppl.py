####################################################################################
# Cleaning up Norwegian Wikipedia
# Output is an UTF-8 file with one paragraph per line and double line breaks between articles
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd

def main(args):
    minimum_number_of_words_in_an_article = 1
    all_articles = ""
    valid_paragraph_count = 0

    #Read the file
    print('Starting to read json-file...')
    df = pd.read_json(args.input_file)
    print(f'Finished loading {len(df)} articles.')
    

    print('Starting to parse json file...')
    
    for index, row in df.iterrows():
        #There are some encoded line breaks in here that seems to confuse Spacey. Replace them
        #article = df['text'].str.replace("\n"," ")
        wikiarticle = row['text'].replace("\n\n","<p>")
        wikiarticle = wikiarticle.replace("\n"," ")
        wikiarticle = wikiarticle.replace("<p>","\n").strip().strip('\n\r')
        
        #All 
        articles = wikiarticle.split('\n')

        for article in articles:
            if len(str(article).split()) >= minimum_number_of_words_in_an_article:
                valid_paragraph_count += 1
                all_articles += str(article) + '\n'
        
        #Add an extra paragraph at the end of an article
        all_articles += '\n'
        #Uncomment to run a test on part of the dataset
        #if index > 100:
        #    break
    
    #import pdb; pdb.set_trace() 
    
    with open(args.output_file, 'w+', encoding="utf-8") as f:
        f.write(all_articles)
    
    #Print some statistics
    word_count = len(re.findall(r'\w+', all_articles))

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {index}')
    print(f'Number of valid paragraphs: {valid_paragraph_count}')
    print(f'Number of words: {word_count}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)


