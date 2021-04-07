# Status Corpus v2
This page tracks the status of version 2 of our corpus. The purpose of the table is currently to track the status. When the processing has reached at least level 4, the word count and exact size will be calculated. See level description at the bottom of this document.


## Corpora unchanged from v1
| Sources  |   Status | Level | GB text |
| -------- |   :-----|   -----:| -----:|
| Wikipedia NOB -2019  | Ready in jsonl-format. | 2| 0.9 |
| Wikipedia NNO -2019 | Ready in jsonl-format. | 2 | 0.2 |
| Newspapers Online NOB -2019 | Ready in jsonl-format. | 2 | 5.0 |
| Newspapers Online NNO -2019 |  Ready in jsonl-format.  | 2 | 0.3 |
| Common Crawl OSCAR NOB -2020 |  Ready in jsonl-format. | 2 | 4.9 |
| Common Crawl OSCAR NNO -2020 |  Ready in jsonl-format. | 2 | ? |
| Parliament Documents OCR 1814-2014 (Stortingsforhandlingene)  |  Should be copied from v1 to v2. | 0 | 5.1 |
| Public Reports OCR 1814-2020 (Evalueringsrapporter) |  Ready in jsonl-format. |2 | 0.6 |



## Corpora updated since v1
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Books OCR 1814-2021| In the first version we did delete all books OCRed before 01.01.2009. This is now rescanned in Tesseract.  | 0| More than 69.0 |
| Newspapers pdf-delivered 2008-2021| The last years several newspapers have been delivered as pdf to the library. The quality of these are a lot higher than the OCRed material. We are currently parsing these and using the pdf version if possible. We are using the PLM-list to determine if the newspapers are pdf-delivered. | 0 | Approx 20.0 |
| Newspapers OCR 1960-2021|  In v1 only 1961,1971,1981,1998-2007 from microfilm was included. We are now downloading a much larger number of newspapers. We are yet to decide exactly the starting date here. | 0| Much more than 1.8 |
| Periodicals OCR 2010-2021 |  These are tricky since the quality varies a lot. We are considering if we are going to reprocess this to increase quality and size. |0 | More than 1.9 |
| Legal Collection 1814-2021 (Lovdata CD/DVD) |  We have gotten an extended version from Lovdata. This one is larger but will not be possible to redistribute. Not yet parsed. | 0| More than 0.4|


## New corpora
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Government Documents -2021  | Large collection parsed directly from xhtml. Should just be copied over.| 0| ? |
| Parliament Documents -2021  | This needs to be followed up. | 0| ? |
| Målfrid Collection -2021  | Large collection collected by Språkbanken. We will be using the mupdf-version. Needs to be reparsed with the latest version of mupdf.| 0| ? |
| Idun Collection -2019  | Downloaded Idun data| 0| ? |
| Norart Collection -2019  | Downloaded Norart data| 0| ? |
| MC4  | We are discussing whether to add more MC4 data here| 0| ? |
| CC-100 | Monolingual Datasets from Web Crawl Data. Jan-December 2018 Commoncrawl snapshot. http://data.statmt.org/cc-100/.  | |  |
|   | - Norwegian | (2)| 50.0 |
|   | - Danish | (2) | 48.0  |
|   | - Swedish | (2) | 78.0  |
|   | - English | (2) | 301.0 |



## Processing Levels
| Level  |   Description | Format |
| -------- |   :-----|  :-----|
| 0 | The file is not yet processed/downloaded. | - | 
| 1 | Source files. For library files this is json-files, and the meta-information (OCR-quality) is used for next step processing. For the other files this is the raw downloaded file. In some cases, this step might be skipped. The main purpose of this level is to have an archive in case the original source disappears.| various |
| 2 | Jsonl-format. Previously this was **P**aragraph**P**er**L**ine-files. Documents are here a single line in the jsonl-format.| jsonl |
| 3 | Cleaned text. Text is cleaned and evaluated before this step. Paragraphs is removed here, and segments of up to 1000 words are separated by linebreaks. In v2 is this format also jsonl but without paragraphs.| jsonl |
| 4 | Deduplicated and randomised text. All sources are mixed at this stage and duplicates removed. Document per line.| txt |
| 5 | Sentence segmentation. A pre-trained [Spacy Model for Norwegian Bokmål] (https://spacy.io/models/nb)is used to segment sentences.| txt |
| 6 | Tfrecords. Tfrecord-files are generated with various vocabularies and sequence lengths.| tfrecords |


