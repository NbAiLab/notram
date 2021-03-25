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
python create_wikipedia_jsonl.py --doctype wikipedia --language_reported nno --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/wikipedia_nno/nno.wikipedia.json --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/wikipedia_nno.jsonl
python create_wikipedia_jsonl.py --doctype wikipedia --language_reported nob --input_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/source_1/wikipedia_nob/nob.wikipedia.json --output_file /nfsmounts/meta2/disk4/folder1/nancy/content/text/v2/jsonl_2/wikipedia_nob.jsonl
````