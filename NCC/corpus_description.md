# Norwegian Colossal Corpus
This page summarizes the Norwegian Collossal Corpus. The corpus is a collection of multiple smaller Norwegian corpuses that are suitable for training large language models. We have done extensive cleaning on the datasets, and have made them available in a common format.


## Government Reports
A collection of documents and reports from the Norwegian government. The files are downloaded directly from the government API in a native xhtml-format that they use for creating both Word and pdf reports. In pre-processing typically headings, tables, footnotes etc are filtered out.

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|1.1 GB| ? | ? | ? |

<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 

</details>


## Parliament Collections
**NEED MORE TEXT HERE - WHO HAS COLLECTED THIS** Also referred to as Stortingsforhandlingene. Collection of documents from the Norwegian Parliament. The corpus contains mainly OCRed reports. Part of the collection at the National Library. 
| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|9.5 GB| ? | ? | ? |

<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 

</details>


## Pulic Reports
**NEED MORE TEXT HERE** Also referred to as __Evalueringsrapporter__. The corpus contains mainly OCRed reports. Part of the collection at the National Library. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|0.7 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>


## LovData CD
CD/DVD last published in 2005. Contains a very complete collection of legal resources, including laws, NOUs etc. The collection is now out of database protextion. We have cleaned out resources that might contain personal information. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|0.4 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>


## Målfrid Collection
A collection of more than 9.2M public documents in pdf-format from 311 different sources. Collected from Språkbanken. We are using the part that is possible to read as text (roughly 6M documents). The largest sources are ssb (1.5M), regjeringen (1M), Uio (1M), fylkesmannen (0.7M), nve (0.4M), ntnu (0.3M), patentstyret (0.2M), vegvesenen (0.2M), fhi (0.2M).

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|17.0 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>


## Newspapers
A large collection of out-of-copyright newspapers from the National Library of Norway. This collection both has OCR scanned newspapers, and newspapers that are delivered to the library as pdf and where we are able to extract the text directly.

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|17.0 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>



## Newspapers Online
 A Norwegian Newspaper Corpus with texts from online bokmål newspapers between 1998 and 2019 collected by Språkbanken. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|2.6 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>

## Books
A large collection of out-of-copyright books from the National Library of Norway. This is OCR scanned documents only. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|6.2 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>

## Subtitles
Norwegian subtitles from OpenSubtitles.
| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)|0.3 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>

## Wikipedia
A dump of Wikipedia downloaded 2021.06.20. The text is cleaned. The dump contains both Bokmål and Nynorsk, however this is marked in the corpus in the doc_type-tag. In addition there is automatic language detection by Fasttext that in most cases will overlap.

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)|0.9 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
### Document Types
only a placeholder for stats. 
</details>

## Web Corpora
Please also note that there are Norwegian Web Corpora available, most notably the [OSCAR](https://huggingface.co/datasets/oscar) and the [MC4](https://huggingface.co/datasets/mc4) dataset.  Both these sets have a Norwegian Bokmål and a Norwegian Nynorsk subset. MC4 is the largest set (70GB) but is fairly uncleaned with a significant part of machine generated text. The OSCAR set is smaller (**?**) but is better clened. Almost the entire OSCAR corpus is contained in MC4, so it is not recommented adding both. It might also be an alternative to add just a portion of MC4 because of its size and relatively low quality.

We are unable to redistribute these sets in this package however the datasets are in the same HuggingFace Dataset format and can easily be combined with these sets. 
