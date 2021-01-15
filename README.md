# Norwegian Transformer Model
This is the repository for the project "NoTraM - Norwegian Transformer Model" owned by the National Library of Norway. The purpose is to create a transformer-based model for the Norwegian language. In addition the project aims at collecting and facilitate language resources that can be used for creating other Norweigan NLP models.

# Models
We have released the NB-BERT-Base model. This is based on the same structure as [BERT Cased multilingual model](https://github.com/google-research/bert/blob/master/multilingual.md), and is trained on a wide variety of Norwegian text (both bokmål and nynorsk) from the last 200 years. The score below is on NER/POS-tasks on a newer corpus but we expect the model also perform good on other tasks.

Here are some of our results:
| Task  |   mBERT-base| NB-BERT-base |
| -------- |   -----:| -----:|
|POS - NorNE - Bokmål|98.32|**98.86**|
|POS - NorNE - Nynorsk|98.08|**98.77**|
| | | |
|NER - NorNE - Bokmål|88.67|**93.66**|
|NER - NorNE - Nynorsk|88.13|**92.02**|
| | | |
|Classification - ToN - Frp/SV|73.75|**77.49**|
|Sentence-level binary sentiment classification|73.27|**84.04**|

* F1-scores on test dataset. Both models were finetuned for 4 epochs with learning rate 3e-5.



## Download
The model can be [downloaded from Huggingface](https://huggingface.co/nbailab). 

## Colab Notebooks
| Task  |   Colaboratory Notebook |
| -------- | -----:|
| How to use the model for masked layer predictions (easy)|<p align="left"><a href="https://colab.research.google.com/gist/peregilk/f3054305cfcbefb40f72ea405b031438/nbailab-masked-layer-pipeline-example.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></p> |
| How to finetune a classification model (advanced)| <a href="https://colab.research.google.com/gist/peregilk/3c5e838f365ab76523ba82ac595e2fcc/nbailab-finetuning-and-evaluating-a-bert-model-for-classification.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|
| How to finetune a NER/POS-model (advanced) | <p align="left"><a href="https://colab.research.google.com/gist/peregilk/6f5efea432e88199f5d68a150cef237f/-nbailab-finetuning-and-evaluating-a-bert-model-for-ner-and-pos.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></p>|


# Corpus
In a [unique project](https://www.zdnet.com/article/norways-petabyte-plan-store-everything-ever-published-in-a-1000-year-archive/) started in 2006, the National Library of Norway is aiming at digitizing and storing all content ever published in Norwegian and making it available to the public. This is the bases for this training corpus. In addition we add several other known public sources of Norwegian text. Details about the sources as well as how they are processed are available in the [Colossal Norwegian Corpus Description](https://github.com/NBAiLab/notram/blob/master/guides/corpus_description.md).

The table below describes the size of the current version of the corpus.

| Sources  |   Million words | GB text |
| -------- |   -----:| -----:|
| Books OCR 1814-2020| 11 820| 69.0 |
| Newspapers Scan OCR 2015-2020|  3 350 | 20.0 |
| Newspapers Microfilm OCR 1961,1971,1981,1998-2007|  292 | 1.8 |
| Periodicals OCR 2010-2020 |  317 | 1.9 |
| Public Reports OCR 1814-20?? (Evalueringsrapporter) |  91 | 0.6 |
| Legal Collection 1814-2004 (Lovdata CD/DVD) |  63 | 0.4 |
| Wikipedia NOB -2019  | 140 | 0.9 |
| Wikipedia NNO -2019 | 32 | 0.2 |
| Newspapers Online NOB -2019 | 678 | 4.0 |
| Newspapers Online NNO -2019 |  47 | 0.3 |
| Common Crawl OSCAR -2020 |  799 | 4.9 |
| Parliament Documents OCR 1814-2014 (Stortingsforhandlingene)  |  809 | 5.1 |
| **Total After Dedublication**  | **18 438** | **109.1 GB** |

# Comparable Large Corpuses
| Sources  |  Size (GB) |
| -------- |  -----:|
| Norwegian part of mBERT | 1 GB |
| English BERT | 16 GB |
| Swedish BERT | 20 GB |
| English XLNet Base | 16 GB |
| English XLNet Large | 113 GB |
| English RoBERTa | 160 GB |

# Planned future versions
| Sources  |  Approx Size (GB) |
| -------- |  -----:|
| MC4 -2020| ~20 GB |
| Not included newspapers scan and microfilm | ~50 GB |
| Re-OCR | ~50 GB |
| Current unscanned part of NL archive | ~50 GB |
| Governments documents | ~5 GB |


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
