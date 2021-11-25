[<img align="right" width="150px" src="../images/nblogo.png">](https://ai.nb.no)

# Overview - Processing the NCC
This is a short overview of how the [NCC](corpus_description.md) is processed. The document links to guides with the exact steps that needs to be performed to recreate the NCC. There is also a more thorough practical [step-by-step guide](step_by_step_guide.md) for how to build this corpus. 
## Processing Structure

<img align="center" width="800px" src="../images/bilderavsteg.png">

1) **Source files**. NCC is composed from multiple sources in various formats. At the "source file"-level the files are stored as close to the original format as possibly.

2) **Json files**. The corpus is then converted to a common json-lines format. In general all relevant information from the source files are kept but they are converted to a common format for reading. In general we are striving to have one document per line, separate paragraphs. The json-format does not limit what keys can be used since this depends on the source, however, it recommends that if possible the following [json keys](json_format.md) are used. Please see the following [documentation](create_scripts.md) for the set of scripts provided to convert specific source files to json.

3) **Clean json files**. At this stage the files are cleaned and standardised. All documents are still on a paragraph level. Please see the [description of cleaning rules](cleaning_rules_description.md) that are applied. The cleaning procedure does differ between the sources. The sub-corpora are deduplicated internally on paragraph level.

4) **Collation and deduplication**. At this stage paragraphs are collated, fasttext-language detections are performed and the keys are standardised and reduced. 

5) **Training dataset**. In the end training dataset are created from the corpus files. These corpuses can be in multiple formats (tfds, json, huggingface datasets etc) depending on the use. 

---
<img width="150px" src="../images/Nasjonalbiblioteket.jpg"> <sup> - written by __Per Egil Kummervold__</sup>
