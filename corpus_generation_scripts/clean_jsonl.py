######################################################################
### Cleans up jsonl files
### Needs config.json to be placed in output directory - also serves as documentation
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

def read_config(cfile):
    try:
        f = open(cfile,"r")
        config = json.load(f)
    except:
        print("Error. There has to be a valid config-file in the output directory")
        exit()

    return config

def load_jsonl(jsonl):
    #Read the json and get it into pandas
    with open(jsonl) as f:
        lines = f.read().splitlines()
    df_inter = pd.DataFrame(lines)
    df_inter.columns = ['json_element']
    
    #Decode into dictionary
    df_inter['json_element'].apply(json.loads)

    #Normalise
    metakeys = get_metakeys(jsonl)
    data = pd.json_normalize(df_inter['json_element'].apply(json.loads), record_path =['paragraphs'], meta=metakeys)

    return data

def get_metakeys(jsonl):
    #Read one line of the jsonlines file and close it
    firstfile = open(args.input_file, "r")
    firstline = firstfile.readline()
    firstfile.close()
    jsonline = json.loads(firstline)
    metakeys = list(jsonline.keys())
    metakeys.remove('paragraphs')
    
    return metakeys


def count_alphawords(text):
    #Counts the number of pure alphawords (at least two characters long) in a text string
    #Adds spaces before some characters, if not . and , would lead to non-alpha words
    pat = re.compile(r"([.,;()!:/])")
    text = pat.sub(" \\1 ", text)
    num = sum((w.isalpha() and len(w) >= 2) for w in text.split())
    return num

def count_words(text):
    #Counts the number of words (at least two characters long) in a text string
    #Adds spaces before some characters, if not . and , would lead to non-alpha words
    pat = re.compile(r"([.,;()!:/])")
    text = pat.sub(" \\1 ", text)
    num = len([word for word in text.split() if len(word)>=2])
    return num

def main(args):
    config = read_config(os.path.join(args.output_folder,"config.json"))
    data = load_jsonl(args.input_file)
    
    #Number of alpha words in paragraph
    print(f'Checking that min alpha words is at least {config["min_alphawords_paragraph"]}. Valid posts = {len(data)}')
    cond = data['text'].apply(lambda x: count_alphawords(x)) >= config['min_alphawords_paragraph']
    data = data[cond]
    print(f'Completed filtering min alpha words. Valid posts = {len(data)}')

    #Numbers of words in paragraph
    print(f'Checking that min number of words in a paragraph is at least {config["min_words_paragraph"]}. Valid posts = {len(data)}')
    cond = data['text'].apply(lambda x: count_words(x)) >= config['min_words_paragraph']
    data = data[cond]
    print(f'Completed filtering min words. Valid posts = {len(data)}')

    #metakeys = get_metakeys(args.input_file)

    print(f'Loaded the data with {len(data)} rows')

    
    
    breakpoint()
    


def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_folder', required=True, help='Path to output folder.')
    #parser.add_argument('--username_filler', default='@user', type=str, help='Username filler (ignored when replace_username option is false)')
    #parser.add_argument('--url_filler', default='http://domain.com', type=str, help='URL filler (ignored when replace_urls option is false)')
    #parser.add_argument('--email_filler', default='anonymous@domain.com', type=str, help='Email filler (ignored when replace_email option is false)')
    #parser.add_argument('--digibok', default='keep', type=str, help='Handling of digibok_ids. "keep", "remove" or "auto". Last option relies on other settings in script')
    #parser.add_argument('--min_alphawords', default=2, type=int, help='The minimum number of letter-only- words with a length of at least 2. Keeps empty lines.')
    #parser.add_argument('--max_words_in_section', required=False, default=1000, help='After reaching this maximum number of words, the next paragraph will be split into a new section.')

    #parser.add_argument('--num_logged_samples', default=10, type=int, help='Log first n samples to output')
    #add_bool_arg(parser, 'run_in_parallel', default=True, help='Run script in parallel')
    #add_bool_arg(parser, 'replace_usernames', default=False, help='Replace usernames with filler. Mainly for tweets')
    #add_bool_arg(parser, 'replace_urls', default=False, help='Replace URLs with filler')
    #add_bool_arg(parser, 'replace_email', default=True, help='Replace emails with filler')
    #add_bool_arg(parser, 'fix_unicode', default=True, help='Use ftfy to fix and standardise unicode. Converts it all to valid utf-8')
    #add_bool_arg(parser, 'asciify_emojis', default=False, help='Asciifyi emojis. On by default but mainly useful for social media')
    #add_bool_arg(parser, 'replace_multiple_usernames', default=False, help='Replace "@user @user" with "2 <username_filler>. Mainly for use on tweets"')
    #add_bool_arg(parser, 'standardize', default=True, help='Replace "Standardize text. Remove all control characters.')
    #add_bool_arg(parser, 'replace_multiple_urls', default=False, help='Replace "http://... http://.." with "2 <url_filler>". Mainly for use on tweets')
    #add_bool_arg(parser, 'remove_unicode_symbols', default=True, help='After preprocessing remove characters which belong to unicode category "So"')
    #add_bool_arg(parser, 'remove_accented_characters', default=False, help='Remove accents/asciify everything. Probably not recommended.')
    #add_bool_arg(parser, 'standardize_punctuation', default=True, help='Standardize (asciifyi) special punctuation')
    #add_bool_arg(parser, 'do_lower_case', default=False, help='Convert text to lower case')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)


