######################################################################
### Deduplication
#####################################################################

import os, sys
import glob
from tqdm import tqdm
from pathlib import Path
from utils.textCleaner import cleanTextBlock
from utils.misc import ArgParseDefault, add_bool_arg
import jsonlines
import json
import pandas as pd
import re
from slugify import slugify
import hashlib
import ftfy
from datetime import datetime
import logging
import psutil

def load_jsonl(jsonl):
    #Read the json and get it into pandas
    with open(jsonl) as f:
        lines = f.read().splitlines()
    
    if len(lines):
        df_inter = pd.DataFrame(lines)
        df_inter.columns = ['json_element']
    
    
        #Decode into dictionary
        df_inter['json_element'].apply(json.loads)

        #Normalise
        metakeys = ['id','doc_type','publish_year','doc_length']
        data = pd.json_normalize(df_inter['json_element'].apply(json.loads), record_path =['paragraphs'], meta=metakeys, errors='ignore')

    else:
        data = pd.DataFrame(columns=['id','doc_type','publish_year','doc_length','paragraph_id','text','hash'])

    return data



def main(args):
    filelist = glob.glob(args.input_folder+'*.jsonl')
    
    for i,f in enumerate(filelist):
        new = load_jsonl(f)
        if i == 0:
            data = new
        else:
            data = pd.concat([data, new])

        print(f'Loaded {f} with {len(new)} rows. Totally {len(data)} rows. Memory usage: {psutil.virtual_memory()[2]}%')





def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_folder', required=True, help='Path to input file.')
    parser.add_argument('--output_folder', required=False, help='Path to output folder.')
    parser.add_argument('--config_file',required=False, default="config.json", help='Needs to be placed in output folder. Overrides the default config.json')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)



