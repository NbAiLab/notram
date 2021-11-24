# JSON Format
Specification for the internal format used when extracting text from OCR documents. It allows for storing the relevant information from METS/ALTO for further processing.

## Book example (one for each book)
```bash
"id": "digibok_2006080900001" # The original digibook id - have to be unique for each jsonl line
"doc_type": "book" # The type of material. Newspaper or book
"ocr_date": "20191224" #Date for scanning in the format yyyymmdd. Set to N/A if not in mods post.
"publish_date": "20190101" # Date for publication. For books this is set to 0101 for the publication year. Set to N/A if not in mods post.
"language_reported": "nob" #3-letter language code. nob for Bokmål and nno for Nynorsk. Only reported for books in METS/ALTO. 
"language_detected": "nob" #3-letter language code
"tesseract_version": "4.1.1" #If Tesseract is used for scanning
"docworks_version": "6.5-1.28" #Text reported in METS/ALTO
"abbyy_version": "8.1" #Text reported in METS/ALTO
"document_word_confidence": 0.9 #Float 0-1. Average calculated while processing. 
"page": 1 #Page number - From in METS/ALTO - If documents are divided into one document per page
"paragraphs":   "paragraph_id": 1 #Integer. Starting on 0. Counted during processing.
                "page": 1 #Page number - From in METS/ALTO - if entire book is one document
                "block": 1 #Block number on current page - From in METS/ALTO
                "confidence": 0.36 #Float 0-1. From METS/ALTO
                "text": "text goes here" #utf8-encoded-text
```


## Newspaper example (one for each article)
```bash
"id": "aftenposten_null_null_20190102_160_1_1-2_007_bilag_ARTICLE316" # Reference to the exact article
"doc_type": "newspaper_ocr" # The type of material. Newspaper or book
"ocr_date": "20191224" #Date for OCR in the format yyyymmdd
"publish_date": "20190101" # Date for publication. 
"language_detected": "nob" #3-letter language code
"docworks_version": "6.5-1.28" #Text reported in METS/ALTO
"abbyy_version": "8.1" #Text reported in METS/ALTO
"title": "article title" #Article title. Can be the same for multiple blocks
"document_word_confidence": 0.9 #Float 0-1. Average calculated while processing. 
"paragraphs":   "paragraph_id": 1 #Integer. Starting on 0. Counted during processing.
                "page": 1 #Page number -  From in METS/ALTO
                "confidence": 0.36 #Float 0-1. From METS/ALTO
                "text": "text goes here" #utf8-encoded-text
```

## External files (one for each document)
```bash
"id": "wikipedia_nob_007" # Typically referring to line number in the original source. Can contain letters.
"doc_type": "wikipedia" # The type of material. Newspaper or book
"language_reported": "nob" #3-letter language code. nob for Bokmål, nno for Nynorsk and no for unspecified Norwegian. Set to N/A if not specified.
"language_detected": "nob" #3-letter language code. Can be set to N/A or dropped if this is not done.
"paragraphs":   "paragraph_id": 1 #Integer. Starting on 0. Counted during processing.
                "text": "text goes here" #utf8-encoded-text
```
