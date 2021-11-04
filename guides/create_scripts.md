# Create scripts
These scripts are used for creating the json-files (2) from the source-files (1). 

## create_cc100.py
Process the CC100 corpus. Output is UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance cc100_no
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_facebook.py
Convert the WEB64 Facebook corpus to jsonl. This corpus is in json format. Output is a jsonl UTF-8 file with one post per line
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_government.py
Process the corpus downloaded from the governments API. The corpus consists of multiple files in xhtml format. Output is an UTF-8 json-lines-file with one document per line
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_lovdata_cd.py
Create jsonl from the Lovdata CD. This content does have double breaks between each artile. Some meta-info is collected from the file names. Output is an UTF-8 file with one article per line

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance cc100_no
  --input_folder INPUT_FOLDER
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_lovdata_transfer.py
Process the transferred Lovdata corpus. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_maalfrid.py
Create jsonl from mupdf-created Maalfrid documents. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance maalfrid
  --input_folder INPUT_FOLDER
                        Input folder
  --meta_file META_FILE
                        Meta file from Språkbanken in csv format
  --output_file OUTPUT_FILE
                        Output file
```

## create_mc4.py
Convert the MC4 to our json-format. This corpus is in ascii json format. Output is an UTF-8 file with one document per line
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_file INPUT_FILE
                        Input file name.
```

## create_newspapers_online.py
Processing the newspaper corpus published by Språkbanken. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input_path INPUT_PATH
                        Input path
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file
  --doc_type DOC_TYPE   Doc type
  -l LANGUAGE_REPORTED, --language_reported LANGUAGE_REPORTED
                        Language. nob, nno or . Folder names determine language.
```

## create_newspapers_pdf.py
Convert extracted plain text from mupdf to JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --input_dir input_dir
                        Input directory
  --input_dir_glob input_dir_glob
                        Input directory glob
  --output_dir output_dir
                        Output directory
  --doc_type doc_type   Document type
  --pymupdf_version pymupdf_version
                        PyMuPDF version
  --report_parsing_error report_parsing_error
                        Report filename parsing errors
    
```

## create_opensubtitles.py
Process OpenSubtitles. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_oscar.py
Process the OSCAR corpus. This corpus has one document per line. No paragraphs. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_parliament.py
Create corpus from parliament files! Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_publicreports.py
Create Public Report jsonl from downloaded text files. This corpus is formed as a document per line. No paragraphs.Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_reddit.py
Create the Reddit corpus from the downloaded archive. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --year YEAR           Selects only one year
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  -i INPUT_FOLDER, --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_twitter.py
Process the twitter corpus in json format. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance tweet
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  -i INPUT_FOLDER, --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_vgdebatt.py
Convert vgdebatt to jsonl. This corpus is originally in json format. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance tweet
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_wikipedia_download.py
Process the downloaded Wikipedia files. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no, da, sv, is or N/A
  --doc_type DOC_TYPE   For instance wikipedia_download_no
  --year YEAR           Selects only one year
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  -i INPUT_FILE, --input_file INPUT_FILE
                        Input file.
```

## create_wikipedia_huggingface_en.py
Create Wikipedia jsonl from Hugging Face. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --output_file OUTPUT_FILE
                        Output file
```

## create_wikipedia_spraakbanken.py
Process the Wikipedia dump published by Språkbanken. Output is UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doc type
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```
