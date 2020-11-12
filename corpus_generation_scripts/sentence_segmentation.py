####################################################################################
# Read an UTF8-encoded file with one article per line ##############################
# Produce a new file with: #########################################################
# * Line breaks after each sentence ################################################
# * Double line breaks after each article ##########################################
####################################################################################


import sys, glob, os, re, argparse
import pandas as pd

#Norwegian Spacy
import spacy
from spacy.lang.nb.examples import sentences 
nlp = spacy.load('nb_core_news_sm')
from pandarallel import pandarallel
import ftfy

# Initialization
pandarallel.initialize()

def main(args):

    #Parse paths
    full_paths = [os.path.join(os.getcwd(), path) for path in args.input]
    
    files = set()
    for path in full_paths:
        if os.path.isfile(path):
            files.add(path)
        else:
            files |= set(glob.glob(path + '/*.txt'))

    print('Prosessing the following files:')
    for f in files:
        print(f)

    #Read files
    valid_paragraph_count = 0
    valid_sentence_count = 0
    
    for f in files:
        with open(f) as fp:
            
            valid_paragraph_count += 1
            input_basename = os.path.basename(f)
            output_file_name = f'sentences_{input_basename}'
            output_file = os.path.join(args.output_folder,output_file_name)
            print(f'Opening {f} and printing to {output_file}')
            
            for n,paragraph in enumerate(fp):
                if n % 10000 == 0:
                    print(f'..paragraph {n}')

                sentences = sentseq(paragraph.strip('\"')) 
                valid_sentence_count += sentences.count('\n')
                with open(output_file, 'a', encoding='utf-8') as op:
                    op.write(sentences)

        print(f'Wrote {os.path.join(args.output_folder,output_file)} with {valid_paragraph_count} paragraphs and {valid_sentence_count} sentences')



def sentseq(text):
    if len(text) >= 100000:
        print(len(text))
        print(text)
    section = nlp(text)
    article = ""
    for sentence in section.sents:
        article += str(sentence) + "\n"
    return article


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, nargs='+', help='Input file(s) or path to files. If path is provided, all files ending with *.txt will be parsed.')
    parser.add_argument('-o', '--output_folder', required=True, help='Output folder. Needs to be separate from input folder')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)




