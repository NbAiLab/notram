# Norwegian Corpus

## Norwegian National Library
The copyright issues of this part of the corpus needs to be cleared with Kopinor before publishing
* **Books** - Published between 1814 and 2020. OCR quality of books scanned between 2006 and 2008 have fairly low quality. Only books scanned from 2009 are included included. A rough estimate is that around 75% of all publicly available books in Norway is included.
* **Newspapers** - Published between 2015 and 2020. A collection of pdf-files and scans from microfilm.
* **Periodicals** - Published between ??. A wide range of periodicas and yearbooks. Mostly OCR scans.
* **Legal** - LovData CD (200?) and LovData DVD (200?). This is a complete collection of all verdicts prior to these dates. The collection is originally OCR scanned but after that manually corrected.


## External Sources
This part of the corpus can be downloaded directly. The rights to redistribute the cleaned versions needs to be cleared.
* **Wikipedia NOB** - [Norwegian Wikipedia Bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/) downloaded March 2019 and published by Språkbanken. Nynorsk and Bokmål is published in the same file.
* **Wikipedia NON** - [Norwegian Wikipedia Nynorsk](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/) downloaded March 2019 and published by Språkbanken. Nynorsk and Bokmål is published in the same file.
* **Newspapers Språkbanken** - A [Norwegian Newspaper Corpus](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-4/) with texts between 1998 and 2019 collected by Språkbanken. 
* **M4C** - The Norwegian part of the Multilingual Common Crawl Corpus Collection published by TFHub. The same corpus as the one used to train T5 in 2020
* **Norwegian Government Reports** - Collected by the Norwegian National Library


## Processing Steps
1. Source files. For library files this is txt/meta-files, and the meta-information (OCR-quality) is used for next step processing. 
2. **P**aragraph**P**er**L**ine-files. Articles are separated by double line breaks, paragraphs with single linebreaks.
3. Cleaned text. Text is cleaned and evaluated before this step.
4. Deduplicated and randomised text. All sources are mixed at this stage and duplicates removed.
5. Sentence segmentation. Spacy is used to segment sentences.
6. Tfrecords. Tfrecord-files are generated with various vocabularies and sequence lengths.


## Billion Words in Corpus
| Sources  |  PPL (2) | Cleaned (3) |
| -------- |  -----:|  -----:| 
| Books  | 15.12 | 14.99 | 
| Newspapers | - | - | 
| Periodicals  | - |  - |
| Legal  | - |  - |
| Wikipedia NOB  | - |  - | 
| Wikipedia NON  | - |  - | 
| Newspapers Språkbanken | - |  - |
| M4C  | - |  - | 
| Norwegian Government Reports  | - |  - | 
| **Total**  |**-** |  **-** |


## Size of Corpus in Gb
| Sources  |  PPL (2) | Cleaned (3) |
| -------- |  -----:|  -----:| 
| Books  | 87 | 86 | 
| Newspapers | - | - | 
| Periodicals  | - |  - |
| Legal  | - |  - |
| Wikipedia NOB  | - |  - | 
| Wikipedia NON  | - |  - | 
| Newspapers Språkbanken | - |  - |
| M4C  | - |  - | 
| Norwegian Government Reports  | - |  - | 
| **Total**  |**-** |  **-** |


## Total Corpus Size
| Sources  |  Cleaned (3) | Deduplicated (4/5) | Tfrecord dupe=1 (6) |
| -------- |  -----:|  -----:| -----:| 
| Words  | - | - | - | 
| Size (Gb) | - | - | - |


## Status
| Sources  |  Level (in progress) | Responsible for next step |
| -------- |  -----:|  -----:| 
| Books  | 3 | PE | 
| Newspapers | (1) | F | 
| Periodicals  | (1) |  F |
| Legal  | - |  SA |
| Wikipedia NOB  | (1) |  PE | 
| Wikipedia NON  | (1) |  PE | 
| Newspapers Språkbanken | (1) |  PE |
| M4C  | (1) |  J | 
| Norwegian Government Reports  | - |  SA | 



