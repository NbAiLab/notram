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
### All Norwegian National Library Corpus Files
Selection of what to include in the corpus is done at this level. The decisions on this level is mainly done on basis of what is written in the meta-file. 
```bash
    parser.add_argument('-i', '--input_folder', required=True, help='Path to input folder. All files ending with *.txt will be parsed.')
    parser.add_argument('-o', '--output_file', required=True, help='Output file. Will overwrite it exists')
    parser.add_argument('-s', '--min_ocr_date', required=False, default='01-01-2009', help='Will drop all articles that was ocr-ed prior to this date')
    parser.add_argument('-p', '--min_publish_year', required=False, default='1814', help='Will drop all articles published prior to this year')
    parser.add_argument('-l', '--language', required=False, default='', help='If set, only articles in this language will be included')
    parser.add_argument('-L', '--unknown_language', required=False, default='', help='Any unknown language is set to this value')
    parser.add_argument('-y', '--unknown_year', required=False, default='1900', help='Any unknown year is set to this value')
    parser.add_argument('-C', '--min_confidence_article', required=False, default='0.9', help='Will drop all articles with lower average word confidence')
    parser.add_argument('-c', '--min_confidence_paragraph', required=False, default='0.8', help='Will drop all paragraphs with lower average word confidence')
    parser.add_argument('-a', '--min_words_paragraph', required=False, default='5.0', help='Minimum average number of words per paragraph in the entire article/book')
    add_bool_arg(parser, 'debug', default=False, help='Print debug info about paragraphs.')
```
For books this script can be run with the default settings to create the ppl-file.
```bash
python create_ppl.py --input_folder /source/ --output_file /ppl/myfile_ppl.txt
```
Then they can be cleaned like this:
```bash
for i in 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020; do tmux new -d -s $i "python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/ppl_2/book/book_$i.ppl --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/book/book_$i_cleaned.txt"; done;
```

For newspapers 2015-2020, the numbers of files are very large, and it might be more effective splitting in either year or months. Here is an example splitting the create script into monthly batches. Each command is run in a separate tmux:
```bash
for i in 01 02 03 04 05 06 07 08 09 10 11 12; do tmux new -d -s $i "python create_ppl.py --input_folder /home/peregil/data/text/2015/'$i'/ --output_file /home/peregil/data/output/newspapers_nonpdf_2015_'$i'_ppl.txt"; done;
```
### Public Reports
For public reports the individual files needs to be concatenated before running clean
```bash
for f in *.txt; do (cat "${f}"; echo "\n\n") >> ../../v3/ppl_2/public_reports/public_reports_ppl.txt; done
```

### Periodicals
Here is an example splitting the create script into yearly batches. Each command is run in a separate tmux:
```bash
for i in 2018 2019 2020; do tmux new -d -s books$i "python create_ppl.py --input_folder /disk4/folder1/nancy/content/text/tidsskrift/text/'$i'/ --output_file /disk4/folder1/nancy/content/text/v3/ppl_2/periodicas/periodicas_'$i'_v2_ppl.txt"; done;
```
Currently periodicas also might have to be split in months.

The following script will paralellprocess all files with clean
```bash
for f in /disk4/folder1/nancy/content/text/v3/ppl_2/periodicals/*.*; do n=${f##*/}; m=${n%_ppl.*}; tmux new -d -s $m "python clean_ppl.py --input_file '$f'  --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/periodicals/'$m'_cleaned.txt"; done
```

### Newspapers Microfilm
The following command can be used to create microfilm newspapers for some years
```bash
for y in 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 1981 1971 1961; do for i in 01 02 03 04 05 06 07 08 09 10 11 12; do tmux new -d -s micro-$y-$i "python create_ppl.py --input_folder /disk4/folder1/nancy/content/text/newspaper/mikrofilmAviser/text/'$y'/ --output_file /disk4/folder1/nancy/content/text/v3/ppl_2/newspapers_microfilm/newspapers_microfilm_'$y'_'$i'_ppl.txt";done; done
```
The following script will paralellprocess all files with clean
```bash
for f in /disk4/folder1/nancy/content/text/v3/ppl_2/newspapers_microfilm/*.*; do n=${f##*/}; m=${n%_ppl.*}; tmux new -d -s $m "python clean_ppl.py --input_file '$f'  --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers_microfilm/'$m'_cleaned.txt"; done
```

### Legal
The files are originally in ISO-8859, so we need to convert to utf8
```bash
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT lokaleforskrifter_2005.TXT -o legal_utf8/lokaleforskrifter_2005.TXT 
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT norgeslover_2005.TXT -o legal_utf8/norgeslover_2005.TXT 
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT odelsting_2005.txt -o legal_utf8/odelsting_2005.txt 
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT rtv_rundskriv_2005.TXT -o legal_utf8/rtv_rundskriv_2005.TXT 
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT rundskriv_lovavdeling_2005.TXT -o legal_utf8/rundskriv_lovavdeling_2005.TXT 
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT sentrale_forskrifter_2005.TXT -o legal_utf8/sentrale_forskrifter_2005.TXT 
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT skatt_rundskriv_2005.txt -o legal_utf8/skatt_rundskriv_2005.txt 
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT somb_rundskriv_2005.TXT -o legal_utf8/somb_rundskriv_2005.TXT 
```

Then just run standard clean on all files
```bash
python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/test_and_source_1/legal_utf8/lokaleforskrifter_2005.TXT  --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/legal/lokale.txt
```


### Wikipedia NOB and NNO
After downloading the archive from [https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/], unpack the files. You need nob.wikipedia.json and nno.wikipedia.json. In the current archive there are 492863 articles in bokmål and 139926 in nynorsk.
```bash
python create_wikipedia_ppl.py --input_file /disk2/peregil/text_meta_source_1/wikipedia_nob/nob.wikipedia.json --output_file /disk2/peregil/ppl_2/wikipedia_nob/wikipedia_nob.txt
python create_wikipedia_ppl.py --input_file /disk2/peregil/text_meta_source_1/wikipedia_nno/nno.wikipedia.json --output_file /disk2/peregil/ppl_2/wikipedia_nno/wikipedia_nno.txt
```

After this the default cleaning procedure can be run on this.
```bash
python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/peregil/ppl_2/wikipedia_nob/wikipedia_nob.txt --output_file /disk4/folder1/nancy/content/text/v3/peregil/cleaned_ppl_3/wikipedia_nob/cleaned_wikipedia_nob.txt
python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/ppl_2/wikipedia_nob/wikipedia_nno.txt --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/wikipedia_nno/cleaned_wikipedia_nob.txt
```
### Common Crawl OSCAR
The format is very close to the format we need. We only need to replace single newlines with double newlines in the deduplicated file:
```bash
sed ':a;N;$!ba;s/\n/\n\n/g' /disk4/folder1/nancy/content/text/v3/text_meta_source_1/oscar/no_dedup.txt > /disk4/folder1/nancy/content/text/v3/ppl_2/oscar_nob_ppl.txt
sed ':a;N;$!ba;s/\n/\n\n/g' /disk4/folder1/nancy/content/text/v3/text_meta_source_1/oscar/nn_dedup.txt > /disk4/folder1/nancy/content/text/v3/ppl_2/oscar_nno_ppl.txt

#Combine these files since nno is very small
echo "\n\n" > /disk4/folder1/nancy/content/text/v3/ppl_2/oscar/artbreak.txt
cat /disk4/folder1/nancy/content/text/v3/ppl_2/oscar/oscar_nob_ppl.txt /disk4/folder1/nancy/content/text/v3/ppl_2/oscar/artbreak.txt /disk4/folder1/nancy/content/text/v3/ppl_2/oscar/oscar_nno_ppl.txt > /disk4/folder1/nancy/content/text/v3/ppl_2/oscar/oscar_ppl.txt
```
Then do a simple clean:
```bash
python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/ppl_2/oscar_ppl.txt --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/oscar/oscar_cleaned.txt

```

### Online Newspapers from Språkbanken
These are in multiple files, so we first need to get them all
```bash
wget https://www.nb.no/sbfil/tekst/norsk_aviskorpus.zip
wget https://www.nb.no/sbfil/tekst/nak_2012.tar
wget https://www.nb.no/sbfil/tekst/nak_2013.tar
wget https://www.nb.no/sbfil/tekst/nak_2014.tar
wget https://www.nb.no/sbfil/tekst/nak_2015.tar
wget https://www.nb.no/sbfil/tekst/nak_2016.tar
wget https://www.nb.no/sbfil/tekst/nak_2017.tar
wget https://www.nb.no/sbfil/tekst/nak_2018.tar
wget https://www.nb.no/sbfil/tekst/nak_2019.tar

```

When the files are downloaded, they need to be unpacked.
```bash
#Unpack the archive
unzip norsk_aviscorpus.zip
for f in *.tar; do tar -xvf "$f"; done

#Delete directories 1/ and 2/
rm -rf 1/
rm -rf 2/

#Unpack the subdirectories
for f in 3/*.tar.gz; do tar -zxvf "$f"; done
for f in ????/*.tar.gz; do tar -zxvf "$f"; done

#You might delete the tar, gz and zip files at this stage but it is not necessary.
```
Note that the structure is slightly different before 2012. However, everything will be included in one large newspaper file.

```bash
python create_newspapers_online_ppl.py --input_path /disk4/folder1/nancy/content/text/v3/text_meta_source_1/newspapers_online/ --output_file /disk4/folder1/nancy/content/text/v3/ppl_2/newspapers_online/newspapers_online_ppl.txt

# You also have the option of creating separate bokmål and nynorsk files here, using these commands:
# python create_newspapers_online_ppl.py --input_path /disk4/folder1/nancy/content/text/v3/text_meta_source_1/newspapers_online/ --output_file /disk4/folder1/nancy/content/text/v3/ppl_2/newspapers_online/newspapers_online_nob_ppl.txt --language nob
# python create_newspapers_online_ppl.py --input_path /disk4/folder1/nancy/content/text/v3/text_meta_source_1/newspapers_online/ --output_file /disk4/folder1/nancy/content/text/v3/ppl_2/newspapers_online/newspapers_online_nno_ppl.txt --language nno
```
In the end you can run the default cleaning script on this:
```bash
python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/ppl_2/newspaper_online/newspapers_online_ppl.txt --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers_online/cleaned_newspapers_online.txt
# Or for the separate languages
# python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/ppl_2/newspapers_online/newspapers_online_nob_ppl.txt --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers_online/cleaned_newspapers_online_nob.txt
# python clean_ppl.py --input_file /disk4/folder1/nancy/content/text/v3/ppl_2/newspapers_online/newspapers_online_ppl_nno.txt --output_file /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers_online/cleaned_newspapers_online_nno.txt

``

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
 
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/books/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 10 --output_name books
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 5 --output_name newspapers

python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/public_reports/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name public_reports
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/wikipedia_nno/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name wikipedia_nno
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/wikipedia_nob/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name wikipedia_nob
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers_online_nno/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name newspapers_online_nno
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers_online_nob/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name newspapers_online_nob
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/oscar/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name oscar
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/digistorting/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name digistorting
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/legal/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name legal
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/periodicals/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name periodicals
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/cleaned_ppl_3/newspapers_microfilm/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --shards 1 --output_name newspaper_microfilm

# Final
python dedup_rand_shard.py --input_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/indiv_dedup/ --output_folder /disk4/folder1/nancy/content/text/v3/dedup_rand_4/complete_dedup/ --shards 500 --output_name colossal_norwegian_corpus_271120
```
Make sure to split in shards no larger than 210MB. If they are larger, you can always split later with this (splits in 10) to directory split100MB.

 ```bash
for f in *.txt; do split -d -n 10 --additional-suffix=.txt $f split100MB/${f%.*}_; done
```

## Sentence segmentation
Sentence segmentation is run on each of the N shards. The following should be run adjusted to the number of processes being no larger than the number of cores:
 ```bash
for i in {1..400}; do tmux new -d -s seg-$i "python sentence_segmentation.py -i /disk4/folder1/nancy/content/text/v3/dedup_rand_4/complete_dedup/colossal_norwegian_corpus_271120_'$i'.txt -o /disk4/folder1/nancy/content/text/v3/sentence_segm_5/";done
 ```
 ## Create tfrecords
For creating the tfrecords, we depend on covid-twitter-bert. The notram-branch allows you to run this on multiple cpu's as well as specify input and output directories.

If the shards are 100MB each, this means we are able to run on 40 cores if we have 500MB memory.

```bash
python create_pretrain_data.py --data_dir /disk4/folder1/nancy/content/text/v3/sentence_segm_5/split100MB/ --vocab_dir /disk4/folder1/nancy/content/text/v3/ --output_dir /disk4/folder1/nancy/content/text/v3/tfrecords_6/bert_multi_seq128_dup3/ --run_name notram_v1 --model_class bert_multi_cased --dupe_factor 3 --max_seq_length 128 --max_predictions_per_seq 19 --max_num_cpus 40
 ```
