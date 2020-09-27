####################################################################################
# Read all files in a directory with accompanying json meta file and validate ######
# * scan date ######################################################################
# * publication year  ##############################################################
# * language  ######################################################################
# * wc document ####################################################################
# * wc paragraph  ##################################################################
# * language  ######################################################################
####################################################################################


import sys, glob, os, re, argparse
from tqdm import tqdm
import numpy as np
import pandas as pd
sys.path.append(r'../utils')
sys.path.append(r'../')
from utils.misc import ArgParseDefault, add_bool_arg
from datetime import datetime, timedelta
from utils.textCleaner import cleanTextBlock, cleanTextBlock_notram


def main(args):
    input_files = get_input_files(args.input_folder)
    print(f'Found {len(input_files):,} input text files')
 
    complete = pd.Series()

    #Read everything into one large pandas frame 
    #for input_file in tqdm(input_files):
    for input_file in input_files:
        article = pd.Series()
        meta_file = input_file.replace(".txt",".meta")
        article = pd.read_csv(input_file, sep='\r', encoding='utf-8',squeeze=True, header=None,quotechar=None, quoting=3)
        meta = pd.read_json(meta_file)
        input_file_name = os.path.basename(input_file)

        publishYear = meta.publishYear[0]
        if publishYear == "<unknown>":
            publishYear = args.unknown_year
        
        language = meta.language[0]
        if language == "<unknown>":
            language = args.unknown_language

        scanDate = f'{meta.urn[0][14:16]}-{meta.urn[0][12:14]}-{meta.urn[0][8:12]}'
        confidenceArticle = meta.bookOcrWordconfidence[0]
        confidenceParagraphs = meta.paragraphs
       
        keep = True
        #Make a sanity check regarding the length of the article and the length of the meta file. 
        if len(meta) != len(article):
            print(f'ERROR: {input_file_name}: The length of input file is {len(article)} while the corresponding meta-file has a length of {len(meta)}. Skipping file!')
            keep = False


        #Scan Date
        if (datetime.strptime(args.min_scan_date, '%d-%m-%Y') < datetime.strptime(scanDate, '%d-%m-%Y')) and keep:
            print(f'{input_file_name} deleted because minimum scan age is {args.min_scan_date}. This book is scanned {scanDate}.')
            keep = False

        #Language
        if (args.language != '') and keep:
            if (args.language != language) and keep:
                print(f'{input_file_name} deleted because article language is {language} and only {args.language} should be included.')
                keep = False
        
        #Publish Year
        if (int(args.min_publish_year) >= int(publishYear)) and keep:
            print(f'{input_file_name} deleted because minimum publication year is {args.min_publish_year}. This book was published in {publishYear}.')
            keep = False
        
        #Confidence Article
        if (float(args.min_confidence_article) >= float(confidenceArticle)) and keep:
            print(f'{input_file_name} deleted because minimum article confidence is {args.min_confidence_article}. This book has a confidence of {confidenceArticle}.')
            keep = False
        
        if not keep:
            article.drop(article.index, inplace=True)
        
        #Else evaluate every paragraph
        else:
            preProcessArticleLength = len(article)
            
            #Paragraph Confidence
            for aid,text in enumerate(article):
                pconf = float(meta.paragraphs[aid]['confidence'])
                if pconf < float(args.min_confidence_paragraph):
                    if args.debug: print(f'P{aid} - Conf={pconf} - this is less then {args.min_confidence_paragraph}. Dropping line.\n{text}\n')
                    article.drop([aid], inplace=True)
            article.reset_index(drop=True, inplace=True)
            
            #Do cleaning
            if args.clean:
                for aid,text in enumerate(article):
                    article[aid] = cleanTextBlock_notram(text,do_lower_case=False)
                    if article[aid] == "":
                        article.drop([aid], inplace=True)
            article.reset_index(drop=True, inplace=True)
            
            print(f'{input_file_name} is valid. Keeping {len(article)} of {preProcessArticleLength} paragraphs.')

        #Append whatever is left into a dataframe
        complete = complete.append(article, ignore_index=True)

    #Save
    complete.to_csv(args.output_file, header=None, index=None)
    print(f'Final file with {len(complete)} lines was saved to {args.output_file}')
    print(f'Number of valid words in corpus: {complete.str.split().apply(len).sum()}')

def get_input_files(input_folder):
    return glob.glob(os.path.join(input_folder, '*.txt'))


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_folder', required=True, help='Path to input folder. All files ending with *.txt will be parsed.')
    parser.add_argument('-o', '--output_file', required=True, help='Output file. Will overwrite it exists')
    parser.add_argument('-s', '--min_scan_date', required=False, default='31-12-2999', help='Will drop all articles that is scanned prior to this date')
    parser.add_argument('-p', '--min_publish_year', required=False, default='2999', help='Will drop all articles published prior to this year')
    parser.add_argument('-l', '--language', required=False, default='', help='If set, only articles in this language will be included')
    parser.add_argument('-L', '--unknown_language', required=False, default='nob', help='Any unknown language is set to this value')
    parser.add_argument('-y', '--unknown_year', required=False, default='1900', help='Any unknown year is set to this value')
    parser.add_argument('-C', '--min_confidence_article', required=False, default='1.0', help='Will drop all articles with lower average word confidence')
    parser.add_argument('-c', '--min_confidence_paragraph', required=False, default='1.0', help='Will drop all paragraphs with lower average word confidence')
    add_bool_arg(parser, 'debug', default=False, help='Print debug info about paragraphs.')
    add_bool_arg(parser, 'clean', default=False, help='Run precedure for cleaning text. Specified in sub-routine.')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)




