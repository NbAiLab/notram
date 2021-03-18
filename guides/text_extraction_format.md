# Text Extraction Format
Specification for the internal format used when extracting text from OCR documents. It allows for storing the relevant information from METS/ALTO for further processing.

## Book example (one for each book)
```bash
"urn": "digibok_2006080900001" # The original digibook id
"scan_date": "20191224" #Date for scanning in the format yyyymmdd
"publish_date": "20190101" # Date for publication. For books this is set to 0101 for the publication year
"language_reported": "nob" #3-letter language code. nob for Bokmål and nno for Nynorsk. Only reported for books in METS/ALTO. 
"language_detected": "nob" #3-letter language code
"docworks_version": "6.5-1.28" #Text reported in METS/ALTO
"abbyy_version": "8.1" #Text reported in METS/ALTO
"document_word_confidence": "0.9" #Float 0-1. Average calculated while processing. 
"document_word_98_confidence": "0.56" #Float 0-1. Percentage above 0.98 confidence. Calculated while processing 
"paragraphs":   "id": "1" #Integer. Starting on 0. Counted during processing.
                "page": "1" #Page number - From in METS/ALTO
                "block": "1" #Block number on current page - From in METS/ALTO
                "confidence": "0.36" #Float 0-1. From METS/ALTO
                "text": "text goes here" #utf8-encoded-text
```


## Newspaper example (one for each article)
```bash
"urn": "aftenposten_null_null_20190102_160_1_1-2_007_bilag_ARTICLE316" # The original digibook id
"scan_date": "20191224" #Date for scanning in the format yyyymmdd
"publish_date": "20190101" # Date for publication. 
"language_reported": "nob" #3-letter language code. nob for Bokmål and nno for Nynorsk. Set to N/A for newspapers since it is not reported in METS/ALTO
"language_detected": "nob" #3-letter language code
"docworks_version": "6.5-1.28" #Text reported in METS/ALTO
"abbyy_version": "8.1" #Text reported in METS/ALTO
"document_word_confidence": "0.9" #Float 0-1. Average calculated while processing. 
"document_word_98_confidence": "0.56" #Float 0-1. Percentage above 0.98 confidence. Calculated while processing 
"paragraphs":   "id": "1" #Integer. Starting on 0. Counted during processing.
                "page": "1" #Page number -  From in METS/ALTO
                "block": "1" #Block number on current page - From in METS/ALTO
                "confidence": "0.36" #Float 0-1. From METS/ALTO
                "text": "text goes here" #utf8-encoded-text
```

