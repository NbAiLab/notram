# Step-By-Step Guide - Corpus Building
This step-by-step guide walks you through the entire process of curating a corpus in the json-format used by the NCC. The examples here is applied on the OSCAR corpus, but can easily be adaptet to any sub-corpus you would like to convert to this format.

The general structure is:
1) Obtaining source files
2) Converting to json
3) Cleaning and deduplication
4) Collation and cross corpus deduplication
5) Creating the dataset


## 0) Preparation
In this example we store all the files under */home/user*. Here we will have two directories, */home/user/notram* that is the notram-git, and */home/user/corpus* where our subcorpus is stored. Under the last folder, there will be the following sub-directories: *source\_1*, *json\_2*, *clean\_json\_3*, *corpus\_files\_4*, *corpus_\collections_5*.

Lets create this structure
```bash
# Go to home directory
cd

# Clone notram. You are of course free to fork it instead
git clone https://github.com/NBAiLab/notram.git

# Make the directories
mkdir corpus corpus/clean_1 corpus/json_2 corpus/clean_json_3 corpus/corpus_files_4 corpus/corpus_collections_4

```


## 1) Optaining Source Files
This step is dependent source. In this example we download the [OSCAR](https://oscar-corpus.com/post/oscar-v21-09/) corpus. Please note that this is also available as a [Hugging Face Dataset](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109) but since we want to apply some extra cleaning and also deduplicate on cross of other corpuses, we here download it from the source. To optain the original files, you will need to contact the authors by mail. In this example all files are stored in a folder named /home/user/corpus.


## 2) Converting to json
For the OSCAR dataset, you will notice that there is a prepared create-script called [*create_oscar.py*](https://github.com/NBAiLab/notram/blob/master/corpus_generation_scripts/create_oscar.py) available in */home/user/notram/corpus_generation_scripts/create_oscar.py*. Documentation is available [here](https://github.com/NBAiLab/notram/blob/master/guides/create_scripts.md#create_oscarpy). The OSCAR dataset is in a very simple txt based format where each line is a document. There are multiple other create-scripts in this folder, and if you dataset has another format (like pdf, xml, xhtml, json) it is likely that you can find another script to use as a starting point.

The goal of this script is to convert the external dataset to a structures [json-lines format](https://github.com/NBAiLab/notram/blob/master/guides/text_extraction_format.md) are used. format. This 

```bash
# Go to home directory
cd

# Convert the source files to json
python 
```

