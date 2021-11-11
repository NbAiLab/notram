[Needs More Information]

# Dataset Card for NBAiLab/<corpusname>

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
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
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Freddy wetjen][mailto:freddy.wetjen@nb.no]

### Dataset Summary

The <corpusname> dataset contains json lines with language training data. Here is an example json line:

{"id": "1006205", "doc_type": "cc100", "publish_year": 2021, "lang_fasttext": "nn", "lang_fasttext_conf": "0.641", "text": "Eg har en PLAN! KOS deg og ha en fortryllende herlig pinse :)"}



### Supported Tasks and Leaderboards

[Needs More Information]

### Languages
<languages>


## Dataset Structure

### Data Instances

{
"id": "1021619", 
"doc_type": "cc100", 
"publish_year": 2021, 
"lang_fasttext": "nn",
 "lang_fasttext_conf": "0.409",
 "text": "�Henry Melson Stommel� i Store norske leksikon, snl.no."
}


### Data Fields

Id: String with id to source of line and a unique identifier
doc_type: String describing type of media text extracted from (I.e. book,newspaper etc)
publish_year: String with year text pulished
lang_fasttext:String. language of text identified by fasttext
lang_fasttext_conf: String. Confidence
text: String. text

### Data Splits

[Needs More Information]

## Dataset Creation
The set is sharded into 1GB of uncompressed text, making it <nosplits> json-files for training, and 1 json-file for validation. The files are gzipped.
Build date: <builddate>
### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

We do not know anything of biases in the corpus

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

Freddy.wetjen@nb.no

### Licensing Information

Restricted license

### Citation Information

{
author = {Kummervold, Per E  and
  De la Rosa, Javier  and
  Wetjen, Freddy  and
  Brygfjeld, Svein Arne",
}
