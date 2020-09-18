
import sys, os
import ftfy
from tqdm import tqdm

sys.path.append(r'../utils')
sys.path.append(r'../')

from utils.textCleaner import cleanText
from utils.misc import ArgParseDefault, add_bool_arg

def main(args):

    input_files = get_input_files(args.input_path)
    print(f'Found {len(input_files):,} input text files')
    
    output_folder = "output"
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    for input_file in tqdm(input_files):
        input_filename = os.path.basename(input_file).split('.txt')[0]
        output_filepath = os.path.join(output_folder, f'{input_filename}_clean.txt')

        with open(input_file, 'r') as f_in, open(output_filepath, 'w') as f_out:
            for i, line in enumerate(tqdm(f_in, total=num_lines)):
                output_text = preprocess(line, args)
                output_text += f'\n'
                f_out.write(output_text)
                
                print(line)
                print(clean_text)

def get_input_files(input_folder):
    return glob.glob(os.path.join(input_folder, '**', '*.txt'))


def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_path', help='Path to folder with txt files.')
    parser.add_argument('--username_filler', default='@user', type=str, help='Username filler')
    parser.add_argument('--url_filler', default='http://domain.com', type=str, help='URL filler (ignored when replace_urls option is false)')
    parser.add_argument('--num_logged_samples', default=10, type=int, help='Log first n samples to output')
    add_bool_arg(parser, 'run_in_parallel', default=True, help='Run script in parallel')
    add_bool_arg(parser, 'replace_usernames', default=False, help='Replace usernames with filler. Mainly for tweets')
    add_bool_arg(parser, 'replace_urls', default=True, help='Replace URLs with filler')
    add_bool_arg(parser, 'asciify_emojis', default=True, help='Asciifyi emojis. On by default but mainly useful for social media')
    add_bool_arg(parser, 'replace_multiple_usernames', default=False, help='Replace "@user @user" with "2 <username_filler>. Mainly for use on tweets"')
    add_bool_arg(parser, 'standardize', default=True, help='Replace "Standardize text. Remove all contraol characters.')
    add_bool_arg(parser, 'replace_multiple_urls', default=False, help='Replace "http://... http://.." with "2 <url_filler>". Mainly for use on tweets')
    add_bool_arg(parser, 'remove_unicode_symbols', default=True, help='After preprocessing remove characters which belong to unicode category "So"')
    add_bool_arg(parser, 'remove_accented_characters', default=False, help='Remove accents/asciify everything. Probably not recommended.')
    add_bool_arg(parser, 'standardize_punctuation', default=True, help='Standardize (asciifyi) special punctuation')
    add_bool_arg(parser, 'do_lower_case', default=True, help='Convert text to lower case')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)


