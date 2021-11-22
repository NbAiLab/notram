# Step-By-Step Guide - Corpus Building
This step-by-step guide walks you through the entire process of curating a corpus in the json-format used by the NCC. The examples here is applied on the OSCAR corpus, but can easily be adaptet to any sub-corpus you would like to convert to this format.

The general structure is:
1) Obtaining source files
2) Converting to json
3) Cleaning and deduplication
4) Collation and cross corpus deduplication
5) Creating the dataset


## 0) Preparation



## 1) Optaining Source Files
In this example we store all the files under */home/user*. Here we will have two directories, */home/user/notram* that is the notram-git, and */home/user/corpus* where our subcorpus is stored. Under the last folder, there will be the following sub-directories: *source\_1*, *json\_2*, *clean\_json\_3*, *corpus\_files\_4*, *corpus_\collections_5*.

Lets create this structure
```bash
# Go to home directory
cd ~

# Clone notram. You are of course free to fork it instead
git clone https://github.com/NBAiLab/notram.git

# Install requirements (we really recomment doing this in a virtual environment)
pip install -r notram/requirements.txt

# Make the directories
mkdir corpus corpus/clean_1 corpus/json_2 corpus/clean_json_3 corpus/corpus_files_4 corpus/corpus_collections_5

```

In this example we download the [OSCAR](https://oscar-corpus.com/post/oscar-v21-09/) corpus. Please note that this is also available as a [Hugging Face Dataset](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109) but since we want to apply some extra cleaning and also deduplicate on cross of other corpuses, we here download it from the source. To optain the original files, you will need to contact the authors by mail. In this example all files are stored in a folder named /home/user/corpus.

```bash
# To be written.... we can also download this from HuggingFace RAW.....

```

## 2) Converting to json
For the OSCAR dataset, you will notice that there is a prepared create-script called [*create_oscar.py*](https://github.com/NBAiLab/notram/blob/master/corpus_generation_scripts/create_oscar.py) available in */home/user/notram/corpus_generation_scripts/create_oscar.py*. Documentation is available [here](https://github.com/NBAiLab/notram/blob/master/guides/create_scripts.md#create_oscarpy). The OSCAR dataset is in a simple txt-based format where each line is a document. There are multiple other create-scripts in the same directory, and if your dataset has another format (like pdf, xml, xhtml, json) it is likely that you can find another script to use as a starting point.

The goal of this script is to convert the external dataset to a structures [json-lines format](https://github.com/NBAiLab/notram/blob/master/guides/text_extraction_format.md) are used. format. This 

```bash
# Go to home directory
cd ~

# Convert the source files to json
# How long this depends depends on your computer. Run the Nynorsk corpus first. The corpus is 66MB and will give you an indication. The Bokmål corpus is 60 times larger (4GB). 
python notram/corpus_generation_scripts/create_oscar.py --language_reported nn --doc_type oscar_nn --input_file corpus/source_1/oscar_nn.txt --output_file corpus/json2/oscar_nn.json
python notram/corpus_generation_scripts/create_oscar.py --language_reported nb  --doc_type oscar_nb --input_file corpus/source_1/oscar_nb.txt --output_file corpus/json2/oscar_nb.json

```

## 3) Cleaning and deduplication
The problem with using web based sources for training languge models is that they contain a lot of noise. Typical examples is long product lists that are not really language and considerable amount of machine generated text. The OSCAR corpus is considerably more cleaned than for instance MC4, but we still apply our cleaning procedure also on this corpus.

The cleaning routines are defined in separate config-files. These can be adapted to the specific source. Cleaning procedures for OCR-based texts are usually different from digitally born texts. We start here by copying a sample config-file

