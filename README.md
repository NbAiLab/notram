# Norwegian Transformer Model
This is the repository for the project "NoTraM - Norwegian Transformer Model" owned by the National Library of Norway. The purpose is to create a transformer-based model for the Norwegian language. In addition the project aims at collecting and facilitate language resources that can be used for creating other Norweigan NLP models.

# Corpus
In a [unique project](https://www.zdnet.com/article/norways-petabyte-plan-store-everything-ever-published-in-a-1000-year-archive/) started in 2006, the National Library of Norway is aiming at digitizing and storing all content ever published in Norwegian and making it available to the public. This is the bases for this training corpus. In addition we add several other known public sources of Norwegian text. Read about the [details and the status](https://github.com/NBAiLab/notram/blob/master/guides/corpus.md) of composing the Collossal Norwegian Corpus.

# Guides
Technical guides made available that explains the process of both creating the corpus, and doing the actual training. 
### [Preparing bucket, VM and TPU for training Notram BERT](https://github.com/NBAiLab/notram/blob/master/guides/setting_up_machines_for_training.md)
### [Setting up a Notram VM from scratch](https://github.com/NBAiLab/notram/blob/master/guides/set_up_vm.md)
### [Training a Notram BERT model](https://github.com/NBAiLab/notram/blob/master/guides/start_training.md)
### [Prepare and download the Nordic part of MC4](https://github.com/NBAiLab/notram/blob/master/guides/prepare_common_crawl.md)

# Other Resources
### Vocabulary tools
* [bert-vocab-builder](https://github.com/kwonmha/bert-vocab-builder)

### Corpora resources
* [Parallel Corpora for European Languages](https://paracrawl.eu/)
* [OSCAR - Filtered Common Crawl](https://oscar-corpus.com/)

### Other Nordic Models
* [Swedish BERT Models](https://github.com/Kungbib/swedish-bert-models)
