# Norwegian Transformer Model
## 🔥 December 1st - Release the Norwegian Colossal Corpus 🔥
## 🔥 December 1st - Release New Norwegian RoBERTa Models 🔥

The project "NoTraM - Norwegian Transformer Model" is owned by the National Library of Norway. The purpose is to create a transformer-based model for the Norwegian language. In addition the project aims at collecting and facilitate language resources that can be used for creating other Norweigan NLP models. This includes building the Norwegian Colossal Corpus.
### Most of these links should appear naturally in the text below
* [Overview Processing the NCC](processing_NCC.md)
* [Step-by-Step Guide Processing the NCC](step_by_step_guide.md)
* [Creating and Uploading HuggingFace Dataset](creating_huggingface_dataset.md)
* [Norwegian Colossal Corpus Description](corpus_description.md)
* [JSON-lines Format](json_format.md)
* [Corpus Create-scripts](create_scripts.md)
* [Corpus Cleaning-rules](cleaning_rules_description.md)
* [Fequently Used Commands for JSON-line Files](json_commands.md)





# Models
Currently the following models are available. Trained on a larger corpus.
| Name  |  Description | Download/Demo|
| -------- |  -----| -----:|
| nb-bert-base | The original model based on the same structure as [BERT Cased multilingual model](https://github.com/google-research/bert/blob/master/multilingual.md). It is trained on The Colossal Norwegian Corpus v1.  | [INFO](https://huggingface.co/NbAiLab/nb-bert-base)|
| nb-bert-base-mnli | The nb-bert-base-model finetuned on the mnli task. Unlike the other models, this model can be used for classification tasks without any additional finetuning. | [INFO](https://huggingface.co/NbAiLab/nb-bert-base-mnli)|
| nb-bert-large (beta) | The model is based on the BERT-large-uncased architecture, and is trained on the Colossal Norwegian Corpus v1. For classification tasks, this model will give the best results.| [INFO](https://huggingface.co/NbAiLab/nb-bert-large)|


## Results
The NB-BERT-Base modelis thoroughly tested in the article cited below. Here are some of our results:
| Task  |   mBERT-base| NB-BERT-base |
| -------- |   -----:| -----:|
|POS - NorNE - Bokmål|98.32|**98.86**|
|POS - NorNE - Nynorsk|98.08|**98.77**|
| | | |
|NER - NorNE - Bokmål|81.75|**90.03**|
|NER - NorNE - Nynorsk|84.69|**87.67**|
| | | |
|Classification - ToN - Frp/SV|73.75|**77.49**|
|Sentence-level binary sentiment classification|73.27|**84.04**|

* *F1-scores on test dataset. Both models were finetuned for 4 epochs with learning rate 3e-5.*

# Colossal Norwegian Corpus
We aim at building a copus of Norwegian text that is on par with available datasets for English. Our aim is to make as much of this publicly available as possible. 

In a [unique project](https://www.zdnet.com/article/norways-petabyte-plan-store-everything-ever-published-in-a-1000-year-archive/) started in 2006, the National Library of Norway is aiming at digitizing and storing all content ever published in Norwegian and making it available to the public. This is the basis for the training corpus. In addition we add several other public sources of Norwegian text. Details about the sources as well as how they are processed are available in the [Colossal Norwegian Corpus Description](https://github.com/NBAiLab/notram/tree/master/corpus).

| Corpus  | License  | Size | Words | Documents | Avg words per doc  |
| -------- | -------- |   :-----|   -----:| -----:| -----:|
| Government Reports | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|1.1 GB| 155,318,754 | 4,648       | 33,416           |
| Parliament Collections | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)| 8.0 GB| 1,301,766,124 | 9,528       | 136,625          |
| Pulic Reports| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|0.5 GB| 80,064,396 | 3,365       | 23,793           |
| LovData CD | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|0.4 GB| 54,923,432 | 51,920      | 1,057            |
| Målfrid Collection| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|14.0 GB| 1,905,481,776 | 6,735,367   |              282 |
| Newspapers| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|14.0 GB| 2,019,172,625 | 10,096,424  |              199 |
| Newspapers Online | [CC BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/)|3.7 GB| 541,481,947 | 3,695,943   |              146 |
| Books | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|6.2 GB| 861,465,907 | 24,253 | 35,519 |
| Subtitles | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)|0.2 GB| 54,133,135 | 13,416      | 4,034            |
| Wikipedia | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)|1.0 GB| 140,992,663 | 681,973     |              206 |


Needs to be adapted for NCC... Just here for reference.
## License
Various licences applies to different parts of the corpus. Every document in the corpus has a tag telling what **"doc_type"** it belongs to. If you are unable to accept any of the licenses, you should filter out the **"doc_type"** with a conflicting license. 

| Doc_type  | License  | 
| :-------- | :------------- |  
| government_nb, government_nn, parliament, publicreports, lovdata_cd_\*, maalfrid_\* | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|
| newspapers_ocr, newspapers_pdf, books| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|
| newspapers_online_nb, newspapers_online_nn | [CC BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/)|
| opensubtitles, wikipedia | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)|
| mc4, oscar_nb, oscar_nn | externally available |
| newspapers_restricted_\*, books_restricted, norart, lovdata_transfer, twitter, twitter_news, facebook, vgdebatt, reddit | restricted |





# Colab Notebooks
The original model needs to be fine-tuned for the target task. A typical task is classification, and it is then recommeded that you train a top fully connected layer for this specific task. The following notebook will allow you to both test the model, and to train your own specialised model on top of our model. Especially the notebook about classification models that trains a sentiment classification task, can very easily be adapted to training any NLP classification task.

| Task  |   Colaboratory Notebook |
| -------- | -----:|
| How to use the model for masked layer predictions (easy)|<a href="https://colab.research.google.com/gist/peregilk/f3054305cfcbefb40f72ea405b031438/nbailab-masked-layer-pipeline-example.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| How to use finetuned MNLI-version for zero-shot-classification (easy)|<a href="https://colab.research.google.com/gist/peregilk/769b5150a2f807219ab8f15dd11ea449/nbailab-mnli-norwegian-demo.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| How to finetune a classification model (advanced)| <a href="https://colab.research.google.com/gist/peregilk/3c5e838f365ab76523ba82ac595e2fcc/nbailab-finetuning-and-evaluating-a-bert-model-for-classification.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|
| How to finetune a NER/POS-model (advanced) | <a href="https://colab.research.google.com/gist/peregilk/6f5efea432e88199f5d68a150cef237f/-nbailab-finetuning-and-evaluating-a-bert-model-for-ner-and-pos.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|


# Citation
If you use our models or our corpus, please cite our article:

    @inproceedings{kummervold-etal-2021-operationalizing,
    title = {Operationalizing a National Digital Library: The Case for a {N}orwegian Transformer Model},
    author = {Kummervold, Per E  and
      De la Rosa, Javier  and
      Wetjen, Freddy  and
      Brygfjeld, Svein Arne",
    booktitle = {Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)},
    year = "2021",
    address = "Reykjavik, Iceland (Online)",
    publisher = {Link{\"o}ping University Electronic Press, Sweden},
    url = "https://aclanthology.org/2021.nodalida-main.3",
    pages = "20--29",
    abstract = "In this work, we show the process of building a large-scale training set from digital and digitized collections at a national library. The resulting Bidirectional Encoder Representations from Transformers (BERT)-based language model for Norwegian outperforms multilingual BERT (mBERT) models in several token and sequence classification tasks for both Norwegian Bokm{\aa}l and Norwegian Nynorsk. Our model also improves the mBERT performance for other languages present in the corpus such as English, Swedish, and Danish. For languages not included in the corpus, the weights degrade moderately while keeping strong multilingual properties. Therefore, we show that building high-quality models within a memory institution using somewhat noisy optical character recognition (OCR) content is feasible, and we hope to pave the way for other memory institutions to follow.",
    }
