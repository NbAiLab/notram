####################################################################################
# Read an UTF8-encoded file with one article per line ##############################
# Produce a new file with: #########################################################
# * Line breaks after each sentence ################################################
# * Double line breaks after each article ##########################################
####################################################################################


import sys, glob, os, re, argparse
import pandas as pd

#Norwegian Spacy
import spacy
from spacy.lang.nb.examples import sentences 
nlp = spacy.load('nb_core_news_sm')
from pandarallel import pandarallel
import ftfy

# Initialization
pandarallel.initialize()

def main(args):

    #Parse paths
    full_paths = [os.path.join(os.getcwd(), path) for path in args.input]
    
    files = set()
    for path in full_paths:
        if os.path.isfile(path):
            files.add(path)
        else:
            files |= set(glob.glob(path + '/*.txt'))

    print('Prosessing the following files:')
    for f in files:
        print(f)

    #Read files
    all_articles = ""
    valid_article_count = 0
    valid_sentence_count = 0
    minimum_number_of_words_in_article = 3
    
    complete = pd.Series()
    content = pd.Series()

    for f in files:
        content = pd.read_csv(f, sep='\r', encoding='utf-8',squeeze=True, header=None)
        complete = pd.concat([complete, content], ignore_index=True)
    
    #Sentence segmentation
    print(f'Loaded all files. Starting sentence segmentation. There is a total of {len(complete)} articles to process.')

    #Deduplication
    if str(args.deduplicate) == 'True':
        print(f'Deduplicating. There are {len(complete)} articles before deduplication.')
        complete = complete.drop_duplicates(keep='first', inplace=False).reset_index(drop=True)
        print(f'There are {len(complete)} articles after deduplication.')
    else:
        print("Skipping deduplication")

    #Randonomisation
    if str(args.randomize) == 'True':
        print("Starting to randomizing all rows.")
        complete = complete.sample(frac=1).reset_index(drop=True)
        print("Finished randomizing.")
    else:
        print("Skipping randomisation")

    #Remove articles with less than X words
    complete = complete[~complete.str.count('\s+').lt(minimum_number_of_words_in_article)]
    print(f'There are {len(complete)} articles after removing all articles with less than {minimum_number_of_words_in_article} words.')
    
    print("Drop NaN");
    complete = complete.dropna()

    #Fix utf-8 errors
    print("Starting to fix utf-8 errors")
    complete = complete.parallel_apply(ftfy.fix_text)

    #Split articles into sentences
    print('Starting to split articles into sentence')
    
    
    complete = complete.parallel_apply(sentseq)

    all_articles = complete.str.cat(sep='\n')

    #Save
    with open(args.output_file, 'w+', encoding='utf-8') as f:
        f.write(all_articles)

    
    
    #Print some statistics
    word_count  = len(all_articles.split(' '))
    sent_count = len(all_articles.split('\n'))
    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {len(complete)}')
    print(f'Total number of sentences: {sent_count}')
    print(f'Total number of words: {word_count}')


def sentseq(text):
    section = nlp(text)
    article = ""
    for sentence in section.sents:
        article += str(sentence) + "\n"
    return article


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, nargs='+', help='Input file(s) or path to files. If path is provided, all files ending with *.txt will be parsed.')
    parser.add_argument('-o', '--output_file', required=True, help='Output file')
    parser.add_argument('-r', '--randomize', required=False, default='False', help='Randomizes all articles before segmentation. Default: False. Set to True/False')
    parser.add_argument('-d', '--deduplicate', required=False, default='False', help='Deduplicates all articles before sentence segmenation. Default: False. Set to True/False')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)




