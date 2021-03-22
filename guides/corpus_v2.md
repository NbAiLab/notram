# Status Corpus v2
This page tracks the status of version 2 of our corpus. The purpose of the table is currently to track the status. When the processing has reached at least level 4, the, number of words and exact size will be calculated. See level description at the bottom of this document.


## Corpora unchanged from version 1
| Sources  |   Status | Level | GB text |
| -------- |   :-----|   -----:| -----:|
| Wikipedia NOB -2019  | Should be copied from v1 to v2.| 0| 0.9 |
| Wikipedia NNO -2019 | Should be copied from v1 to v2. | 0 | 0.2 |
| Newspapers Online NOB -2019 | Should be copied from v1 to v2.| 0 | 4.0 |
| Newspapers Online NNO -2019 |  Should be copied from v1 to v2.| 0 | 0.3 |
| Common Crawl OSCAR -2020 |  Should be copied from v1 to v2. | 0 | 4.9 |
| Parliament Documents OCR 1814-2014 (Stortingsforhandlingene)  |  Should be copied from v1 to v2. | 0 | 5.1 |
| Public Reports OCR 1814-2020 (Evalueringsrapporter) |  Should be copied from v1 to v2. |0 | 0.6 |



## Corpora revised from version 1
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Books OCR 1814-2020| In the first version we did delete all books OCRed before 01.01.2009. This is now rescanned in Tesseract.  | 0| More than 69.0 |
| Newspapers Pdf delivered 2015(?)-2020| The last years several newspapers have been delivered as pdf to the library. The quality of these are a lot higher than the OCRed material. We are currently parsing these and using the pdf version if possible.| 0 | More than 20.0 |
| Newspapers OCR 1960-2020(?)|  In version 1 only 1961,1971,1981,1998-2007 from microfilm was included. We are now downloading a much larger number of newspapers after 1960.| 0| More than 1.8 |
| Periodicals OCR 2010-2020 |  ?|0 | More than 1.9 |
| Legal Collection 1814-2004 (Lovdata CD/DVD) |  We have gotten an extended version from Lovdata. This one is larger but will not be possible to redistribute. Not yet parsed. | 0| More than 0.4|


## New corpora
| Sources  |   Status | Level | GB text |
| -------- |   :-----|   -----:| -----:|
| Government Documents -2021  | Large collection parsed directly from xhtml. Should just be copied over.| 0| ? |
| Målfrid Collection -2021  | Large collection collected by Språkbanken. We will be using the mupdf-version. Needs to be reparsed with the latest version of mupdf.| 0| ? |




## Processing Levels
| Level  |   Description |
| -------- |   :-----|
| 0 | The file is not yet processed/downloaded. |
| 1 | Source files. For library files this is json-files, and the meta-information (OCR-quality) is used for next step processing. For the other files this is the raw downloaded file. In some cases, this step might be skipped.|
| 2 | Jsonl-format. Previously this was **P**aragraph**P**er**L**ine-files. Documents are here a single line in the jsonl-format.|
| 3 | Cleaned text. Text is cleaned and evaluated before this step. Paragraphs is removed here, and segments of up to 1000 words are separated by linebreaks. This is a text only format where documents are separated by double line breaks... Or is it?? Freddy?|
| 4 | Deduplicated and randomised text. All sources are mixed at this stage and duplicates removed.|
| 5 | Sentence segmentation. A pre-trained [Spacy Model for Norwegian Bokmål] (https://spacy.io/models/nb)is used to segment sentences.|
| 6 | Tfrecords. Tfrecord-files are generated with various vocabularies and sequence lengths.|


