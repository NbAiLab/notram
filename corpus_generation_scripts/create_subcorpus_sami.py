######################################################################
### Creates a sub-corpus  - In this example: sami
#####################################################################

import os, sys
import glob
from tqdm import tqdm
from pathlib import Path
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



def main(args):
    with open(args.json_file_list) as file:
        json_file_list = file.readlines()
        json_file_list = [line.rstrip() for line in json_file_list]

    with open(args.docid_list) as file:
        docid_list = file.readlines()
        docid_list = [line.rstrip() for line in docid_list]

    for myfile in tqdm(json_file_list): 
        with jsonlines.open(myfile) as reader:
            with jsonlines.open(args.output_file, mode='w') as writer:
                for n,obj in enumerate(reader):
                    if obj['id'] in docid_list:
                        writer.write(obj)
                        print(obj['id'])

    
    #Save is as jsonl
    #output_filename = os.path.join(args.output_folder, os.path.basename(args.input_file))
    #save_jsonl(data, output_filename)
    #logger.info(f'*** Finished processing file. Result has {len(data)} posts. Result is written to {os.path.join(args.output_folder, os.path.basename(args.input_file))}')
    #print(f'*** Finished processing file. Result has {len(data)} posts. Result is written to {os.path.join(args.output_folder, os.path.basename(args.input_file))}')

def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--json_file_list', required=True, help='List of json-files that should be processed')
    parser.add_argument('--output_file', required=True, help='Path to output file. Will replace existing file.')
    parser.add_argument('--docid_list',required=True, default="config.json", help='List of docids that should be included')
    parser.add_argument('--log_level',required=False, default="INFO", help='Set logging level to DEBUG to get a report on all decisions')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
   
    # Invoke logger globally
    logger= logging.getLogger()
    if args.log_level == "INFO":
       logger.setLevel(logging.INFO)
    elif args.log_level =="DEBUG":
       logger.setLevel(logging.DEBUG)
    else:
        print("Log level not accepted")
        exit()
    main(args)



