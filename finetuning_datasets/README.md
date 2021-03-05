# Norwegian Finetuning Datasets
This is a description of some openly available finetuning datasets that might be useful for evaluating Norwegian NLP Models. The list is focused on training sets that are suitable for testing the performance of transformer-based NLP-models. These set are most likely not suited for making a production system.

## The Talk of Norway: A Richly Annotated Corpus of the Norwegian Parliament, 1998–2016
Every speech is richly annotated with metadata harvested from different sources, and augmented with language type, sentence, token, lemma, part-of-speech, and morphological feature annotations. The work is thoroughly described in this [article](https://www.duo.uio.no/bitstream/handle/10852/71356/ton.pdf?sequence=2&isAllowed=y). From this set a large number of finetuning datasets can be generated. The entire annotated dataset is available from the [talk-of-norway GitHub](https://github.com/ltgoslo/talk-of-norway)

### Nynorsk/Bokmål
A balanced dataset with 6000 bokmål/nynorsk sentences. Collected by the Norwegian National Library. Available from [here](https://github.com/NBAiLab/notram/blob/master/finetuning_datasets/parliament_speeches_1998_2016_nob_nyn.csv).

### Cabinet/Support/Opposition
A balanced dataset with 6000 samples telling if the speaker is cabinet, support or opposition. Collected by the Norwegian National Library.
Available from [here](https://github.com/NBAiLab/notram/blob/master/finetuning_datasets/parliament_speeches_1998_2016_role.csv).

### FrP/SV
A balanced dataset with 6000 samples telling if the speaker is FrP or SV. Please note that is is not given that it is actually possible, even for a human, to determine the party of the speaker. Collected by the Norwegian National Library.
Available from [here](https://github.com/NBAiLab/notram/blob/master/finetuning_datasets/parliament_speeches_1998_2016_frp_or_sv.csv).

### Sentences
Single unique sentences from the Talk of Norway dataset. Sentences have been extracted and separated into a Bokmål and Nynorsk corpus based on the annotation. Then they have been segmented. The following command has been run to clean the corpus: "cat sentences_talk_of_norway_text_nob.txt | sort | uniq | shuf| grep -E '^(\w+\b.){4}' | grep '^[A-ZÆØÅ].*[.]$' >> sentences_talk_of_norway_cleaned_nob.txt". This corpus is excluded from the NoTraM training set, and is therefore suitable for testing. The Bokmål corpus has 1,361,240 sentences, while the Nynorsk corpus has 182,210 sentences. The dataset is available from the NB Ai-Lab public git.  


# Universial Dependencies
The Norwegian UD treebank is based on the Bokmål section of the Norwegian Dependency Treebank (NDT), which is a syntactic treebank of Norwegian. NDT was developed 2011-2014 at the National Library of Norway in collaboration with the Text Laboratory and the Department of Informatics at the University of Oslo. It contains both morphological and syntactic annotations.

It includes a total of 20.045 sentences, split in training, validation and test. It can be downloaded directly from the [Universal Depenncies - Norwegian Bokmål GitHub](https://github.com/UniversalDependencies/UD_Norwegian-Bokmaal), but is more easily available as part of the [norwegian_ner - Huggingface Dataset](https://huggingface.co/datasets/norwegian_ner).


# Named Entity Recognition
This dataset is described in the paper NorNE: Annotating Named Entities for Norwegian by Fredrik Jørgensen, Tobias Aasmoe, Anne-Stine Ruud Husevåg, Lilja Øvrelid, and Erik Velldal, accepted for LREC 2020 and available as pre-print [here](https://arxiv.org/abs/1911.12146). NorNE ads named entity annotations on top of the Norwegian Dependency Treebank and was created as a collaboration between Schibsted Media Group, Språkbanken at the National Library of Norway and the Language Technology Group at the University of Oslo. The NorNE corpus is published under the same license as the Norwegian Dependency Treebank.

The dataset is available directly as the [norwegian_ner - Huggingface Dataset](https://huggingface.co/datasets/norwegian_ner).


# Modalities
Lorem Epsum... ?

# Analogies dataset
Lorem epsum... ?

# NoReC: The Norwegian Review Corpus
The Norwegian Review Corpus (NoReC) is created for the purpose of training and evaluating models for document-level sentiment analysis. The entire corpus can be downloaded from the [Norwegian Review Corpus GitHub](https://github.com/ltgoslo/norec).

### NoReC Eval
NoReC_eval is a dataset of Norwegian full-text reviews where sentences are labeled to indicate whether they are evaluative or sentiment-bearing, i.e. where they are intended by the author (or some other opinion holder) to serve as an evaluation or judgment. The data comprises roughly 8000 sentences across almost 300 reviews and 10 different thematic categories. 

The data is distributed in a tab-separated format, with one tsv-file per review. Download from the [NoReC Eval GitHub](https://github.com/ltgoslo/norec_eval).

### NoReC Fine
An extension of the NoRec Eval. While the previously released dataset NoReC_eval labeled sentences as to whether they are evaluative or sentiment-bearing, NoReC_fine expands on these annotations by labeling polar expressions, opinion holders and opinion targets. It is also expanded by roughly 3500 sentences.

Download from the [NoReC Fine GitHub](https://github.com/ltgoslo/norec_fine).

### NoRec Gender
NoReC_gender comprises the book reviews of the Norwegian Review Corpus (NoReC), here expanded with annotations of gender of both book authors and critics (review authors).

Download from the [NoReC Gender GitHub](https://github.com/ltgoslo/norec_gender).

| Task  |   Colaboratory Notebook |
| -------- | -----:|
| How to use the model for masked layer predictions (easy)|<a href="https://colab.research.google.com/gist/peregilk/f3054305cfcbefb40f72ea405b031438/nbailab-masked-layer-pipeline-example.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| How to finetune a classification model (advanced)| <a href="https://colab.research.google.com/gist/peregilk/3c5e838f365ab76523ba82ac595e2fcc/nbailab-finetuning-and-evaluating-a-bert-model-for-classification.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|
| How to finetune a NER/POS-model (advanced) | <a href="https://colab.research.google.com/gist/peregilk/6f5efea432e88199f5d68a150cef237f/-nbailab-finetuning-and-evaluating-a-bert-model-for-ner-and-pos.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|
