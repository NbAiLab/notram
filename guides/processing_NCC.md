# Processing the NCC
This document gives an overview of how the NCC is processed. The document links to guides with the exact steps that needs to be performed to recreate the NCC.

## Processing structure

1) Source files
NCC is composed from multiple sources in various formats. At the "source file"-level the files are stored as close to the original format as possibly.

2) Json files
The corpus is then converted to a common json-lines format. In general all relevant information from the source files are kept but they are converted to a common format for reading. In general we are striving to have one document per line, separate paragraphs. The json-format does not limit the tags that can be used, however, it recommends that if possible the following JSON STANDARD is used. 
