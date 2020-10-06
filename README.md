# Norwegian Transformer Model
This is the repository for the project "NoTraM - Norwegian Transformer Model" owned by the National Library of Norway. The purpose is to create a transformer-based model for the Norwegian language. In addition the project aims at collecting and facilitate language resources that can be used for creating other Norweigan NLP models.

# Available datasources
### Scanned books
| Sources  |   Words Raw | Words First Clean |Words Second Clean | Deduplicated |
| -------- |  -----:|  -----:| -----:| -----:| 
| 2009  | 1,816,686,744 | 1 205 066 719 | N/A | - | 
| 2010 | 1,570,727,985 | 1 255 763 510 | 1 244 407 623 | - | 
| 2011  | 2,252,826,509 |  2 093 456 928 | 2 076 296 114 | - | 
| 2012  | 1,982,794,535 |  1 574 827 699 | 1 566 777 809 | - | 
| 2013  | 2,410,337,140 |  1 977 450 194 | 1 967 235 126 | - | 
| 2014 | 2,442,049,695 |  1 901 034 898 | 1 522 943 744 | - | 
| 2015  | 1,166,564,208 |  818 726 467 | 813 646 038 | - | 
| 2016  |0 |  1 052 036 635 |1 045 702 485 | - | 
| 2017  |0 |  991 211 953 | 990 217 034 | - | 
| 2018 |0 |  1 269 376 306 | 1 262 184 246 | - | 
| 2019  |0 |  291 495 087 | 290 366 131 | - | 
| 2020  | 0 | 834 129 514 |831 068 263 | - | 
| **Total**  |0 |  **15 264 575 910** | **13 610 844 613++** | **12 824 793 952** | 


### External Bokmål
| Scan year  |   Words | 
| -------- |  -----:| 
| Parliament Talks  |  58 841 660 | 
| Wikipedia |  153 183 516 | 
| Newspaper  |  745 757 438 | 
| Newspaper_xml  |  65 094 804 | 
| **Total**  |  **1 022 877 418** | 


### External Nynorsk
| Sources  |   Words | 
| -------- |  -----:| 
| Wikipedia |  35 051 361 | | 
| Newspaper_xml  |  41 664 447 | 
| **Total**  |  **76 715 808** | 


Here is a [summary](https://github.com/peregilk/NoTraM/blob/master/filestructure.md) of all the avilable datasources and pre-processed files.

# Utils
In this directory there is a collection of corpus cleaners/filters. There is one script per datacorpus. The purpose of the filters is to go through the corpuses and clean the text. The output format is a txt-file where documents (in most cases paragraphs) are separated by a single linebreak. The format should be standard UTF-8. No sentence segmentation and/or deduplication is done at this stage. Each of the scripts does some basic cleaning but currently no filtering based on length.

### Basic commands for creating the txt-files where documents/paragraphs are separated by single linebreaks
```bash
python utils/clean_parliament.py --input_file data/rawfiles/parliament_speeches_1998_2016.csv --output_file data/output/sentences/parliament_speeches_1998_2016_rawarticles.txt &&
python utils/clean_wikipedia.py --input data/rawfiles/nob.wikipedia.json --output_file data/output/sentences/nob.wikipedia.txt &&
python utils/clean_newspapers.py --input data/rawfiles --output_file data/output/sentences/norsk_aviskorpus_html.txt &&
python utils/clean_newspapers_xml.py --language nob --input data/rawfiles --output_file data/output/sentences/norsk_aviskorpus_xml_bokmal.txt &&

python utils/clean_wikipedia.py --input data/rawfiles/nno.wikipedia.json --output_file data/output/sentences/nno.wikipedia.txt &&
python utils/clean_newspapers_xml.py --language nno --input data/rawfiles --output_file data/output/sentences/norsk_aviskorpus_xml_nynorsk.txt
```

The last script does basic filtering (based on minimum three words per article). It also does deduplication and shuffles the entire dataset.
```bash
python utils/norwegian_sentence_segmentation.py --input data/output/sentences --output_file data/output/corpus/all_040920.txt -d True -r True
```

# Resources

### Vocabulary tools
* [bert-vocab-builder](https://github.com/kwonmha/bert-vocab-builder)

### Corpora resources
* [Parallel Corpora for European Languages](https://paracrawl.eu/)
* [OSCAR - Filtered Common Crawl](https://oscar-corpus.com/)

