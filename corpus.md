# Colossal Norwegian Corpus
The Colossal Norwegian Corpus consists of both publicly available sources and of sources that is handed over to the National Library of Norway in compliance with ["pliktavleveringslova"](https://lovdata.no/dokument/NL/lov/1989-06-09-32) - a Norwegian law that requires all published materials to be sent to the library so it can be made available for research and documentation. 


## Main Sources
### Norwegian National Library
The copyright issues of this part of the corpus needs to be cleared with Kopinor before publishing
* **Books** - Published between 1814 and 2020. OCR quality of books scanned between 2006 and 2008 have fairly low quality. Only books scanned from 2009 are included included. A rough estimate is that more than 50% of all published books in Norway is included.
* **Newspapers** - Published between 2015 and 2020. A collection of pdf-files and scans from microfilm.
* **Periodicals** - Published between ??. A wide range of periodicas and yearbooks. Mostly OCR scans.
* **Legal** - LovData CD (200?) and LovData DVD (200?). This is a complete collection of all verdicts prior to these dates. The collection is originally OCR scanned but after that manually corrected.


### Public Sources
This part of the corpus can be downloaded directly. The rights to redistribute the cleaned versions needs to be cleared.
* **Wikipedia NOB** - [Norwegian Wikipedia Bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/) downloaded March 2019 and published by Språkbanken. Nynorsk and Bokmål are published in the same file.
* **Wikipedia NNO** - [Norwegian Wikipedia Nynorsk](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/) downloaded March 2019 and published by Språkbanken. Nynorsk and Bokmål are published in the same file.
* **Newspapers Språkbanken** - A [Norwegian Newspaper Corpus](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-4/) with texts between 1998 and 2019 collected by Språkbanken. 
* **MC4** - The Norwegian part of the [Colossal Clean Crawled Corpus](https://www.tensorflow.org/datasets/catalog/c4?hl=en) published by Google in cooperation with Common Crawl. This is the Norwegian part of the corpus used to train T5 in 2020. See cleaning instructions at the end of this article.
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
| Wikipedia NOB  | - |  - | 
| Wikipedia NON  | - |  - | 
| Newspapers Språkbanken | - |  - |
| MC4  | - |  - | 
| Norwegian Government Reports  | - |  - | 
| Parliament Archives  | - |  - | 
| **Total**  |**-** |  **-** |


### Size in Gb
| Sources  |  PPL (2) | Cleaned (3) |
| -------- |  -----:|  -----:| 
| Books  | 69 | 68 | 
| Newspapers | - | - | 
| Periodicals  | - |  - |
| Legal  | - |  - |
| Wikipedia NOB  | - |  - | 
| Wikipedia NON  | - |  - | 
| Newspapers Språkbanken | - |  - |
| MC4  | - |  - | 
| Norwegian Government Reports  | - |  - | 
| Parliament Archives  | - |  - | 
| **Total**  |**-** |  **-** |


### Total Corpus Size
| Sources  |  Cleaned (3) | Deduplicated (4/5) | Tfrecord dupe=1 (6) |
| -------- |  -----:|  -----:| -----:| 
| Words (Billion)  | - | - | - | 
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
| Parliament Archives  | - |  SA | 

## Notes
### MC4 Cleaning
The MC4 is a cleaned version of Common Crawl. The following precedure have been applied:

> Unfortunately, the majority of [the text in Common Crawl] is not natural language. Instead, it largely comprises gibberish or boiler-plate text like menus, error messages, or duplicate text. Furthermore, a good deal of the scraped text contains content that is unlikely to be helpful for any of the tasks we consider (offensive language, placeholder text, source code, etc.). To address these issues, we used the following heuristics for cleaning up Common Crawl's web extracted text:
> - We only retained lines that ended in a terminal punctuation mark (i.e. a period, exclamation mark, question mark, or end quotation mark).
> - We removed any page that contained any word on the "List of Dirty, Naughty, Obscene or Otherwise Bad Words". [https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and...]
> * Many of the scraped pages contained warnings stating that Javascript should be enabled so we removed any line with the word Javascript.
> - Some pages had placeholder "lorem ipsum" text; we removed any page where the phrase "lorem ipsum" appeared.
>- Some pages inadvertently contained code. Since the curly bracket "{" appears in many programming languages (such as Javascript, widely used on the web) but not in natural text,we removed any pages that contained a curly bracket.
> - To deduplicate the dataset, we discarded all but one of any three-sentence span occurring more than once in the dataset.
Additionally, since most of our downstream tasks are focused on English-language text, we used langdetect [https://pypi.org/project/langdetect/] to filter out any pages that were not classified as English with a probability of at least 0.99. 

