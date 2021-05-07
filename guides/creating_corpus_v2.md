# Creating the Norwegian Corpus v2
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

## Create jsonl-files
### External sources

```bash
python create_newspapers_online_jsonl.py --doc_type newspapers_online --language_reported nno --input_path /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/newspapers_online/ --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/newspapers_online_nno.jsonl &&
python create_newspapers_online_jsonl.py --doc_type newspapers_online --language_reported nob --input_path /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/newspapers_online/ --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/newspapers_online_nob.jsonl &&
python create_wikipedia_jsonl.py --doc_type wikipedia --language_reported nno --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/wikipedia_nno/nno.wikipedia.json --output_file  /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/wikipedia_nno.jsonl &&
python create_wikipedia_jsonl.py --doc_type wikipedia --language_reported nob --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/wikipedia_nob/nob.wikipedia.json --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/wikipedia_nob.jsonl &&
python create_oscar_jsonl.py --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/oscar/nn_dedup.txt --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/oscar_nno.jsonl --doc_type oscar --language_reported nno &&
python create_oscar_jsonl.py --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/oscar/no_dedup.txt --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/oscar_nob.jsonl --doc_type oscar --language_reported nob &&
python create_publicreports_jsonl.py --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/publicreports/ --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/public_reports.jsonl --doc_type publicreport &&

python create_government_jsonl.py --input_folder /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/government/xhtml/nb/ --language_reported nbo --doc_type government --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/government_nbo.jsonl
python create_government_jsonl.py --input_folder /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/government/xhtml/nn/ --language_reported nno --doc_type government --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/government_nno.jsonl
python create_government_jsonl.py --input_folder /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/government/xhtml/en/ --language_reported en --doc_type government --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/government_en.jsonl

# First converted to utf8 by using this command
# iconv -f ISO-8859-1 data.txt -t UTF-8 -o data_utf8.txt
python create_lovdata_transfer_jsonl.py --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/lovdata_transfer/data_utf8.txt --doc_type lovdata_transfer --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/lovdata_transfer.jsonl


````
