# Step-By-Step Corpus Building Guide
This step-by-step guide walks you through the entire process of curating a corpus in the json-format used by the NCC. The examples here is applied on the OSCAR corpus, but can easily be adaptet to any sub-corpus you would like to convert to this format.

The general structure is:
1) Preparation and obtaining source files
2) Converting to json
3) Cleaning and deduplication
4) Collation and cross corpus deduplication
5) Creating the dataset


## 1) Preparation and Obtaining Source Files
In this example we store all the files under */home/user*. Here we will have two directories, */home/user/notram* that is the notram-git, and */home/user/corpus* where our subcorpus is stored. Under the last folder, there will be the following sub-directories: *source\_1*, *json\_2*, *clean\_json\_3*, *corpus\_files\_4*, *corpus\_collections_5*.

Lets create this structure
```bash
cd ~

# Clone notram. You are of course free to fork it instead
git clone https://github.com/NBAiLab/notram.git

# Install requirements (we really recomment doing this in a virtual environment)
pip install -r notram/requirements.txt

# Make the directories
mkdir corpus corpus/source_1 corpus/json_2 corpus/clean_json_3 corpus/clean_json_3/log corpus/corpus_files_4 corpus/corpus_collections_5

```

In this example we download the [OSCAR](https://oscar-corpus.com/post/oscar-v21-09/) corpus. Please note that this is also available as a [Hugging Face Dataset](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109). You can either contact the OSCAR authors to get access to the dataset, or you can download it from HuggingFace. Here we choose to download it from Huggingface. This does require you to log in and accept a disclaimer first. When you have done that, download the following files (since an authentication token is involed, you might have to do this from your browser and transfer the files to your server afterwards):

* [nn.txt.gz](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109/blob/main/packaged/nn/nn.txt.gz)
* [no_part_1.txt.gz](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109/resolve/main/packaged/no/no_part_1.txt.gz)
* [no_part_2.txt.gz](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109/resolve/main/packaged/no/no_part_2.txt.gz)
* [no_part_3.txt.gz](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109/resolve/main/packaged/no/no_part_3.txt.gz)
* [no_part_4.txt.gz](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109/resolve/main/packaged/no/no_part_4.txt.gz)
* [no_part_5.txt.gz](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109/resolve/main/packaged/no/no_part_5.txt.gz)

Make sure the files are named as above, and downloaded to the folder *corpus/source_1* before continuing.

```bash
#
cd ~
cd corpus/source_1/

# Unzip and rename files
zcat nn.txt.gz > oscar_nn.txt
zcat no*.txt.gz > oscar_nb.txt
rm *.gz
```
<details>
  <summary>A segment of corpus/source_1/oscar_nn.txt</summary>
 
```text
Bygda Ålfoten vart ein del av Bremanger kommune då Davik kommune vart delt i tre ved kommunereguleringa i 1964. (Foto: Arild Nybø, NRK)
I mellomalderen låg det ei kyrkje på Utvær. Utvær ligg åtte km vestanfor dei andre øyane i Solund, og er det vestlegaste punktet i Noreg som har vore busett. Kvifor vart det bygd eit gudshus bokstaveleg tala midt ute i havet?
```
  
</details>


## 2) Converting to json
For the OSCAR dataset, you will notice that there is a prepared create-script called [*create_oscar.py*](https://github.com/NBAiLab/notram/blob/master/corpus_generation_scripts/create_oscar.py) available in */home/user/notram/corpus_generation_scripts/create_oscar.py*. Documentation is available [here](https://github.com/NBAiLab/notram/blob/master/guides/create_scripts.md#create_oscarpy). The OSCAR dataset is in a simple txt-based format where double line breaks separates documents, and single line breaks separates paragraphs. There are multiple other create-scripts in the same directory, and if your dataset has another format (like pdf, xml, xhtml, json) it is likely that you can find another script to use as a starting point.

The goal of this script is to convert the external dataset to a structures [json-lines format](https://github.com/NBAiLab/notram/blob/master/guides/text_extraction_format.md) are used. format. This 

```bash
cd ~

# Convert the source files to json
# Running nynorsk file indicates how long it will take running the 60 times larger Bokmål file

python notram/corpus_generation_scripts/create_oscar.py --language_reported nn --doc_type oscar_nn --input_file corpus/source_1/oscar_nn.txt --output_file corpus/json_2/oscar_nn.json

python notram/corpus_generation_scripts/create_oscar.py --language_reported nb  --doc_type oscar_nb --input_file corpus/source_1/oscar_nb.txt --output_file corpus/json_2/oscar_nb.json

```


<details>
  <summary>One line of corpus/json_2/oscar_nn.json</summary>

  ```json
 
  {
  "doc_type": "oscar_nn",
  "id": "oscar_nn_2",
  "language_reported": "nn",
  "paragraphs": [
    {
      "paragraph_id": 0,
      "text": "Bygda Ålfoten vart ein del av Bremanger kommune då Davik kommune vart delt i tre ved kommunereguleringa i 1964. (Foto: Arild Nybø, NRK)"
    },
    {
      "paragraph_id": 1,
      "text": "I mellomalderen låg det ei kyrkje på Utvær. Utvær ligg åtte km vestanfor dei andre øyane i Solund, og er det vestlegaste punktet i Noreg som har vore busett. Kvifor vart det bygd eit gudshus bokstaveleg tala midt ute i havet?"
    }
  ]
}
  
```
  
</details>

## 3) Cleaning and Deduplication
The problem with using web based sources for training languge models is that they contain a lot of noise. Typical examples is long product lists that are not really language and considerable amount of machine generated text. The OSCAR corpus is considerably more cleaned than for instance MC4, but we still apply our cleaning procedure also on this corpus.

The cleaning routines are defined in separate config-files. These can be adapted to the specific source. Cleaning procedures for OCR-based texts are usually different from digitally born texts. Here we are using a config.script from the notram-repository. You can of course make your own config-file and refer to this instead. The cleaning also does a few other tricks: It calculates the document length and a hash for each of the paragraphs. This speeds up the process of deduplicating across the corpuses.

```bash
cd ~ 

# Run the clean scripts
# Here you could also use the Nynorsk to get an estimate of how long the Bokmål script will take

python notram/corpus_generation_scripts/clean.py --input_file corpus/json_2/oscar_nn.json --output_folder corpus/clean_json_3 --config_file notram/corpus_generation_scripts/config/config.json

python notram/corpus_generation_scripts/clean.py --input_file corpus/json_2/oscar_nb.json --output_folder corpus/clean_json_3 --config_file notram/corpus_generation_scripts/config/config.json
```

<details>
  <summary>One line of corpus/clean_json_3/oscar_nn.json</summary>

  ```json
 
{
  "doc_type": "oscar_nn",
  "id": "oscar_nn_2",
  "publish_year": 2021,
  "doc_length": 360,
  "paragraphs": [
    {
      "paragraph_id": 0,
      "text": "Bygda Ålfoten vart ein del av Bremanger kommune då Davik kommune vart delt i tre ved kommunereguleringa i 1964. (Foto: Arild Nybø, NRK)",
      "hash": "0022d3206973366fc86dc83bb3718757"
    },
    {
      "paragraph_id": 1,
      "text": "I mellomalderen låg det ei kyrkje på Utvær. Utvær ligg åtte km vestanfor dei andre øyane i Solund, og er det vestlegaste punktet i Noreg som har vore busett. Kvifor vart det bygd eit gudshus bokstaveleg tala midt ute i havet?",
      "hash": "30743e4da2e8120bba8fa7576f60f082"
    }
  ]
}
  
```
  
</details>


## 4) Standardisation and cross corpus deduplication
Often we will have a lot of small corpuses that we want to combine. The last step has multiple steps. Firstly it strips away any unnecessary meta-data and standardises for instance date formet. It then uses Fasttext to do language detection based on the text. Please refer to the Fasttext pages for how to install this. In the end it runs deduplication across all corpuses, and keeps the paragraphs in the longest documents. 

To have full flexibility on what to include in the final corpuses, this script requires specification of what files to be included. The file is *corpus\_files\_4/filelist.txt* is a text file with absolute paths. 


```bash
cd ~ 

# Generate the file list
# In this case it will be just our two files
# Note that the parameter to ls here is the number "1" and not the letter "l"

ls -1 corpus/clean_json_3/*.* > corpus/corpus_files_4/filelist.txt

# You can of course edit this file before proceding

python notram/corpus_generation_scripts/corpus_files_builder.py --corpus_output_dir corpus/corpus_files_4/

```

<details>
  <summary>One line of corpus/corpus_files_4/oscar_nn.json</summary>

  ```json
 {
  "id": "oscar_nn_2000",
  "doc_type": "oscar_nn",
  "publish_year": 2021,
  "lang_fasttext": "nn",
  "lang_fasttext_conf": "0.823",
  "text": "Men skal ein forhandle, må det også vere forhandlingsvilje. Og evne til å både skape og utnytte eit forhandlingsrom. Partane må, ikkje minst i eit hovudoppgjer, vurdere situasjonen både på kort og lang sikt. Store delar av offentleg sektor står i ein heilt annan situasjon enn industrien og ein del andre næringar. I offentleg sektor er det ikkje mangel på arbeid og oppgåver. Det som manglar er folk med nødvendig utdanning og kompetanse."
}
  
```
  
</details>

## 5) Creating the dataset
In the final step we collate the corpuses, shuffle them and then create a train and validation file. For uploading this to Huggingface, please look at **THIS GUIDE**. 

```bash
cd ~ 

# Run the corpus file creator
**FREDDY**

python notram/corpus_generation_scripts/dataset_builder.py --input_folder corpus/corpus_files_4/ --corpus_output_dir corpus/corpus_collections_5/

**FREDDY input_folder
**FREDDY Hvorfor ikke bare --output_folder som brukes i de andre scriptene....?


