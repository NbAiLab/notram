#!/usr/bin/env python3

####################################################################################
# Script is not in use, since this is no longer in the main corpus
# Cleaning up parliament speech files
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd

def main(args):
    minimum_number_of_words_in_an_article = 1
    all_articles = ""
    valid_article_count = 0

    #Read the file
    df = pd.read_csv(args.input_file, encoding='utf-8', dtype='string')

    for index, row in df.iterrows():
        article = row['text']

        if len(str(article).split()) >= minimum_number_of_words_in_an_article:
            valid_article_count += 1
            all_articles += str(article) + '\n'

        #Uncomment to run a test on part of the dataset
        #if index > 100:
        #    break
    
    with open(args.output_file, 'w+', encoding="utf-8") as f:
        f.write(all_articles)

    #Print some statistics
    word_count = len(re.findall(r'\w+', all_articles))

    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {index}')
    print(f'Number of valid articles: {valid_article_count}')
    print(f'Number of words: {word_count}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Fill in! Output is an UTF-8 JSON lines")
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

