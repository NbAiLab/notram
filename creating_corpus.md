# Creating the Norwegian Corpus
This guide describes the steps used for creating the Norwegian Corpus. The final corpus will have one book/article/webpage on one single line. To get to this point, there are several steps wee need to go through.


## Extract Text from Alto Files

### Books
### Newspapers
### Periodicals


## Extract Text from Other Sources
Run the script below for extracting text to /source. As much text as possible should be extracted at this stage.
```bash
script here
```

## Create ParagraphPerLine-files
Selection of what to include in the corpus is done at this level. The decisions on this level is mainly done on basis of what is written in the meta-file. 
```bash
    parser.add_argument('-i', '--input_folder', required=True, help='Path to input folder. All files ending with *.txt will be parsed.')
    parser.add_argument('-o', '--output_file', required=True, help='Output file. Will overwrite it exists')
    parser.add_argument('-s', '--min_ocr_date', required=False, default='01-01-2009', help='Will drop all articles that was ocr-ed prior to this date')
    parser.add_argument('-p', '--min_publish_year', required=False, default='1814', help='Will drop all articles published prior to this year')
    parser.add_argument('-l', '--language', required=False, default='', help='If set, only articles in this language will be included')
    parser.add_argument('-L', '--unknown_language', required=False, default='nob', help='Any unknown language is set to this value')
    parser.add_argument('-y', '--unknown_year', required=False, default='1900', help='Any unknown year is set to this value')
    parser.add_argument('-C', '--min_confidence_article', required=False, default='0.9', help='Will drop all articles with lower average word confidence')
    parser.add_argument('-c', '--min_confidence_paragraph', required=False, default='0.8', help='Will drop all paragraphs with lower average word confidence')
    parser.add_argument('-a', '--min_words_paragraph', required=False, default='5.0', help='Minimum average number of words per paragraph in the entire article/book')
    add_bool_arg(parser, 'debug', default=False, help='Print debug info about paragraphs.')
```
For books this script can be run with the default settings to create the ppl-file.
```bash
python create_ppl.py --input_file /source/myfile.txt --output_file /ppl/myfile_ppl.txt
```

## Create Cleaned PPL-files
This is an addidtional step analysing the text quality for inclusion. It also does some general standardisation, like converting to utf-8. The script has the following options.
 
```bash
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_file', required=True, help='Path to output file.')
    parser.add_argument('--username_filler', default='@user', type=str, help='Username filler (ignored when replace_username option is false)')
    parser.add_argument('--url_filler', default='http://domain.com', type=str, help='URL filler (ignored when replace_urls option is false)')
    parser.add_argument('--email_filler', default='anonymous@domain.com', type=str, help='Email filler (ignored when replace_email option is false)')
    parser.add_argument('--digibok', default='keep', type=str, help='Handling of digibok_ids. "keep", "remove" or "auto". Last option relies on other settings in script')
    parser.add_argument('--min_alphawords', default=2, type=int, help='The minimum number of letter-only- words with a length of at least 2. Keeps empty lines.')
    parser.add_argument('--max_words_in_section', required=False, default=1000, help='After reaching this maximum number of words, the next paragraph will be split into a new section.')

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
```
For books this script can be run with the default settings to create the cleaned-ppl-file.
```bash
python clean_ppl --input_file /ppl/myfile_ppl.txt --output_file /cleaned_ppl/myfile_cleaned_ppl.txt
```

## Deduplicate and randomize
This script removes the paragraph so that max N words are in each section. It then deduplicates these sections and randomizes them. In the end it is divided into shards so that it is easier to read for the tfrecord-generator.
```bash
    parser.add_argument('-i', '--input_folder', required=True, help='Path to input folder. All files ending with *.txt will be parsed.')
    parser.add_argument('-o', '--output_folder', required=True, help='Output folder. Will be created if it does not exist')
    parser.add_argument('-s', '--shards', required=False, default=1, help='Number of shards')
    add_bool_arg(parser, 'randomize', default=False, help='Randomizes all articles before segmentation.')
    add_bool_arg(parser, 'deduplicate', default=False, help='Deduplicates all articles before sentence segmenation.')
 ```
 ```bash
python dedup_rand_shard.py --randomize --deduplicate -w 1000 --input_folder /ppl/cleaned_folder/ --output_folder /cleaned_ppl/dedup/ 
```
