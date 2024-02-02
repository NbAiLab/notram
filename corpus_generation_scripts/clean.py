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
import time
from pandarallel import pandarallel
import stopword_cleaner

pandarallel.initialize(use_memory_fs=True)

start_time = time.time()

def exec_time():
    end_time = time.time()
    out = str(round(end_time-start_time,1)) + " seconds"
    return out

# compile regexes
username_regex = re.compile(r'(^|[^@\w])@(\w{1,15})\b')
url_regex = re.compile(r'((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))')
email_regex = re.compile(r'[\w\.-]+@[\w\.-]+')
control_char_regex = re.compile(r'[\r\n\t]+')

stopwordCleaner = stopword_cleaner.Cleaner()

def read_config(cfile):
    try:
        f = open(cfile,"r")
        config = json.load(f)
    except:
        logger.info("Error. There has to be a valid config-file in the output directory")
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
    df_inter['json_element'].parallel_apply(json.loads)

    logger.info(f'***  Json parsed. {len(df_inter)} lines. ({exec_time()})')
    print(f'***  Json parsed with {len(df_inter)} lines. ({exec_time()})')


    #Normalise
    metakeys = get_metakeys(lines)
    data = pd.json_normalize(df_inter['json_element'].parallel_apply(json.loads), record_path =['paragraphs'], meta=metakeys, errors='ignore')

    return data

def save_jsonl(data, filename):
   
    with open(filename, 'w', encoding='utf-8') as file:
        data.to_json(file, orient='records', lines=True, force_ascii=False)
    
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
        logger.debug(f'Changed "{input_text}" -> "{text}"')

    return text

def truncate_last_valid_sentence(text):
    triple_val = text.rfind("tml")+2
    double_val = max(text.rfind("=P"),text.rfind("=p"), text.rfind(":p"), text.rfind(":P"), text.rfind(";D"), text.rfind(":D"), text.rfind(";/"))+1
    last_val = max(triple_val,double_val, text.rfind("."),text.rfind(";"),text.rfind(":"), text.rfind("?"), text.rfind(")"), text.rfind("!"), text.rfind("*"), text.rfind("\""), text.rfind("\'")) + 1
    
    if last_val <=  2:
        last_val = 0
    
    if last_val != len(text):
        logger.debug(f'Changed "{text}" -> "{text[0:last_val]}"')
    
    return text[0:last_val]

def replace_usernames_tweets(text, filler='@User'):
    # replace other user handles by filler
    text = str(text)
    input_text = str(text)
    text = re.sub(username_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split())
    
    if input_text != text:
        logger.debug(f'Changed "{input_text}" -> {text}"')

    return text

def replace_urls(text, filler='http://www.no'):
    text = str(text)
    input_text = text
    # <url> is a marker used internally. use filler instead
    text = text.replace('<url>', filler)
    # replace other urls by filler
    text = re.sub(url_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split()) 
    
    if input_text != text:
        logger.debug(f'Changed "{input_text}" -> {text}"')

    return text

def replace_email_addresses(text, filler='email@email.no'):
    text = str(text)
    input_text = text
    text = re.sub(email_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split()) 
    
    if input_text != text:
        logger.debug(f'Changed "{input_text}" -> {text}"')

    return text

def run_stopword_cleaner(text):
    cleaned_text = stopwordCleaner.clean(text)
    if cleaned_text != None:
        return True
    else:
        logger.debug(f'Removed {text} (due to low stop word density.)"')
        return False

def main(args):
    pd.set_option("display.max_rows", None)
    ocr_doc = 1

    #Invoke logging
    log_name = os.path.basename(args.input_file).replace(".jsonl","")
    log_name = log_name + ".log"

    logging.basicConfig(filename=os.path.join(args.output_folder,"log/",log_name), format='%(asctime)s %(message)s', filemode='w')

    config = read_config(args.config_file)
    
    print(f'*** Starting to process: {args.input_file}')
    data = load_jsonl(args.input_file)
   
    logger.info(f'***  Data loaded. {len(data)} paragraphs. ({exec_time()})')
    print(f'*** Data loaded with {len(data)} paragraphs. Log written to {os.path.join(args.output_folder, "log/", log_name)}. ({exec_time()})')

    
    if config['assume_late_missing_dates']:
        publish_date = "20211007"
        publish_year = "2021"
        ocr_date = "20211007"
        ocr_year = "2021"
    else:
        publish_date = "18140517"
        publish_year = "1814"
        ocr_date = "18140517"
        ocr_year = "1814"



    #Create columns if they do not exist
    if 'publish_date' not in data:
        data['publish_date'] = publish_date
    
    if 'publish_year' not in data:
        data['publish_year'] = publish_year

    if 'ocr_date' not in data:
        data['ocr_date'] = ocr_date
    
    if 'ocr_year' not in data:
        data['ocr_year'] = ocr_year

    if 'document_word_confidence' not in data:
        data['document_word_confidence'] = 1.0
        #If documen_word_confidence is not set, we assume that this is not an ocr1ed document
        ocr_doc = 0


    if 'confidence' not in data:
        data['confidence'] = 1.0
    
    
    #Fix possible NaN is mixing datasets
    data['document_word_confidence'] = data['document_word_confidence'].fillna(1.0)
    data['confidence'] = data['confidence'].fillna(1.0)
    data['publish_date'] = data['publish_date'].fillna(publish_date)
    data['publish_year'] = data['publish_year'].fillna(publish_date)
    data['ocr_date'] = data['ocr_date'].fillna(publish_date)
    data['ocr_year'] = data['ocr_year'].fillna(publish_date)


    #Fix unicode
    if config['normalise_unicode']:
        data['text'] = data['text'].parallel_apply(normalise_unicode)
    logger.info(f'***  Normalised unicode. Removed double spaces. Trimmed string. ({exec_time()})')
    print(f'***  Normalised unicode. Removed double spaces. Trimmed string.({exec_time()})')

    #Truncate last valid sentence in paragraph
    if config['truncate_last_valid_sentence']:
        data['text'] = data['text'].parallel_apply(truncate_last_valid_sentence)
   
    #Delete paragraph where the max word length is too long. This indicate OCR errors
    cond = data['text'].parallel_apply(lambda x: max_word_length(x)) <= config['max_word_length_paragraph']
    logger.debug(f'\n\n*** The following text was deleted because some of the words were too long:\n {data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering out pragraphs with too long words. Valid posts = {len(data)}. ({exec_time()})')
    print(f'***  Completed filtering out pragraphs with too long words. Valid posts = {len(data)}. ({exec_time()})')
    
    #Do stopword cleaning
    if config["run_stopword_cleaner"]:
        cond = data["text"].parallel_apply(run_stopword_cleaner)
        data = data[cond]
        logger.info(f'***  Removed sentences with low stopword density. Valid posts = {len(data)}. ({exec_time()})')
        print(f'***  Removed sentences with low stopword density. Valid posts = {len(data)}. ({exec_time()})')
    else:
        logger.info(f'***  Skipped stop word cleaning. ({exec_time()})')
        print(f'***  Skipped stop word cleaning. ({exec_time()})')

    #Add hash
    data['hash'] = data['text'].parallel_apply(lambda x: get_hash(x))
    logger.info(f'***  Added hash. ({exec_time()})')
    print(f'***  Added hash. ({exec_time()})')
    
    #Convert to datetime
    if "olddateformat" in args.input_file:
        data['publish_date'] = pd.to_datetime(data['publish_date'], format='%d%m%Y', errors='coerce').dt.strftime('%Y%m%d')
    else:
        data['publish_date'] = pd.to_datetime(data['publish_date'], format='%Y%m%d', errors='coerce').dt.strftime('%Y%m%d')
    
    logger.info(f'***  Converted old date format. ({exec_time()})')
    print(f'***  Converted old data format. ({exec_time()})')

    data['publish_year'] = pd.to_datetime(data['publish_date'], format='%Y%m%d', errors='coerce').dt.strftime('%Y')
    data['ocr_date'] = pd.to_datetime(data['ocr_date'], format='%Y%m%d', errors='coerce').dt.strftime('%Y%m%d') 
    data['ocr_year'] = pd.to_datetime(data['ocr_date'], format='%Y%m%d', errors='coerce').dt.strftime('%Y') 
    logger.info(f'***  Created publish year, ocr_date, ocr_year. ({exec_time()})')
    print(f'***  Created publish year, ocr_date, ocr_year. ({exec_time()})')

    #Set meaningfult default for missing dates
    data['publish_date'] = data['publish_date'].fillna(publish_date)
    data['publish_year'] = data['publish_year'].fillna(publish_year)
    data['ocr_date'] = data['ocr_date'].fillna(ocr_date)
    data['ocr_year'] = data['ocr_year'].fillna(ocr_year)
    logger.info(f'***  Created defaults for dates. ({exec_time()})')
    print(f'***  Created defaults for dates. ({exec_time()})')


    if ocr_date:
        cond = data['ocr_date'] >= config['min_ocr_date']
        logger.debug(f'\n\n*** The following text was deleted because the ocr date was too old:\n {data[~cond]["text"]}')
        data = data[cond]
        logger.info(f'***  Completed filtering OCR date. Valid posts = {len(data)}. ({exec_time()})')
        print(f'***  Completed filtering OCR date. Valid posts = {len(data)}. ({exec_time()})')
    else:
        print(f'***  Skipped evaluating ocr date since this is not an ocr document. ({exec_time()})')

    #Filter for publish date
    cond = data['publish_date'] >= config['min_publish_date']
    
    logger.debug(f'\n\n*** The following text was deleted because publish data was too old:\n {data[~cond]["text"]}')
    data = data[cond]
    logger.info(f'***  Completed filtering publishdate. Valid posts = {len(data)}. ({exec_time()})')
    print(f'***  Completed filtering publishdate. Valid posts = {len(data)}. ({exec_time()})')

    #Filter for document word confidence
    if ocr_doc:
        cond = data['document_word_confidence'].astype(float) >= config['min_document_word_confidence']
        logger.debug(f'\n\n*** The following text was deleted because document confidence was too low: \n{data[~cond]["text"]}')
        data = data[cond]
        logger.info(f'***  Completed filtering document confidence. Valid posts = {len(data)}. ({exec_time()})')
        print(f'***  Completed filtering document confidence. Valid posts = {len(data)}. ({exec_time()})')
    else:
        print(f'***  Skipped document confidence evaluation since this is not an ocr document. ({exec_time()})')


    #Filter for paragraph confidence
    if ocr_doc:
        cond = data['confidence'].astype(float) >= config['min_confidence_paragraph']
        logger.debug(f'\n\n*** The following text was deleted because paragraph confidence was too low:\n {data[~cond]["text"]}')
        data = data[cond]
        logger.info(f'***  Completed filtering paragraph confidence. Valid posts = {len(data)}. ({exec_time()})')
        print(f'***  Completed filtering paragraph confidence. Valid posts = {len(data)}. ({exec_time()})')
    else:
        print(f'***  Skipped paragraph confidence evaluation since this is not an ocr document. ({exec_time()})')


    #Replace username in tweets
    if config['replace_usernames_tweets']:
        data['text'] = data['text'].parallel_apply(lambda x: replace_usernames_tweets(x))
        logger.info(f'***  Replaced usernames in tweets with {config["replace_usernames_tweets"]}. ({exec_time()})')
        print(f'***  Replaced usernames in tweets with {config["replace_usernames_tweets"]}. ({exec_time()})')
        
    #Replace urls
    if config['replace_urls']:
        data['text'] = data['text'].parallel_apply(lambda x: replace_urls(x))
        logger.info(f'***  Replaced urls with {config["replace_urls"]}. ({exec_time()})')
        print(f'***  Replaced urls with {config["replace_urls"]}. ({exec_time()})')

    #Replace email addresses
    if config['replace_email_addresses']:
        data['text'] = data['text'].parallel_apply(lambda x: replace_email_addresses(x))
        logger.info(f'***  Replaced email addresses with {config["replace_email_addresses"]}. ({exec_time()})')
        print(f'***  Replaced email addresses with {config["replace_email_addresses"]}. ({exec_time()})')

    #Number of alpha words in paragraph
    if len(data)>0:
        cond = data['text'].parallel_apply(lambda x: count_alphawords(x)) >= config['min_alphawords_paragraph']
        logger.debug(f'\n\n*** The following text was deleted because too few alpha words: \n{data[~cond]["text"]}')
        data = data[cond]
    logger.info(f'***  Completed filtering min alpha words. Valid posts = {len(data)}. ({exec_time()})')
    print(f'***  Completed filtering min alpha words. Valid posts = {len(data)}. ({exec_time()})')

    #Numbers of words in paragraph
    if len(data)>0:
        cond = data['text'].parallel_apply(lambda x: count_words(x)) >= config['min_words_paragraph']
        logger.debug(f'\n\n*** The following text was deleted because it had too few words: \n{data[~cond]["text"]}')
        data = data[cond]
    logger.info(f'***  Completed filtering min words. Valid posts = {len(data)}. ({exec_time()})')
    print(f'***  Completed filtering min words. Valid posts = {len(data)}. ({exec_time()})')

    #Minimum number of characters in an article
    #Add this to the frame since we will use it later for sorting
    if len(data)>0:
        data['doc_length'] = data["text"].parallel_apply(len).groupby(data['id']).transform(sum)
        cond = data['doc_length'] >= config['min_length_article']
        logger.debug(f'\n\n*** The following text was deleted because the article minimum lenght was too small:\n {data[~cond]["text"]}')
        data = data[cond]
    logger.info(f'***  Completed filtering min length article. Valid posts = {len(data)}. ({exec_time()})')
    print(f'***  Completed filtering min length article. Valid posts = {len(data)}. ({exec_time()})')
 
    #Remove paragraphs with curly brackets
    if config['drop_paragraphs_with_curly_brackets']:
        cond = data['text'].str.contains('\\{')
        logger.debug(f'\n\n*** The following text was deleted because it contained left curly brackets:\n {data[~cond]["text"]}')
        data = data[~cond]
        cond = data['text'].str.contains('\\}')
        logger.debug(f'\n\n*** The following text was deleted because it contained right curly brackets:\n {data[~cond]["text"]}')
        data = data[~cond]
        print(f'***  Completed filtering out paragraphs with curly brackets. Valid posts = {len(data)}. ({exec_time()})')
    
    #Filter out paragraphs with encoding errors
    if config['drop_paragraphs_with_encoding_errors']:
        cond = data['text'].str.contains('�')
        data = data[~cond]
    logger.info(f'***  Filtered out encoding errors. The length is now {len(data)}. ({exec_time()})')
    print(f'***  Filtered out encoding errors. The length is now {len(data)}. ({exec_time()})')


    #Remove duplicates
    if len(data)>0:
        data.sort_values(by=['doc_length','paragraph_id'], inplace=True, ascending=[False,True])
        data.drop_duplicates(subset="hash",inplace=True,keep='first')
    logger.info(f'***  Finished deduplicating. Final valid posts: {len(data)}. ({exec_time()})')
    print(f'***  Finished deduplicating. Final valid posts: {len(data)}. ({exec_time()})')
    
    #Minimise the size of the jsonl
    if config['minimise_jsonl'] and len(data)>0:
        valid_columns = ['id','doc_type','publish_year','doc_length','paragraph_id','hash','text']
        data.drop(columns=[col for col in data if col not in valid_columns], inplace=True)
        logger.info(f'***  Minimised the dataframe. ({exec_time()})')
        print(f'***  Minimised the dataframe. ({exec_time()})')


    #Tidy up the file and sort it 
    data['publish_year'] = data['publish_year'].astype(int)
    data['paragraph_id'] = data['paragraph_id'].astype(int)
    if len(data)>0:
        data.sort_values(['doc_length', 'paragraph_id'], ascending=[False, True], inplace=True)
    logger.info(f'***  Fixed data type and sorted the dataframe. ({exec_time()})')
    print(f'***  Fixed data type and sorted the dataframe. ({exec_time()})')
    
    #Collapse the dataset
    colnames = [c for c in list(data.columns) if c!='paragraph_id' and c!='text' and c!='hash']
    data = data.groupby(colnames, as_index=False).apply(lambda x:[x[['paragraph_id','text','hash']].to_dict('records')]).rename(columns={None:'paragraphs'})
    logger.info(f'***  Collapsed the dataframe. The length after collapsing it {len(data)}. ({exec_time()})')
    print(f'***  Collapse the dataframe. The length after collapsing it {len(data)}. ({exec_time()})')

    #Save it as jsonl
    output_filename = os.path.join(args.output_folder, os.path.basename(args.input_file))
    save_jsonl(data, output_filename)
    logger.info(f'*** Finished processing file. Result has {len(data)} posts. Result is written to {os.path.join(args.output_folder, os.path.basename(args.input_file))}. ({exec_time()})')
    print(f'*** Finished processing file. Result has {len(data)} posts. Result is written to {os.path.join(args.output_folder, os.path.basename(args.input_file))}. ({exec_time()})')

def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_folder', required=True, help='Path to output folder.')
    parser.add_argument('--config_file',required=False, default="config.json", help='Needs to be placed in output folder. Overrides the default config.json')
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



