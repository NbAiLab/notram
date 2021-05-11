# Status Corpus v2
This page tracks the status of version 2 of our corpus. The purpose of the table is currently to track the status. When the processing has reached at least level 4, the word count and exact size will be calculated. See level description at the bottom of this document.


## Corpora unchanged from v1
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Wikipedia NOB -2019  | Wikipediadump downloaded March 2019 and published by Språkbanken. Nynorsk and Bokmål are published in the same file. This is the extracted bokmål version.| 2| 0.9 |
| Wikipedia NNO -2019 | Same as above. This is the extracted nynorsk version.| 2 | 0.2 |
| Newspapers Online NOB -2019 | A Norwegian Newspaper Corpus with texts from online bokmål newspapers between 1998 and 2019 collected by Språkbanken. | 2 | 5.0 |
| Newspapers Online NNO -2019 |  A Norwegian Newspaper Corpus with texts from online nynorsk newspapers between 1998 and 2019 collected by Språkbanken.  | 2 | 0.3 |
| Common Crawl OSCAR NOB -2020 |  OSCAR or Open Super-large Crawled Aggregated coRpus is a huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus using the goclassy architecture. | 2 | 4.9 |
| Common Crawl OSCAR NNO -2020 |  Same as above in nynorsk.| 2 | 0.1 |
| Parliament Collection OCR 1814-2014 (Stortingsforhandlingene)  |  Collection of documents from the Norwegian Parliament. Part of the collection at the National Library. | 1 | 5.1 |
| Public Reports OCR 1814-2020 (Evalueringsrapporter) |  Collection of public report from the National Library. |2 | 0.6 |
| Lovdata CD -2005 |  CD/DVD last published in 2005. Contains a very complete collection of legal resources, including laws, verdicts, NOUs etc. This is now totally out of copyright. | 2 | 0.4 |


## Corpora updated since v1
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Books OCR 1814-2021| The books OCRed by DocWorks prior to 01.01.2009 had so low quality that it is reOCRed with Tesseract.  | 2 | 184.0 |
|  | DocWorks - All books OCRed with DocWorks after 01.01.2009.| 2 | (144.0) |
| | Tesseract - Books OCRed with Tesseract in 2021.   | 2 | (40.0) |
| Newspapers|  Newspapers in the National Library. Either scanned newspapers that are OCRed or pdf-delivered newspapers processed by mypdf. |  | 280.0 |
| |  1940-1949 - Docworks OCR-scanned newspapers | 2 | (42.0) |
| | 1950-1959 - Docworks OCR-scanned newspapers | 2 | (7.4) |
| | 1960-1969 - Docworks OCR-scanned newspapers | 2 | (30.0) |
|  | 1970-1979 - Docworks OCR-scanned newspapers | 2 | (18.0) |
|   | 1980-1989 - Docworks OCR-scanned newspapers | 2 | (15.0) |
| | 1990-1999 - Docworks OCR-scanned newspapers | 2 | (20.0) |
|  | 2000-2010 - Mainly Docworks OCR-scanned newspapers | 2 | (51.4) |
|  | 2010-2019 - Mix of OCR-scanned and pdf-delivered newspapers | 2 | (78.0) |
|  | 2020-2019 - Mainly pdf-delivered newspapers| 2 | (10.0) |
| Lovdata Transfer |  We have gotten an extended version of the data from Lovdata. This one is larger but will not be possible to redistribute without agreement with Lovdata. The document is on paragraph level. Transferred but not parsed. | 2 | 3.8|
| Government Documents NOB -2021  | Large collection with exceptional high quality parsed directly from xhtml.| 2| 0.7 |
| Government Documents NNO -2021  | As above, but in Nynorsk. | 2| 0.1 |
| Målfrid Collection -2021  | A collection of more than 9.2M public documents in pdf-format from 311 different sources. Collected from Språkbanken. We are using the part that is possible to read as text (more than 95% of the corpus). The largest sources are ssb (1.5M), regjeringen (1M), Uio (1M), fylkesmannen (0.7M), nve (0.4M), ntnu (0.3M), patentstyret (0.2M), vegvesenen (0.2M), fhi (0.2M).| 2| 19.0 |
| Idun Collection -2019  | Downloaded Idun data| 0| ? |
| Norart Collection -2019  | Downloaded Norart data| 0| ? |
| CC-100 | Monolingual Datasets from Web Crawl Data. Jan-December 2018 Commoncrawl snapshot. http://data.statmt.org/cc-100/. All files are downloaded. Conversion to jsonl format is running on Dante. | |  |
|   | - Norwegian | 2| 50.0 |


## Non Norwegian corpora
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| CC-100 | Monolingual Datasets from Web Crawl Data. Jan-December 2018 Commoncrawl snapshot. http://data.statmt.org/cc-100/. All files are downloaded. Conversion to jsonl format is running on Dante. | |  |
|   | - Danish | 2 | 48.0  |
|   | - Swedish | 2 | 78.0  |
|   | - English | 2 | 301.0 |


## Unlikely to be included
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| Twitter archive | An attempt at trying to extract Norwegian tweets from the Internet Archive. | 0| 0 |
| MC4  | We waiting for email regarding if it is possible to get more MC4 data from other places.| 0| 0 |
| Social Media  | SAB is waiting for reply to email from Twitter. Not likely at the moment.| 0| 0 |
| Parliament Documents -2021  | This needs to be followed up. SAB. | 0| 0 |
| Periodicals OCR 2010-2021 |  We have reOCRed this with Tesseract but quality seem to be too low compared to the rest of our sorpus. | 0 | More than 1.9 |


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


