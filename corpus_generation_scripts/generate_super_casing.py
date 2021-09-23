########################################################
## File for generating a super-cased corpus ##
## Adds unicode characters at beginning of words ##
#######################################################

from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from utils.misc import ArgParseDefault, add_bool_arg
import glob
import os

def supercase(text):
    shift = "⇧"
    caps = "⇪"
    tokens = word_tokenize(text)
    mod_tokens = []
    
    for t in tokens:
        #Check if entire word is at least two characters and is entirely uppercased
        if len(t) >= 2 and t == t.upper() and t[0].isalpha():
            mod_tokens.append(t.lower() + caps)
        #Check if upper
        elif t[0].isupper():
            mod_tokens.append(t.lower() + shift)
        #If none of this is true, return original
        else:
            mod_tokens.append(t.lower())

    supercasedtext = TreebankWordDetokenizer().detokenize(mod_tokens)
    return supercasedtext

def main(args):
    input_files = glob.glob(os.path.join(args.input_folder, "*.txt"))
    for input_file in input_files:
        output_file = os.path.join(args.output_folder, os.path.basename(input_file)) 
        if os.path.isfile(output_file):
            print(f'Already processed: {output_file}')
        else:
            print(f'Starting to process: {output_file}')
        
            with open(input_file) as f:
                lines = f.readlines()
                for n, line in enumerate(lines):
                    with open(output_file, "a") as o:
                        o.write(supercase(line)+"\n")
        
def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_folder', required=True, help='Path to input folder.')
    parser.add_argument('--output_folder', required=True, help='Path to output folder.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)


