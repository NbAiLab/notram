########################################################
## File for generating a super-cased corpus ##
## Adds unicode characters at beginning of words ##
#######################################################

from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from utils.misc import ArgParseDefault, add_bool_arg
import glob
import os
import jsonlines

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

    with jsonlines.open(args.output_file, 'w') as writer:
        with jsonlines.open(args.input_file) as reader:
            for n, line in enumerate(reader):
                line['text'] = supercase(line['text'])
                writer.write(line)
        
def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_file', required=True, help='Path to output file.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)


