# Dataset Card for NBAiLab/<corpusname>

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Data Fields](#data-fiels)
- [Dataset Creation](#dataset-creation)
- [Statistics](#statistics)
  - [Document Types](#document-types)
  - [Languages](#languages)
  - [Publish Periode](#publish-periode)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description
- **Homepage:** https://github.com/NBAiLab/notram
- **Repository:** https://github.com/NBAiLab/notram
- **Paper:** https://arxiv.org/abs/2104.09617
- **Point of Contact:** [Freddy Wetjen](mailto:freddy.wetjen@nb.no)

<description>

## How to Use
```python
from datasets import load_dataset
data = load_dataset("NBAiLab/<corpusname>", streaming=True)
```
## Download Data
If you do not want to use the HuggingFace Dataset-library for training, or if you want to do additional pre-processing, it is also possible to download the files locally.
```bash
# Download all files in one batch operation

for i in $(seq -f "%04g" 1 <nosplits>): do wget https://huggingface.co/datasets/NbAiLab/<corpusname>/blob/main/data/train-shard-$i-of-<nosplitszeropadded>.json.gz &; done
# Create one large training file of all shards without unpacking
cat *.gz > onefile.json.gz
```

<details>
<summary>List of all the files.</summary>
<filelist>
</details>

### Dataset Summary
The <corpusname> dataset contains json lines with language training data. Here is an example json line:
```json
{ 
  "id": "1006205", 
  "doc_type": "cc100",
  "publish_year": 2021,
  "lang_fasttext": "nn",
  "lang_fasttext_conf": "0.641",
  "text": "Eg har ein PLAN! KOS deg og ha ei fin helg"
}
```
## Data Fields
|**id:** | String with id to source of line and a unique identifier|
|:-----------|:------------|
|**doc_type ** | String describing type of media text extracted from (I.e. book,newspaper etc)|
|**publish_year ** | Integer. The year text published. When year is undetermined it is set to 2021.|
|**lang_fasttext ** | String. Language of text identified by FastText|
|**lang_fasttext_conf ** | String. Confidence calculated by FastText|
|**text ** | String. The complete utf-8 document. If longer than 1M characters it is split.|

### Dataset Creation
We are providing a **train** and a **validation** split. The standard size of the validation is a single 1GB file, while train is sharded in 1GB chunks. 
All files are gzipped.

Build date: <builddate>

#### Initial Data Collection and Curation
The procedure for the dataset creation is described in detail in our paper.

<stats>

## Considerations for Using the Data
This corpus contains data under copyright and is not allowed to be used outide the National Library of Norway. The dataset should not be distributed.

### Discussion of Biases
Please refer to our paper.

### Dataset Curators
Freddy.wetjen@nb.no
Per.Kummervold@nb.no

### Licensing Information
Not lisenced for use outside the National Library of Norway.

<license>

### Citation Information
We are preparing an article with detailed information about this corpus. Until it is published, please cite out paper discussing the first version of this corpus:
```
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
```
