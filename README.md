# Norwegian Transformer Model
The project "NoTraM - Norwegian Transformer Model" is owned by the National Library of Norway. The purpose is to create a transformer-based model for the Norwegian language. In addition the project aims at collecting and facilitate language resources that can be used for creating other Norweigan NLP models. This includes building the Norwegian Colossal Corpus.

# Models
Currently the following models are available. 
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
