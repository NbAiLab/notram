####################################################################################
# Creates training corpus for vgd topic identification
# Output is an CSV file with topic, subtopic and text
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
from collections import Counter
import random 
from itertools import islice
import jsonlines

def main(args):
    print(f'Starting to read json')
    data = pd.DataFrame(columns=['id','topic', 'subtopic', 'text'])

    idx = 0
    with jsonlines.open(args.input_file) as reader:
        for post in reader:  
            text = ""
            topictext = post['forum'].split('.')
            topicnumber = int(post['id'].split('_')[2])
            user = post['user']

            paragraphs = post['paragraphs']
            for n,p in enumerate(paragraphs):
                if n != 0:
                    text = text + '<br />'
                text = text + str(p['text'])
                text = text.replace("\n","<br />").replace("\r","<br  />")
            
            text = text.strip()
            topic = topictext[0]
            subtopic = topictext[1].replace('-',' ')
            if user!="VG Nett" and user!="oyssol" and topicnumber == 0:
                idx += 1
                data = data.append({'id': idx, 'topic': topic, 'subtopic': subtopic, 'text': text}, ignore_index=True)

    print("Finished loading everything into Pandas")

    data.to_csv(args.output_file, index=False)


    print(f'A total number of {len(data)} is written to file {args.output_file}')


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

