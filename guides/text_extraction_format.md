# Text Extraction Format
Specification for the internal format used when extracting text from OCR documents. It allows for storing the relevant information from METS/ALTO for further processing.

```json
"urn": "digibok_2006080900001" # Comments
"publish_year": "1929" # 4 digits
"language_reported": "nob" #3-letter language code
"language_detected": "nob" #3-letter language code
"docworks_version": "6.5-1.28" #Text reported in METS/ALTO
"abbyyVersion": "8.1" 
"bookOcrWordconfidence": "0.9"
"percentageWords98confidence": "0.56"
"averageNumberOfWordsPerParagraph": "101.2"
"paragraphs":   "id": "P1_TB00001"
                "confidence": "0.36"
                "text": "text goes here"
```
