# Overview - Processing the NCC
This document gives an overview of how the [NCC](corpus_description.md) is processed. The document links to guides with the exact steps that needs to be performed to recreate the NCC. There is also a practical [step-by-step guide](step_by_step_guide.md) for how to build this corpus.

## Processing Structure

### **Source files**. NCC is composed from multiple sources in various formats. At the "source file"-level the files are stored as close to the original format as possibly.
<details>
  <summary>Example source format</summary>
 
```text
Bygda Ålfoten vart ein del av Bremanger kommune då Davik kommune vart delt i tre ved kommunereguleringa i 1964. (Foto: Arild Nybø, NRK)
I mellomalderen låg det ei kyrkje på Utvær. Utvær ligg åtte km vestanfor dei andre øyane i Solund, og er det vestlegaste punktet i Noreg som har vore busett. Kvifor vart det bygd eit gudshus bokstaveleg tala midt ute i havet?
```
  
</details>

2) **Json files**. The corpus is then converted to a common json-lines format. In general all relevant information from the source files are kept but they are converted to a common format for reading. In general we are striving to have one document per line, separate paragraphs. The json-format does not limit what keys can be used since this depends on the source, however, it recommends that if possible the following [json keys](json_format.md) are used. Please see the following [documentation](create_scripts.md) for the set of scripts provided to convert specific source files to json.

<details>
  <summary>Example json-format</summary>

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

3) **Clean json files**. At this stage the files are cleaned and standardised. All documents are still on a paragraph level. Please see the [description of cleaning rules](cleaning_rules_description.md) that are applied. The cleaning procedure does differ between the sources. The sub-corpora are deduplicated internally on paragraph level.

<details>
  <summary>Example clean json format</summary>

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

4) **Collation and deduplication**. At this stage paragraphs are collated, fasttext-language detections are performed and the keys are standardised and reduced. 
<details>
  <summary>Example corpus file format</summary>

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

5) **Training dataset**. In the end training dataset are created from the corpus files. These corpuses can be in multiple formats (tfds, json, huggingface datasets etc) depending on the use. 
