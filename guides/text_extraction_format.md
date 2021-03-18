# Text Extraction Format
Specification for the internal format used when extracting text from OCR documents. It allows for storing the relevant information from METS/ALTO for further processing.

```json
"urn": "digibok_2006080900001" # Comments
"publish_year": "1929" # 4 digits year
"language_reported": "nob" #3-letter language code
"language_detected": "nob" #3-letter language code
"docworks_version": "6.5-1.28" #Text reported in METS/ALTO
"abbyy_version": "8.1" #Text reported in METS/ALTO
"document_word_confidence": "0.9" #Float 0-1. Average calculated while processing. 
"document_word_98_confidence": "0.56" #Float 0-1. Percentage above 0.98 confidence. Calculated while processing 
"paragraphs":   "id": "1" #Integer. Starting on 0
                "confidence": "0.36" #Float 0-1. From METS/ALTO
                "text": "text goes here" #utf8-encoded-text
```
