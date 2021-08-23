####################################################################################
# File for making emoticon and supercase vocab building file
# Makes it so large that it can not be ignored in vocab building
# Output is an UTF-8 file with one document per line
####################################################################################

import requests
import ftfy, glob, argparse, os
import jsonlines
from tqdm import tqdm
from datetime import datetime
from slugify import slugify
import json

def main(args):
    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        #emoticons
        emoticonfile = open(args.input_file, 'r')
        lines = emoticonfile.readlines()
        for _ in range(100):
            for l in lines:
                n+=1
                entry = {}
                entry['id'] = "special_"+str(n)
                entry['text'] = l.replace('\n', ' ').replace('\r', '').replace('\t', '')
                writer.write(entry)
        #supercasing
        for _ in range(1000):
            n+=1
            entry = {}
            entry['id'] = "special_"+str(n)
            entry['text'] = "⇧"
            writer.write(entry)
        for _ in range(1000):
            n+=1
            entry = {}
            entry['id'] = "special_"+str(n)
            entry['text'] = "⇪"
            writer.write(entry)
        for _ in range(1000):
            n+=1
            entry = {}
            entry['id'] = "special_"+str(n)
            entry['text'] = "\n"
            writer.write(entry)


    print(f'File is written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', required=True, help='Output file name. Will overwrite it exists')
    parser.add_argument('-i', '--input_file', required=True, help='Input file name.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
#print(soup.prettify()) # print the parsed data of html
