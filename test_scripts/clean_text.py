import sys, os, glob
from tqdm import tqdm

sys.path.append(r'../utils')
sys.path.append(r'../')

from utils.textCleaner import cleanTextBlock
from utils.misc import ArgParseDefault, add_bool_arg

def main(args):
    input_files = get_input_files(args.input_folder)
    print(f'Found {len(input_files):,} input text files')
    
    output_folder = args.output_folder

    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)


    for input_file in tqdm(input_files):
        num_lines = sum(1 for _ in open(input_file, 'r'))
        input_filename = os.path.basename(input_file).split('.txt')[0]
        output_filepath = os.path.join(output_folder, f'{input_filename}_clean.txt')

        with open(input_file, 'r') as f_in, open(output_filepath, 'w') as f_out:
            for i, line in enumerate(tqdm(f_in, total=num_lines)):
                output_text = cleanTextBlock(line, args)
                if output_text:
                    output_text += f'\n'
                    f_out.write(output_text)

def get_input_files(input_folder):
    return glob.glob(os.path.join(input_folder, '*.txt'))

def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_folder', required=True, help='Path to folder with txt files.')
    parser.add_argument('--output_folder', required=True, help='Path to output folder.')
    parser.add_argument('--username_filler', default='@user', type=str, help='Username filler (ignored when replce_username option is false)')
    parser.add_argument('--url_filler', default='http://domain.com', type=str, help='URL filler (ignored when replace_urls option is false)')
    parser.add_argument('--email_filler', default='anonymous@domain.com', type=str, help='Email filler (ignored when replace_email option is false)')
    parser.add_argument('--minimum_words', default=2, type=int, help='The minimum number of words in the block to keep it')
    parser.add_argument('--minimum_alpha', default=2, type=int, help='The minimum number of alphanumeric characters in the block to keep it. Removes OCR errors from cover pages.')
    #parser.add_argument('--num_logged_samples', default=10, type=int, help='Log first n samples to output')
    #add_bool_arg(parser, 'run_in_parallel', default=True, help='Run script in parallel')
    add_bool_arg(parser, 'replace_usernames', default=False, help='Replace usernames with filler. Mainly for tweets')
    add_bool_arg(parser, 'replace_urls', default=True, help='Replace URLs with filler')
    add_bool_arg(parser, 'replace_email', default=True, help='Replace emails with filler')
    add_bool_arg(parser, 'fix_unicode', default=True, help='Use ftfy to fix and standardise unicode. Converts it all to valid utf-8')
    add_bool_arg(parser, 'asciify_emojis', default=True, help='Asciifyi emojis. On by default but mainly useful for social media')
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


