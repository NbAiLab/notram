# Processing the NCC
This document gives an overview of how the NCC is processed. The document links to guides with the exact steps that needs to be performed to recreate the NCC.

## Processing structure

1) Source files
NCC is composed from multiple sources in various formats. At the "source file"-level the files are stored as close to the original format as possibly.

2) Json files
The corpus is then converted to a common json-lines format. In general all relevant information from the source files are kept but they are converted to a common format for reading. In general we are striving to have one document per line, separate paragraphs. The json-format does not limit what keys can be used since this depends on the source, however, it recommends that if possible the following JSON KEYS are used. Please see the following DESCRIPTION for the set of scripts are provided to convert specific source files to json.

3) Clean json files
At this stage the files are cleaned and standardised. All documents are still on a paragraph level. Please see the DESCRIPTION for a list of cleaning rules that are applied. The cleaning procedure does differ between the sources. The sub-corpora are deduplicated internally om paragraph level.

4) Collation and deduplication
At this stage paragraphs are collated, fasttext-language detections are performed and the keys are standardised and limited. See a HERE FOR A DESCRIPTION OF THE FILE FORMAT.

5) Training corpuses
In the end training corpuses are created from the corpus files. These corpuses can be in multiple formats (tfds, json, huggingface datasets etc) depending on the use.

