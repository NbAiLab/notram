####################################################################################
# Read all cleaned files in a directory ############################################
# * Deduplicate ####################################################################
# * Randomize  #####################################################################
# * Divide into n shards  ##########################################################
####################################################################################


import sys, glob, os, re, argparse
import pandas as pd
from pandarallel import pandarallel
from tqdm import tqdm
import numpy as np
sys.path.append(r'../utils')
sys.path.append(r'../')
from utils.misc import ArgParseDefault, add_bool_arg

# Initialization
pandarallel.initialize()

def main(args):
    input_files = get_input_files(args.input_folder)
    print(f'Found {len(input_files):,} input text files')
 
    output_folder = args.output_folder

    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    content = pd.Series()
    complete = pd.Series()

    #Read everything into one large pandas frame 
    for input_file in tqdm(input_files):
        content = pd.read_csv(input_file, sep='\r', encoding='utf-8',squeeze=True, header=None)
        complete = pd.concat([complete, content], ignore_index=True)
    
    print(f'Loaded all files. There is a total of {len(complete)} articles to process.')

    # Single word paragraphs does not make sense from a mlm point of view. This also automatically deletes the docid    
    complete = complete[~complete.str.count('\s+').lt(2)]
    print(f'There are {len(complete)} articles after removing all articles with less than two words.')
    
    complete = complete.dropna()
    print(f'There are {len(complete)} articles after removing NaN.')


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


    #Save
    for id, df_i in  enumerate(np.array_split(complete, int(args.shards))):
        output_file = os.path.join(args.output_folder,f'output_{id+1}.txt')       
        print(f'Saving file #{id+1}: {output_file}')
        df_i.to_csv(output_file, header=False, index=False)

    #Print some statistics
    print(f'Saved all files to folder: {args.output_folder}')


def get_input_files(input_folder):
    return glob.glob(os.path.join(input_folder, '*.txt'))


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_folder', required=True, help='Path to input folder. All files ending with *.txt will be parsed.')
    parser.add_argument('-o', '--output_folder', required=True, help='Output folder. Will be created if it does not exist')
    parser.add_argument('-s', '--shards', required=False, default=1, help='Number of shards')
    add_bool_arg(parser, 'randomize', default=False, help='Randomizes all articles before segmentation.')
    add_bool_arg(parser, 'deduplicate', default=False, help='Deduplicates all articles before sentence segmenation.')
 
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)




