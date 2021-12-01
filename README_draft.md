# Norwegian Transformer Model

The project "NoTraM - Norwegian Transformer Model" is owned by the National Library of Norway. The goal is to create transformer-based models for the Norwegian language, and using the libraries resources in building a huge Norwegian text corpus.

The goal of the project is therefore twofold:

* Build transformer-based models for Norwegian and nordic languages based on modern transformer architectures (BERT,Roberta,T5 a.o)
* Build an execellent corpus (both in quality and quantity) specialized for unsupervised language training. Our goal is to make it available openly to the machine learning community. And thereby make a good resource for future language models in Norwegian.



## 🔥 December 1st 2021 - First Release of the Norwegian Colossal Corpus 🔥
# Norwegian Colossal Corpus
The Norwegian Colossal Corpus is an open text corpus comparable in size and quality with available datasets for English. 

The core of the corpus is based on a [unique project](https://www.zdnet.com/article/norways-petabyte-plan-store-everything-ever-published-in-a-1000-year-archive/) started in 2006. In the digitalisation project the goal has veeb to digitize and store all content ever published in Norwegian. In addition we have added multiple other public sources of Norwegian text. Details about the sources as well as how they are built are available in the [Colossal Norwegian Corpus Description](https://github.com/NBAiLab/notram/tree/master/corpus). 

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

The easiest way to access the corpus is to [download from HuggingFace](https://huggingface.co/datasets/NbAiLab/NCC). This site explains in details how the corpus can be used. It also gives an extensive information about the content of the corpus, as well as how to filter out certain part of the corpus and how it can be combined with other Norwegian datasets like [MC4](https://huggingface.co/datasets/mc4) and [OSCAR](https://huggingface.co/datasets/oscar).

In addition to the corpus itself we do provide a set of scripts for [creating](guides/create_scripts.md) and [cleaning](guides/cleaning_rules_description.md) corpus files. We also provide a guide where you can follow us in creating a corpus for your data sources[step-by-Step Guide about how to create corpus file](guides/step_by_step_guide.md), and a description about how to [create and upload a HuggingFace dataset](guides/creating_huggingface_dataset.md). Other tools and guides can also be found on our [Guides Page](guides/README.md). We have made all our software available for anyone to use. Most of it is written in python 3. 


# Models
Currently the following models are available from the National Library. The models below are all trained on an older, and partly restricted corpus. We are planning on releasing a set of models trained on our newest corpus.

| Name  |  Description | Model|
| -------- |  :-----| ----------:|
| nb&#8209;bert&#8209;base | The original model based on the same structure as [BERT Cased multilingual model](https://github.com/google-research/bert/blob/master/multilingual.md). Even if it is trained mainly on Norwegian text, it does also maintain some of the multilingual capabilities. Especially it has good scores on Swedish, Danish and English. | [🤗&nbsp;Model](https://huggingface.co/NbAiLab/nb-bert-base)|
| nb&#8209;bert&#8209;base&#8209;mnli | The nb-bert-base-model finetuned on the mnli task. Unlike the other models, this model can be used for classification tasks without any additional finetuning. | [🤗&nbsp;Model](https://huggingface.co/NbAiLab/nb-bert-base-mnli)|
| nb&#8209;bert&#8209;large | The model is based on the BERT-large-uncased architecture. For classification tasks, this model will give the best results. Since it is uncased it might not give as good results on NER-tasks. It might require more processing power both for finetuning and for inference.| [🤗&nbsp;Model](https://huggingface.co/NbAiLab/nb-bert-large)|


## Results
The NB-BERT-Base model is thoroughly tested in the article cited below. Here are some of our results:
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


# Colab Notebooks
The original models need to be fine-tuned for the target task. A typical task is classification, and it is then recommeded that you train a top fully connected layer for this specific task. The following notebooks will allow you to both test the model, and **to train your own specialised model** on top of our model. Especially the notebook about classification models that trains a sentiment classification task, can very easily be adapted to training any NLP classification task.

| Task  |   Colaboratory Notebook |
| -------- | -----:|
| How to use the model for masked layer predictions (easy)|<a href="https://colab.research.google.com/gist/peregilk/f3054305cfcbefb40f72ea405b031438/nbailab-masked-layer-pipeline-example.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| How to use finetuned MNLI-version for zero-shot-classification (easy)|<a href="https://colab.research.google.com/gist/peregilk/769b5150a2f807219ab8f15dd11ea449/nbailab-mnli-norwegian-demo.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| How to finetune a classification model (advanced)| <a href="https://colab.research.google.com/gist/peregilk/3c5e838f365ab76523ba82ac595e2fcc/nbailab-finetuning-and-evaluating-a-bert-model-for-classification.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|
| How to finetune a NER/POS-model (advanced) | <a href="https://colab.research.google.com/gist/peregilk/6f5efea432e88199f5d68a150cef237f/-nbailab-finetuning-and-evaluating-a-bert-model-for-ner-and-pos.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|

# Disclaimer 
_The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.
When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.
In no event shall the owner of the models (The National Library of Norway) be liable for any results arising from the use made by third parties of these models._

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
