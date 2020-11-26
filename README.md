# Norwegian Transformer Model
This is the repository for the project "NoTraM - Norwegian Transformer Model" owned by the National Library of Norway. The purpose is to create a transformer-based model for the Norwegian language. In addition the project aims at collecting and facilitate language resources that can be used for creating other Norweigan NLP models.

# Corpus
In a [unique project](https://www.zdnet.com/article/norways-petabyte-plan-store-everything-ever-published-in-a-1000-year-archive/) started in 2006, the National Library of Norway is aiming at digitizing and storing all content ever published in Norwegian and making it available to the public. This is the bases for this training corpus. In addition we add several other known public sources of Norwegian text. Details about the sources as well as how they are processed are available in the [Colossal Norwegian Corpus Description](https://github.com/NBAiLab/notram/blob/master/guides/corpus_description.md).

The table below describes the current status of the corpus. Size is available as soon as the status reaches level 3.

| Sources  |  Level | Responsible | Million words | GB text |
| -------- |  -----:|  -----:| -----:| -----:|
| Books OCR 1814-2020| 4 | - | 11 820| 69.0 |
| Newspapers Scan OCR 2015-2020| 4 | - | 3 350 | 20.0 |
| Newspapers Microfilm OCR 2006| (1) | F | - | - |
| Periodicals OCR 2010-2020 | (2) |  - | - | - |
| Public Reports OCR 1814-20?? (Evalueringsrapporter) | 4 |  - | 91 | 0.6 |
| Legal Collection 1814-2004 (Lovdata CD/DVD) | 4 |  - | 63 | 0.4 |
| Wikipedia NOB -2019  | 4 |  - | 140 | 0.9 |
| Wikipedia NNO -2019 | 4 |  - | 32 | 0.2 |
| Newspapers Online NOB -2019 | 4 |  - | 678 | 4.0 |
| Newspapers Online NNO -2019 | 4 |  - | 47 | 0.3 |
| MC4 -2020 | (1) |  J | - | - |
| Common Crawl OSCAR -2020 | 4 |  - | 799 | 4.9 |
| Parliament Documents OCR 1814-2014 (Stortingsforhandlingene)  | 4 |  PE | 809 | 5.1 |
| **Total After Dedublication**  |  |   | **17 829** | **105.4 GB** |

# Comparable Large Corpuses
| Sources  |  Size (GB) |
| -------- |  -----:|
| Norwegian part of mBERT | 0.5 GB |
| English BERT | 16 GB |
| Swedish BERT | 20 GB |
| English XLNet Base | 16 GB |
| Eglish XLNet Large | 113 GB |
| English RoBERTa | 160 GB |

# Guides
Technical guides made available that explains the process of both creating the corpus, and doing the actual training. 
### [Preparing bucket, VM and TPU for training Notram BERT](https://github.com/NBAiLab/notram/blob/master/guides/setting_up_machines_for_training.md)
### [Setting up a Notram VM from scratch](https://github.com/NBAiLab/notram/blob/master/guides/set_up_vm.md)
### [Training a Notram BERT model](https://github.com/NBAiLab/notram/blob/master/guides/start_training.md)
### [Prepare and download the Nordic part of MC4](https://github.com/NBAiLab/notram/blob/master/guides/prepare_common_crawl.md)
### [Colossal Norwegian Corpus Description](https://github.com/NBAiLab/notram/blob/master/guides/corpus_description.md)
### [Technical procedures for creating the Colossal Norwegian Corpus](https://github.com/NBAiLab/notram/blob/master/guides/creating_corpus.md)

# Other Resources
### Vocabulary tools
* [bert-vocab-builder](https://github.com/kwonmha/bert-vocab-builder)

### Other Nordic Models
* [Swedish BERT Models](https://github.com/Kungbib/swedish-bert-models)
