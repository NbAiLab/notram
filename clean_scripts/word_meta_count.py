import sys, glob, os, re, argparse
from tqdm import tqdm
import numpy as np
import pandas as pd
sys.path.append(r'../utils')
sys.path.append(r'../')
from utils.misc import ArgParseDefault, add_bool_arg
from datetime import datetime, timedelta
from utils.textCleaner import cleanTextBlock, cleanTextBlock_notram
from pathlib import Path


def main(args):
	input_files = get_input_files(args.input_folder)
	print(f'Found {len(input_files):,} meta files')
	totalwords = 0
	#Read everything into one large pandas frame 
	for input_file in tqdm(input_files):		
		try:
			meta = pd.read_json(input_file)
			average_w_paragraph = float(meta.averageNumberOfWordsPerParagraph[0])
			num_paragraphs = int(len(meta.paragraphs))	
			words = int(average_w_paragraph * num_paragraphs)
			totalwords += words
		except Exception:
			print(f'Problem reading {input_file}. Simply ignoring this file')
			pass

	print(f'Total number of words in {args.input_folder} = {totalwords:,}')

def get_input_files(input_folder):
	#return glob.glob(os.path.join(input_folder, '*.txt'))
	return list(Path(input_folder).rglob('*.meta'))

def parse_args():
	# Parse commandline
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input_folder', required=True, help='Path to input folder. All files ending with *.meta will be parsed.')
	args = parser.parse_args()
	return args


if __name__ == "__main__":
	args = parse_args()
	main(args)




