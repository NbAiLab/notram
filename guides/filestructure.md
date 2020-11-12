# PPL - paragraph-per-line
- Filename structure: newspapers_1980_1989_nno/nob/bn_170520.txt
- (corpus name)_time periode_nynorsk/bokmål/bokmål+nynorsk_date.txt
- Try to hold a 10 year perspective on the bulks of files
- Use UTF-8
- Remove all \r and \t
- Include "digibok_id...." on a single line followed by the article
- Separate all parapraphs with \n

# SPL - Sentence-per
- \n after each sentence
- \n\n after each paragraph
- Randomized
- Deduplicated on paragraph level
- Remove all articles shorter than 3 words



# Old files
Contains a backup of downloaded corpora. Raw format. No changes are done to these files.

| File  |  Size | Description | Original Link | Comments |
| -------- |  ----- | -------- | -------- | -------- |
| [nob.wikipedia.json](https://console.cloud.google.com/storage/browser/nortram-west4/rawfiles/nob.wikipedia.json) | 1.3Gb | Norwegian Wikipedia Bokmål 20. mars 2019| [NB Språkbanken](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/)| Description of structure available in [2019_wikipedia.pdf](https://www.nb.no/sbfil/dok/2019_wikipedia.pdf)|
| [nno.wikipedia.json](https://console.cloud.google.com/storage/browser/nortram-west4/rawfiles/nno.wikipedia.json) | 295Mb | Norwegian Wikipedia Nynorsk 20. mars 2019| [NB Språkbanken](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/)| Description of structure available in [2019_wikipedia.pdf](https://www.nb.no/sbfil/dok/2019_wikipedia.pdf) |
| [nno.wikipedia.json](https://console.cloud.google.com/storage/browser/nortram-west4/rawfiles/sme.wikipedia.json) | 11Mb | Norwegian Wikipedia Sami 20. mars 2019| [NB Språkbanken](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-50/)| Description of structure available in [2019_wikipedia.pdf](https://www.nb.no/sbfil/dok/2019_wikipedia.pdf) |
| [norsk_aviskorpus.zip](https://console.cloud.google.com/storage/browser/nortram-west4/rawfiles/norsk_aviskorpus.zip) | 2.7Gb | Norwegian Newspaper Copus | [NB Språkbanken](https://www.nb.no/sprakbanken/ressurskatalog/oai-clarino-uib-no-avis-plain/)| The Norwegian Newspaper Corpus (NNC) Bokmål version is a large monitor corpus representing contemporary Norwegian language in the written variety Norwegian Bokmål. This is partly parsed. Waiting for a new version. Ref Arne Martinus Linstad |
| [parliament_speeches_1998_2016.csv](https://console.cloud.google.com/storage/browser/nortram-west4/rawfiles/norsk_aviskorpus.zip) | 841Mb | Talk of Norway | [Clarino](https://repo.clarino.uib.no/xmlui/handle/11509/123)| Talk of Norway is a collection of Norwegian Parliament speeches from 1998 to 2016. |




