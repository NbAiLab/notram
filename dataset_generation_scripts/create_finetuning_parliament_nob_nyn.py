####################################################################################
# Cleaning up parliament speech files
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
from collections import Counter
import random 
from itertools import islice

#Norwegian Spacy
import spacy
from spacy.lang.nb.examples import sentences
nlp = spacy.load('nb_core_news_sm')

def main(args):
    num_samples = 3000
    print(f'Starting to read csv-file')
    
    #Read the file
    df = pd.read_csv(args.input_file, encoding='utf-8', dtype='string')


    print(f'Finished reading csv-fil.\nNumber of valid articles: {len(df)}')
    
    
    langlist = []
    data = pd.DataFrame(columns=['date', 'language', 'text'])

    for index, row in df.iterrows():
        article = row['text']
        language = row['language']
        date = row['date']
        langlist.append(language)

        section = nlp(article)
        sentences = []
        for s in section.sents:
            sentences.append(s)
        
        #Draw a random sentence - disregard posts with only two sentences. Do not use the first sentence since this might have another language
        if len(sentences) > 2:
            rand_sentence = str(sentences[random.randint(1,len(sentences)-1)])
        else:
            rand_sentence = ""

       #Add to dataframe if more than 5 words and start with capital letter
        if len(rand_sentence.split()) > 5 and rand_sentence[0].isupper():
            data = data.append({'date': date, 'language': language, 'text': rand_sentence}, ignore_index=True)

        if index%1000 == 0:
            print(f'Processing row {index}')
    
    print("Finished loading everything into Pandas")

    nob = data['language'] == "nob"
    nno = data['language'] == "nno"

    nob_sample = data[nob].sample(n=num_samples, random_state=1)
    nno_sample = data[nno].sample(n=num_samples, random_state=1)
   
    final_data = pd.concat([nob_sample, nno_sample], ignore_index=True).sample(frac=1).reset_index(drop=True)

    print("Some stats:")
    l = Counter(langlist) 
    print(l.items())
    
    final_data.to_csv(args.output_file, index=False)


    print(f'A total number of {num_samples} for both bokmål and nynorsk is written to file {args.output_file}')



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

