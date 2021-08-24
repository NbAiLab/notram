# Detailed Description - Norwegian Colossal Corpus v2
This is a detailed description of the corpus. The entire corpus is heavily dedublicated and cleaned, and is saved in a standardised jsonlines-format. Part of the corpus is already publicly available. In this case you can both retrieve the corpus from the original source, or get a cleaned version from us. Please contact us if you want to train large models based on this since we might be able to give you restricted access.


| Sources  |   Description | Public status | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| **General**|  |  | **117GB** |
| Library Books 1814-2021| The main collections of books in the National Library. The majority of of the books are OCRed, with varying quality. In this version of the corpus we have reOCRed a significant part of the corpus with Tesseract, increasing the OCR quality. When cleaning, the parts with low OCR quality is dropped.   | Restricted | 60.0 |
| Library Newspapers|  Newspapers in the National Library. Contains both scanned newspapers that are OCRed or pdf-delivered newspapers post-processed by mypdf. When cleaning, the parts with low OCR quality is dropped. | Avaiting new agreement | 50 |
| Wikipedia  | Wikipediadump downloaded 20210620.| Publicly available - NB and Wikipedia. | 1.6 |
| Open Subtitles -2021  | Norwegian subtitles from OpenSubtitles. | Publicly available - NB and OpenSubtitles | 0.2 |
| Norart Collection -2019  | A collection of scientific articles. Mainly in Norwegian. | Restricted. | 0.2 |
| Online Newspapers | A Norwegian Newspaper Corpus with texts from online bokmål newspapers between 1998 and 2019 collected by Språkbanken. | Publicly available - NB and Språkbanken. | 5.0 |
| **Web**|  |  | **93GB** |
| CC-100 | Monolingual Datasets from Web Crawl Data. This is a complete Jan-December 2018 Common Crawl snapshot. | Publicly availble from NB and http://data.statmt.org/cc-100/. | 24.0 |
| OSCAR -2020 |  OSCAR or Open Super-large Crawled Aggregated coRpus is a huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus using the goclassy architecture. The original file is roughly 10 x bigger, but is duplicated in CC-100 and MC-4. | Publicly available from NB and multiple other sources.  | 0.5 |
| MC4  | The complete MC4 corpus used for training T5. AllenAI has preprocessed this and made it availbale on Huggingface. Filtering of the MC4 is complicated, and the quality of this corpus might be lower than the other corpora in this collection. | Publicly available both from NB and Huggingface| 68.0 |
| **Social Media**|  |  | **25GB** |
| Facebook | Large collection of Norwegian Facebook-posts collected by Web64. The archive is maintained until 2018. | Restricted | 3.9 |
| Reddit  | A collection of around 500k Norwegian Reddit posts between 2005-2019. Only posts with more than 20 characters and with a 0.7 confidence of Norwegian are included.  | Publicly availble from NB or http://files.pushshift.io/reddit/comments/ | 0.2 |
| Twitter Top | Collection of tweets from the top 10.000 Norwegian tweeters between 2016 and 2018. Collected by Web64. | Restricted| 5.9 |
| Twitter News | Collection of tweets from StoryBoard. Comments to Norwegian news articles. Collected by Web64. | Restricted| 0.3 |
| VGDebatt  | A download of all posts from VGD since they started around 1998 until 2021.| Restricted| 15.0 |
| **Byrocratic**|  |  | **22GB** |
| Government Documents  | Large collection with exceptional very quality parsed directly from xhtml.| 2| 0.1 |
| Parliament Documents  |  Also referred to as Stortingsforhandlingene. Collection of documents from the Norwegian Parliament. The corpus contains mainly OCRed reports. Part of the collection at the National Library. | Public from NB | 8.1 |
| Public Reports OCR 1814-2020 (Evalueringsrapporter) |  Collection of public report from the National Library. |2 | 0.6 |
| Lovdata CD |  CD/DVD last published in 2005. Contains a very complete collection of legal resources, including laws, verdicts, NOUs etc. This is now totally out of copyright. | Public from NB | 0.4 |
| Lovdata Transfer |  A more updated corpus delivered directly from Lovdata. It contains smaller shunks of data. | Restricted | 0.3 |
| Målfrid Collection -2021  | A collection of more than 9.2M public documents in pdf-format from 311 different sources. Collected from Språkbanken. We are using the part that is possible to read as text (more than 95% of the corpus). The largest sources are ssb (1.5M), regjeringen (1M), Uio (1M), fylkesmannen (0.7M), nve (0.4M), ntnu (0.3M), patentstyret (0.2M), vegvesenen (0.2M), fhi (0.2M).| 2| 11.0 |



## Non Norwegian corpora
| Sources  |   Status | Level | Estimated GB text |
| -------- |   :-----|   -----:| -----:|
| CC-100 | Monolingual Datasets from Web Crawl Data. Jan-December 2018 Commoncrawl snapshot. http://data.statmt.org/cc-100/.  | |  |
|   | - Danish | 2 | 48.0  |
|   | - Swedish | 2 | 78.0  |
|   | - English | 2 | 301.0 |
| Reddit 2005 - 2019 | A collection of Reddit posts. Only posts with more than 20 characters and with a 0.7 confidence of target language are included. Source: http://files.pushshift.io/reddit/comments/. The last step in converting this to our json-format is not completed for English since it is unlikely that it will be used. | |  |
|   | - Danish | 2 | 0.5  |
|   | - Swedish | 2 | 0.9  |
|   | - English | 2 | Approx 1000.0|
| Wikipedia EN -2020  | Wikipedia. From the HuggingFace datasets. Downloaded  downloaded May 2020| (2)| 17.0 |


## Processing Levels
The base format
| Level  |   Description | Format |
| -------- |   :-----|  :-----|
| 1 | Source files. For library files this is json-files, and the meta-information (OCR-quality) is used for next step processing. For the other files this is the raw downloaded file. In some cases, this step might be skipped. The main purpose of this level is to have an archive in case the original source disappears.| various |
| 2 | Jsonl-format. Documents are here a single line in the jsonl-format.| jsonl |
| 3 | Cleaned jsonl. Text is cleaned and evaluated before this step. Each paragraph is deduplicated on file-level. Then newlines/paragraphs are removed. Articles no logner than 1000 words. At this stage we drop a lot of meta-information that is attached to each of the documents. | jsonl |
| 4 | Deduplicated jsonl. Sources are mixed at this stage and duplicates removed. Document per line.| jsonl |



