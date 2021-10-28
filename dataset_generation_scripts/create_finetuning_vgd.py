####################################################################################
# Creates training corpus for vgd topic identification
# Output is an CSV file with topic, subtopic and text
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd
import numpy as np
from collections import Counter
import random 
from itertools import islice
import jsonlines
import re
from datasets import Dataset

def main(args):
    print(f'Starting to read json')
    data = pd.DataFrame(columns=['id','docid', 'topic', 'subtopic', 'title','text','firstanswer'])

    idx = 0
    with jsonlines.open(args.input_file) as reader:
        for post in reader:  
            
            topictext = post['forum'].split('.')
            topicnumber = int(post['id'].split('_')[2])
            docid = str(post['id'].split('_')[1])
            title = re.search(r'tittel/(.*?)/side', docid).group(1).replace("-"," ").capitalize()
            
            user = post['user']
            
            paragraphs = post['paragraphs']
            #text = ""
            #for n,p in enumerate(paragraphs):
            #    if n != 0:
            #        text = text + '<br />'
            #    text = text + str(p['text'])
            #    text = text.replace("\n","<br />").replace("\r","<br />")
        
            #text = text.replace("<br />","\n")
            #text = text.strip()
            text = ""
            for p in paragraphs:
                 text = text + str(p['text'])
                 text = text.replace("', '"," ")
                 text = text.replace("'","")
                 text = text.replace("[","")
                 text = text.replace("]","")

            text = " ".join(text.split())
            

            topic = topictext[0]
            subtopic = topictext[1].replace('-',' ')
            if user!="VG Nett" and user!="oyssol" and (topicnumber == 0 or topicnumber == 1):
                idx += 1
                if topicnumber == 0:
                    data = data.append({'id': idx, 'docid': docid, 'topic': topic, 'title': title, 'subtopic': subtopic, 'text': text, 'firstanswer': np.nan}, ignore_index=True)
                elif topicnumber == 1:
                    data.loc[data.docid == docid,"firstanswer"] = text
    print("Finished loading everything into Pandas")
    #breakpoint()
    data.dropna(subset=['firstanswer'], inplace=True)
    data = data[data.text != "[Slettet]"]
    data = data[data.firstanswer != "[Slettet]"]

    dataset = Dataset.from_pandas(data)
    dataset.save_to_disk(args.output_folder)
    data.to_csv(args.output_folder+"/vgd.csv", index=False)
    

    #Create GPT training set
    gpt_text = ""
    for index, row in data.iterrows():
        
        if "/kjaerlighetssorg/" in row['docid']:
            topic = "Kjærlighetssorg"
        elif "/fotball-premier-league/" in row['docid']:
            topic = "Premiere League"
        elif "/politikk-norsk/" in row['docid']:
            topic = "Norsk politikk"
        else:
            topic = "Ukjent"

        question = row['text']
        answer = row['firstanswer']
        
        #gpt_text += "<forum>"+topic+"</forum><post>"+question+"</post><svar>"+answer+"<svar>"+"\n"
        gpt_text += "<post>"+question+"</post><svar>"+answer+"</svar>"+"\n"
        with open(args.output_folder+"/gpt_file.txt", "w") as gpt_file:
            gpt_file.write(gpt_text)

    print(f'A total number of {len(data)} is written to file {args.output_folder}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, type=str, help='Input file')
    parser.add_argument('--output_folder', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)

