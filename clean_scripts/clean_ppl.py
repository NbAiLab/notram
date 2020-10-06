# There is an additional script that does the same on entire folders

import sys, os, glob
from tqdm import tqdm
from pathlib import Path

sys.path.append(r'../utils')
sys.path.append(r'../')

from utils.textCleaner import cleanTextBlock
from utils.misc import ArgParseDefault, add_bool_arg

def main(args):
    input_file = args.input_file
    output_file = args.output_file

    valid = 0
    num_lines = sum(1 for _ in open(input_file, 'r'))
    input_filename = os.path.basename(input_file).split('.txt')[0]

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for i, line in enumerate(tqdm(f_in, total=num_lines)):
            output_text = cleanTextBlock(line, args)
            if output_text:
                valid += 1
                output_text += f'\n'
                f_out.write(output_text)
    print(f'Original file had {num_lines} lines. A total of {valid} lines written to file.')


def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_file', required=True, help='Path to output file.')
    parser.add_argument('--username_filler', default='@user', type=str, help='Username filler (ignored when replace_username option is false)')
    parser.add_argument('--url_filler', default='http://domain.com', type=str, help='URL filler (ignored when replace_urls option is false)')
    parser.add_argument('--email_filler', default='anonymous@domain.com', type=str, help='Email filler (ignored when replace_email option is false)')
    parser.add_argument('--digibok', default='keep', type=str, help='Handling of digibok_ids. "keep", "remove" or "auto". Last option relies on other settings in script')
    parser.add_argument('--min_alphawords', default=2, type=int, help='The minimum number of letter-only- words with a length of at least 2. Keeps empty lines.')
    #parser.add_argument('--num_logged_samples', default=10, type=int, help='Log first n samples to output')
    #add_bool_arg(parser, 'run_in_parallel', default=True, help='Run script in parallel')
    add_bool_arg(parser, 'replace_usernames', default=False, help='Replace usernames with filler. Mainly for tweets')
    add_bool_arg(parser, 'replace_urls', default=False, help='Replace URLs with filler')
    add_bool_arg(parser, 'replace_email', default=True, help='Replace emails with filler')
    add_bool_arg(parser, 'fix_unicode', default=True, help='Use ftfy to fix and standardise unicode. Converts it all to valid utf-8')
    add_bool_arg(parser, 'asciify_emojis', default=False, help='Asciifyi emojis. On by default but mainly useful for social media')
    add_bool_arg(parser, 'replace_multiple_usernames', default=False, help='Replace "@user @user" with "2 <username_filler>. Mainly for use on tweets"')
    add_bool_arg(parser, 'standardize', default=True, help='Replace "Standardize text. Remove all control characters.')
    add_bool_arg(parser, 'replace_multiple_urls', default=False, help='Replace "http://... http://.." with "2 <url_filler>". Mainly for use on tweets')
    add_bool_arg(parser, 'remove_unicode_symbols', default=True, help='After preprocessing remove characters which belong to unicode category "So"')
    add_bool_arg(parser, 'remove_accented_characters', default=False, help='Remove accents/asciify everything. Probably not recommended.')
    add_bool_arg(parser, 'standardize_punctuation', default=True, help='Standardize (asciifyi) special punctuation')
    add_bool_arg(parser, 'do_lower_case', default=False, help='Convert text to lower case')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)


