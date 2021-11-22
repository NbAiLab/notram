# Step-By-Step Guide - Corpus Building
This step-by-step guide walks you through the entire process of curating a corpus in the json-format used by the NCC. The examples here is applied on the OSCAR corpus, but can easily be adaptet to any sub-corpus you would like to convert to this format.

The general structure is:
1) Preparation and obtaining source files
2) Converting to json
3) Cleaning and deduplication
4) Collation and cross corpus deduplication
5) Creating the dataset


## 1) Preparation and Optaining Source Files
In this example we store all the files under */home/user*. Here we will have two directories, */home/user/notram* that is the notram-git, and */home/user/corpus* where our subcorpus is stored. Under the last folder, there will be the following sub-directories: *source\_1*, *json\_2*, *clean\_json\_3*, *corpus\_files\_4*, *corpus_\collections_5*.

Lets create this structure
```bash
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
cd ~

# Convert the source files to json
# How long this takes is depended upon your hardware. 
# Run the Nynorsk corpus first. The corpus is 66MB and will give you an indication. The Bokmål corpus is 60 times larger (4GB). 
python notram/corpus_generation_scripts/create_oscar.py --language_reported nn --doc_type oscar_nn --input_file corpus/source_1/oscar_nn.txt --output_file corpus/json_2/oscar_nn.json
python notram/corpus_generation_scripts/create_oscar.py --language_reported nb  --doc_type oscar_nb --input_file corpus/source_1/oscar_nb.txt --output_file corpus/json_2/oscar_nb.json

```

## 3) Cleaning and Deduplication
The problem with using web based sources for training languge models is that they contain a lot of noise. Typical examples is long product lists that are not really language and considerable amount of machine generated text. The OSCAR corpus is considerably more cleaned than for instance MC4, but we still apply our cleaning procedure also on this corpus.

The cleaning routines are defined in separate config-files. These can be adapted to the specific source. Cleaning procedures for OCR-based texts are usually different from digitally born texts. Here we are using a config.script from the notram-repository. You can of course make your own config-file and refer to this instead. The cleaning also does a few other tricks: It calculates the document length and a hash for each of the paragraphs. This speeds up the process of deduplicating across the corpuses.

```bash
cd ~ 

# Run the clean scripts
# Here you could also use the Nynorsk to get an estimate of how long the Bokmål script will take
python notram/corpus_generation_scripts/clean.py --input_file corpus/json2/oscar_nn.json --ouput_folder corpus/clean_json_3 --config_file notram/corpus_generation_scripts/config/config.json
python notram/corpus_generation_scripts/clean.py --input_file corpus/json2/oscar_nb.json --ouput_folder corpus/clean_json_3 --config_file notram/corpus_generation_scripts/config/config.json
```

4) Standardisation and cross corpus deduplication
Often we will have a lot of small corpuses that we want to combine. The last step has multiple steps. Firstly it strips away any unnecessary meta-data and standardises the json for instance for publication year. It then uses Fasttext to do language detection based on the text. Please refer to the Fasttext pages for how to install this. In the end it runs a The final json will have this structure:

|**id:** | String with id to source of line and a unique identifier|
|:-----------|:------------|
|**doc_type ** | String describing type of media text extracted from (I.e. book,newspaper etc)|
|**publish_year ** | Integer. The year text published. When year is undetermined it is set to 2021.|
|**lang_fasttext ** | String. Language of text identified by FastText|
|**lang_fasttext_conf ** | String. Confidence calculated by FastText|
|**text ** | String. The complete utf-8 document. If longer than 1M characters it is split.|

```bash
cd ~ 

# Run the corpus file creator

**FREDDY**

```


5) Creating the dataset
Even after step 4 we have individual datasets. Now we want to callate this corpuses, shuffle them and in the end create a train and validation set.

```bash
cd ~ 

# Run the corpus file creator

**FREDDY**

```

