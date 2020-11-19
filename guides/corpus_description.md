# Colossal Norwegian Corpus
The Colossal Norwegian Corpus consists of both publicly available sources and of sources that is handed over to the National Library of Norway in compliance with ["pliktavleveringslova"](https://lovdata.no/dokument/NL/lov/1989-06-09-32) - a Norwegian law that requires all published materials to be sent to the library so it can be made available for research and documentation. 


## Main Sources
### Norwegian National Library
The copyright issues of this part of the corpus needs to be cleared with Kopinor before publishing
* **Books** - Published between 1814 and 2020. OCR quality of books scanned between 2006 and 2008 have fairly low quality. Only books scanned from 2009 are included included. A rough estimate is that more than 50% of all published books in Norway is included.
* **Newspapers Paper** - Published between 2015 and 2020. 
* **Newspapers Pdf** - Published between 2015 and 2020. 
* **Newspapers Microfilm** - Published between 2015 and 2020. 
* **Periodicals** - Published between ??. A wide range of periodicas and yearbooks. Mostly OCR scans.
* **Legal** - LovData CD (200?) and LovData DVD (200?). This is a complete collection of all verdicts prior to these dates. The collection is originally OCR scanned but after that manually corrected.


### Public Sources
This part of the corpus can be downloaded directly. The rights to redistribute the cleaned versions needs to be cleared.
* **Wikipedia NOB** - [Norwegian Wikipedia Bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/) downloaded March 2019 and published by Språkbanken. Nynorsk and Bokmål are published in the same file.
* **Wikipedia NNO** - [Norwegian Wikipedia Nynorsk](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/) downloaded March 2019 and published by Språkbanken. Nynorsk and Bokmål are published in the same file.
* **Newspapers Online NOB** - A [Norwegian Newspaper Corpus](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-4/) with texts from online bokmål newspapers between 1998 and 2019 collected by Språkbanken. 
* **Newspapers Online NNO** - A [Norwegian Newspaper Corpus](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-4/) with texts from online nynorsk newspapers between 1998 and 2019 collected by Språkbanken. 
* **MC4** - The Norwegian part of the [Multilingual Colossal Clean Crawled Corpus](https://www.tensorflow.org/datasets/catalog/c4?hl=en) published by Google in cooperation with Common Crawl. This is the Norwegian part of the corpus used to train T5 in 2020. More details about how this archive is processed is available in [this article](https://github.com/NBAiLab/notram/blob/master/guides/prepare_common_crawl.md).
* **Norwegian Government Reports** - Collected by the Norwegian National Library from?
* **Parliament Archives** - Collected by the Norwegian National Library from?


## Processing Steps
1. Source files. For library files this is txt/meta-files, and the meta-information (OCR-quality) is used for next step processing. For the other files this is the raw downloaded file.
2. **P**aragraph**P**er**L**ine-files. Articles are separated by double line breaks, paragraphs with single linebreaks.
3. Cleaned text. Text is cleaned and evaluated before this step. Paragraphs is removed here, and segments of up to 1000 words are separated by linebreaks.
4. Deduplicated and randomised text. All sources are mixed at this stage and duplicates removed.
5. Sentence segmentation. A pre-trained [Spacy Model for Norwegian Bokmål] (https://spacy.io/models/nb)is used to segment sentences.
6. Tfrecords. Tfrecord-files are generated with various vocabularies and sequence lengths.


## Corpus Size
### Billion Words
| Sources  |  PPL (2) | Cleaned (3) |
| -------- |  -----:|  -----:| 
| Books  | 11.89 | 11.82 | 
| Newspapers | - | - | 
| Periodicals  | - |  - |
| Legal  | - |  - |
| Wikipedia NOB  | 0.146 |  0.140 | 
| Wikipedia NNO  | 0.033 |  0.034 | 
| Newspapers Online NOB | 0.730 |  0.732 |
| Newspapers Online NNO | 0.047 |  0.047 |
| MC4  | - |  - | 
| Norwegian Government Reports  | 0.806 |  - | 
| Parliament Archives  | - |  - | 
| **Total**  |**-** |  **-** |


### Size in Gb
| Sources  |  PPL (2) | Cleaned (3) |
| -------- |  -----:|  -----:| 
| Books  | 69.0 | 68.0 | 
| Newspapers | - | - | 
| Periodicals  | - |  - |
| Legal  | - |  - |
| Wikipedia NOB  | 1.0 |  0.9 | 
| Wikipedia NNO  | 0.2 |  0.2 | 
| Newspapers Online NOB | 4.3 |  4.4 |
| Newspapers Online NNO | 0.3 |  0.3 |
| MC4  | - |  - | 
| Norwegian Government Reports  | 5.1 |  - | 
| Parliament Archives  | - |  - | 
| **Total**  |**-** |  **-** |


### Total Corpus Size
| Sources  |  Cleaned (3) | Deduplicated (4/5) | Tfrecord dupe=1 (6) |
| -------- |  -----:|  -----:| -----:| 
| Words (Billion)  | - | - | - | 
| Size (Gb) | - | - | - |


