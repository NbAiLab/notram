# Status Corpus v2
This page tracks the status of version 2 of our corpus. The purpose of the table is currently to track the status. When the processing has reached at least level 4, the word count and exact size will be calculated. See level description at the bottom of this document.


## Corpora unchanged from v1
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Wikipedia NOB -2019  | Ready in jsonl-format. | 2| 0.9 |
| Wikipedia NNO -2019 | Ready in jsonl-format. | 2 | 0.2 |
| Newspapers Online NOB -2019 | Ready in jsonl-format. | 2 | 5.0 |
| Newspapers Online NNO -2019 |  Ready in jsonl-format.  | 2 | 0.3 |
| Common Crawl OSCAR NOB -2020 |  Ready in jsonl-format. | 2 | 4.9 |
| Common Crawl OSCAR NNO -2020 |  Ready in jsonl-format. | 2 | 0.1 |
| Parliament Collection OCR 1814-2014 (Stortingsforhandlingene)  |  Should be copied from v1 to v2. | 1 | 5.1 |
| Public Reports OCR 1814-2020 (Evalueringsrapporter) |  Ready in jsonl-format. |2 | 0.6 |
| Lovdata CD -2005 |  Copied from v1 | 1 | 0.4 |


## Corpora updated since v1
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Books OCR 1814-2021| In the first version we did delete all books OCRed before 01.01.2009. This is now rescanned in Tesseract.  | (1) | More than 69.0 |
| Newspapers pdf-delivered 2008-2021| The last years several newspapers have been delivered as pdf to the library. The quality of these are a lot higher than the OCRed material. We are currently parsing these and using the pdf version if possible. We are using the PLM-list to determine if the newspapers are pdf-delivered. | 0 | Approx 20.0 |
| Newspapers OCR 1960-2021|  In v1 only 1961,1971,1981,1998-2007 from microfilm was included. We are now downloading a much larger number of newspapers. We are yet to decide exactly the starting date here. | 0| Much more than 1.8 |
| Periodicals OCR 2010-2021 |  These are tricky since the quality varies a lot. We are now reprocessing this with Tesseract to increase quality and size.  | 0 | More than 1.9 |
| Lovdata Transfer |  We have gotten an extended version of the data from Lovdata. This one is larger but will not be possible to redistribute without agreement with Lovdata. The document is on paragraph level. Transferred but not parsed. | 1 | 2.5|


## New corpora
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Government Documents NOB -2021  | Large collection parsed directly from xhtml.| 2| 0.7 |
| Government Documents NNO -2021  | As above, but in Nynorsk. | 2| 0.1 |
| Målfrid Collection -2021  | A collection of more than 9.2M public documents in pdf-format from 311 different sources. Collected from Språkbanken. We are using the part that is possible to read as text (more than 95% of the corpus). The largest sources are ssb (1.5M), regjeringen (1M), Uio (1M), fylkesmannen (0.7M), nve (0.4M), ntnu (0.3M), patentstyret (0.2M), vegvesenen (0.2M), fhi (0.2M).| 2| 19.0 |
| Idun Collection -2019  | Downloaded Idun data| 0| ? |
| Norart Collection -2019  | Downloaded Norart data| 0| ? |
| CC-100 | Monolingual Datasets from Web Crawl Data. Jan-December 2018 Commoncrawl snapshot. http://data.statmt.org/cc-100/. All files are downloaded. Conversion to jsonl format is running on Dante. | |  |
|   | - Norwegian | 2| 50.0 |
|   | - Danish | 2 | 48.0  |
|   | - Swedish | 2 | 78.0  |
|   | - English | (2) | 301.0 |


## Unlikely to be included
| Sources  |   Status | Level | Estimated GB text |
| MC4  | We waiting for email regarding if it is possible to get more MC4 data from other places.| 0| 0 |
| Social Media  | SAB is waiting for reply to email from Twitter. Not likely at the moment.| 0| 0 |
| Parliament Documents -2021  | This needs to be followed up. SAB. | 0| 0 |


## Processing Levels
| Level  |   Description | Format |
| -------- |   :-----|  :-----|
| 0 | The file is not yet processed/downloaded. | - | 
| 1 | Source files. For library files this is json-files, and the meta-information (OCR-quality) is used for next step processing. For the other files this is the raw downloaded file. In some cases, this step might be skipped. The main purpose of this level is to have an archive in case the original source disappears.| various |
| 2 | Jsonl-format. Previously this was **P**aragraph**P**er**L**ine-files. Documents are here a single line in the jsonl-format.| jsonl |
| 3 | Cleaned text. Text is cleaned and evaluated before this step. Each paragraph is deduplicated on file-level. Then newlines/paragraphs are removed. Articles no logner than 1000 words. Similar to level 2 jsonl-format, but no paragraphs exists.| jsonl |
| 4 | Deduplicated and randomised text. All sources are mixed at this stage and duplicates removed. Document per line.| txt |
| 5 | Sentence segmentation. A pre-trained [Spacy Model for Norwegian Bokmål] (https://spacy.io/models/nb) is used to segment sentences.| txt |
| 6 | Tfrecords. Tfrecord-files are generated with various vocabularies and sequence lengths.| tfrecords |


