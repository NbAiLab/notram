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
from slugify import slugify
import hashlib
import ftfy
from datetime import datetime
import logging

# Invoke logger globally
console = logging.StreamHandler() 
console.setLevel(logging.DEBUG) 
logging.getLogger('').addHandler(console) 
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# compile regexes
username_regex = re.compile(r'(^|[^@\w])@(\w{1,15})\b')
url_regex = re.compile(r'((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))')
email_regex = re.compile(r'[\w\.-]+@[\w\.-]+')
control_char_regex = re.compile(r'[\r\n\t]+')


def read_config(cfile):
    try:
        f = open(cfile,"r")
        config = json.load(f)
    except:
        logger.info("Error. There has to be a valid config-file in the output directory")
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
    metakeys = get_metakeys(lines)
    data = pd.json_normalize(df_inter['json_element'].apply(json.loads), record_path =['paragraphs'], meta=metakeys)

    return data

def save_jsonl(data, filename):
    colnames = list(data.columns)
    colnames = [c for c in colnames if not c.startswith('para') and not c.startswith('tmp') and not c.startswith('text')]

    data.groupby(colnames, as_index=False).apply(lambda x: x[['paragraph_id','text']].to_dict('r')).rename(columns={None:'paragraphs'}).to_json(filename,orient='records',lines=True)

    logger.info(f'Saved jsonl as "{filename}"')

def get_metakeys(lines):
    allkeys = set()
    for l in lines:
        jsonline = json.loads(l)
        allkeys = allkeys.union(set(jsonline.keys()))
    metakeys = list(allkeys)
    metakeys.remove("paragraphs")
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

def max_word_length(text):
    #Return the max word length in a text snippet
    wordlist = text.split()
    ##Remove all links from the wordlist
    wordlist = [x for x in wordlist if 'http' not in x and '/' not in x and '-' not in x]
    
    if len(wordlist):
        max_length = len(max(wordlist, key=len))
    else:
        max_length = 0
    
    return max_length

def get_hash(text):
    slug = slugify(text)
    result = hashlib.md5(slug.encode())
    return result.hexdigest()

def normalise_unicode(text):
    input_text = text
    text = text.strip()
    text = " ".join(text.split())
    text = ftfy.fix_text(text)
   
    if input_text != text:
        logger.info(f'Changed "{input_text}" -> "{text}"')

    return text

def truncate_last_valid_sentence(text):
    triple_val = text.rfind("tml")+2
    double_val = max(text.rfind("=P"),text.rfind("=p"), text.rfind(":p"), text.rfind(":P"), text.rfind(";D"), text.rfind(":D"), text.rfind(";/"))+1
    last_val = max(triple_val,double_val, text.rfind("."),text.rfind(";"),text.rfind(":"), text.rfind("?"), text.rfind(")"), text.rfind("!"), text.rfind("*"), text.rfind("\""), text.rfind("\'")) + 1
    
    if last_val <=  2:
        last_val = 0
    
    if last_val != len(text):
        logger.info(f'Changed "{text}" -> "{text[0:last_val]}"')
    
    return text[0:last_val]

def replace_usernames_tweets(text, filler='@peregil'):
    # replace other user handles by filler
    input_text = text
    text = re.sub(username_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split())
    
    if input_text != text:
        logger.info(f'Changed "{input_text}" -> {text}"')

    return text

def replace_urls(text, filler='http://url.no'):
    input_text = text
    # <url> is a marker used internally. use filler instead
    text = text.replace('<url>', filler)
    # replace other urls by filler
    text = re.sub(url_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split()) 
    
    if input_text != text:
        logger.info(f'Changed "{input_text}" -> {text}"')

    return text

def replace_email_addresses(text, filler='email@email.no'):
    input_text = text
    text = re.sub(email_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split()) 
    
    if input_text != text:
        logger.info(f'Changed "{input_text}" -> {text}"')

    return text

def main(args):
    pd.set_option("display.max_rows", None)
    
    #Invoke logging
    log_name = os.path.basename(args.input_file).replace(".jsonl",".log")
    logging.basicConfig(filename=os.path.join(args.output_folder,log_name), format='%(asctime)s %(message)s', filemode='w')

    config = read_config(os.path.join(args.output_folder,args.config_file))
    data = load_jsonl(args.input_file)
   
    logger.info(f'***  Data loaded. {len(data)} posts')
   
    #Create columns if they do not exist
    if 'publish_date' not in data:
        data['publish_date'] = datetime.today().strftime('%Y%m%d')
    
    if 'ocr_date' not in data:
        data['ocr_date'] = datetime.today().strftime('%Y%m%d')
    
    if 'document_word_confidence' not in data:
        data['document_word_confidence'] = 1.0
    
    if 'confidence' not in data:
        data['confidence'] = 1.0
 
    #Fix unicode
    if config['normalise_unicode']:
        data['text'] = data['text'].apply(normalise_unicode)
    logger.info(f'***  Normalised unicode. Removed double spaces. Trimmed string.')

    #Truncate last valid sentence in paragraph
    if config['truncate_last_valid_sentence']:
        data['text'] = data['text'].apply(truncate_last_valid_sentence)
   
    #Delete paragraph where the max word length is too long. This indicate OCR errors
    cond = data['text'].apply(lambda x: max_word_length(x)) <= config['max_word_length_paragraph']
    logger.info(f'\n\n*** The following text was deleted because some of the words were too long:\n {data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering out pragraphs with too long words. Valid posts = {len(data)}')
    
    #Add hash
    data['hash'] = data['text'].apply(lambda x: get_hash(x))

    #Convert to datetime
    data['publish_date'] = pd.to_datetime(data['publish_date']) 
    data['ocr_date'] = pd.to_datetime(data['ocr_date']) 

    #Filter for ocrdate
    cond = data['ocr_date'] >= config['min_ocr_date']
    logger.info(f'\n\n*** The following text was deleted because the ocr date was too old:\n {data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering date. Valid posts = {len(data)}')

    #Filter for publish date
    cond = data['publish_date'] >= config['min_publish_date']
    logger.info(f'\n\n*** The following text was deleted because publish data was too old:\n {data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering publishdate. Valid posts = {len(data)}')

    #Filter for document word confidence
    cond = data['document_word_confidence'] >= config['min_document_word_confidence']
    logger.info(f'\n\n*** The following text was deleted because document confidence was too low: \n{data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering document confidence. Valid posts = {len(data)}')

    #Filter for paragraph confidence
    cond = data['confidence'] >= config['min_confidence']
    logger.info(f'\n\n*** The following text was deleted because paragraph confidence was too low:\n {data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering paragraph confidence. Valid posts = {len(data)}')

    #Replace username in tweets
    if config['replace_usernames_tweets']:
        data['text'] = data['text'].apply(lambda x: replace_usernames_tweets(x, config['replace_usernames_tweets']))
        logger.info(f'***  Replaced usernames in tweets with {config["replace_usernames_tweets"]}.')

    #Replace urls
    if config['replace_urls']:
        data['text'] = data['text'].apply(lambda x: replace_urls(x, config['replace_urls']))
        logger.info(f'***  Replaced urls with {config["replace_urls"]}.')

    #Replace email addresses
    if config['replace_email_addresses']:
        data['text'] = data['text'].apply(lambda x: replace_email_addresses(x, config['replace_email_addresses']))
        logger.info(f'***  Replaced email addresses with {config["replace_email_addresses"]}.')

    #Number of alpha words in paragraph
    cond = data['text'].apply(lambda x: count_alphawords(x)) >= config['min_alphawords_paragraph']
    logger.info(f'\n\n*** The following text was deleted because too few alpha words: \n{data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering min alpha words. Valid posts = {len(data)}')

    #Numbers of words in paragraph
    cond = data['text'].apply(lambda x: count_words(x)) >= config['min_words_paragraph']
    logger.info(f'\n\n*** The following text was deleted: \n{data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering min words. Valid posts = {len(data)}')

    #Minimum number of characters in an article
    #Add this to the frame since we will use it later for sorting
    data['doc_length'] = data["text"].apply(len).groupby(data['id']).transform(sum)
    cond = data['doc_length'] >= config['min_length_article']
    logger.info(f'\n\n*** The following text was deleted because the article minimum lenght was too small:\n {data[~cond]}')
    data = data[cond]
    logger.info(f'***  Completed filtering min length article. Valid posts = {len(data)}')
 
    #Remove duplicates
    data.sort_values(by=['doc_length','paragraph_id'], inplace=True, ascending=[False,True])
    data.drop_duplicates(subset="hash",inplace=True,keep='first')

    logger.info(f'***  Finished cleaning. Final valid posts: {len(data)}')

    #save jsonl
    output_filename = os.path.join(args.output_folder, os.path.basename(args.input_file))
    save_jsonl(data, output_filename)


def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_folder', required=True, help='Path to output folder.')
    parser.add_argument('--config_file',required=False, default="config.json", help='Needs to be placed in output folder. Overrides the default config.json')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)

