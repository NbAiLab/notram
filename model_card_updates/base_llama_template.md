---
language:
- no  # Generic Norwegian
- nb  # Norwegian Bokmål
- nn  # Norwegian Nynorsk
- en  # English
- sv  # Swedish
- da  # Danish
tags:
- norwegian
- bokmål
- nynorsk
- swedish
- danish
- multilingual
- text-generation
pipeline_tag: text-generation
license: llama{{ version }}
---

## Model Card: {{ model_name }}

---

### Model Overview

**{{ model_name }}** is part of the **NB-Llama-{{ version }}** series of models, trained on top of [{{ base_model_name }}]({{ base_model_link }}). This multilingual generative model was fine-tuned specifically to support Norwegian Bokmål, Norwegian Nynorsk, and English, with partial support for Swedish and Danish. 

The basic idea with this model series was to explore how current SOTA models could be improved for Norwegian by training only on publicly available data. While these models are trained by the National Library of Norway, they do not include data only available through the legal deposit. They do, however, contain public data like governmental reports that are both publicly available and legally deposited.

---

### Key Features

- **Base Model**: Built on {{ base_model_name }}.
- **Languages**: 
  - Full support: Norwegian Bokmål (nb), Norwegian Nynorsk (nn), English (en).
    - Partial support: Swedish (sv), Danish (da).
    - **Purpose**: Supports Norwegian-specific tasks such as question-answering, summarization, and language modeling, while being capable of multilingual generation and translation. We have tried to preserve the English capabilities from the underlying Meta Llama model.
    - **Training Data**: Combines publicly available multilingual datasets with synthetic data generation, focusing on English, Swedish, and Danish sources. Additional details are given below. 
    - **Architecture**: The model uses the Llama {{ version }} architecture. It is an auto-regressive language model with an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and Direct Preference Optimization (DPO) for alignment.

    ---

    ### Model Details

    - **Developer**: National Library of Norway (NB-AiLab).
    - **Parameters**: {{ parameter_count }}.
    - **Training Data**: 
      - **Sources**: Publicly available datasets in English, Swedish, and Danish, enhanced with synthetic data generation.
        - **Categorization**: Inspired by the FineWeb project, an encoder-only classifier was trained using [nb-bert-base](https://huggingface.co/NbAiLab/nb-bert-base) to evaluate both educational value and linguistic quality in the training samples. Categorization was guided by [Gemini 1.5](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/#gemini-15), and the classifiers are [available here](https://classifier-release-link-here).
        - **Knowledge Cutoff**: May 2024.
        - **License**: [Llama {{ version }} Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama{{ version }}/LICENSE).

        ---

        ### Motivation

        The primary goal of **{{ model_name }}** is to advance support for Norwegian language technologies and strengthen support for Norwegian Bokmål and Norwegian Nynorsk. Much knowledge and culture are also similarly expressed in English, Swedish, and Danish, and when possible, open sources in these languages are included in the training datasets.

        ---

        ### Intended Use

        #### Use Cases
        - Dialogue systems.
        - Norwegian-specific tasks such as:
          - Summarization of texts in Bokmål or Nynorsk.
            - Question-answering tailored to Norwegian cultural and linguistic contexts.
              - Fine-tuning for public-sector or educational applications.
              - General multilingual text generation and language modeling.

              #### Out-of-Scope
              - Use in violation of applicable laws or regulations.
              - Tasks outside the supported languages without additional fine-tuning.
              - High-risk domains without appropriate safety measures.

              ---

              ### How to Use

              For end-users, we strongly recommend using the instruction-tuned models. We provide quantized models with close to the same accuracy that will run much faster on most platforms. When fine-tuning the instruction-tuned models, best results are obtained when applying the appropriate templates from Llama {{ version }}.

              #### Using `transformers`

              ```python
              import transformers

              model_id = "{{ model_id }}"

              pipeline = transformers.pipeline(
                  "text-generation", 
                      model=model_id, 
                          model_kwargs={"torch_dtype": "bfloat16"}, 
                              device_map="auto"
                              )

                              output = pipeline("Hva er Nasjonalbibliotekets rolle i AI-utvikling?")
                              print(output)
               ```
       ### Training Data

       **Overview:**  
       The training data is based entirely on publicly available datasets and synthetically generated data. A key aspect of the training process was leveraging high-quality knowledge sources in English, Swedish, and Danish.
       
       Parts of the following publicly available datasets where used:
       * [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)
       * [Wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia)
       * [High Performance Language Technologies (HPLT)](https://huggingface.co/datasets/HPLT/hplt_monolingual_v1_2)
       * [Norwegian Colossal Corpus (NCC)](https://huggingface.co/datasets/uonlp/CulturaX)
       * [Wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia)

       ---

       ### Data Selection

       **Selection:**  
       - Only a small subset of the original raw data was used. To select the most useful data, we trained an encoder-only classifier built on [nb-bert-base](https://github.com/NbAiLab/nb-bert-base).

       - Categorization methods were inspired by [FineWeb](https://example.com/FineWeb) and evaluated for:  
         - **Educational Value:** To prioritize high-value training samples.  
           - **Linguistic Quality:** Ensuring clarity and accuracy in training data.

           - These classifiers, trained using insights from [Gemini 1.5](https://example.com/Gemini1.5), are released alongside this model.

           ---

           ### Licensing

           The model is released under the [Llama {{ version }} Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama{{ version }}/LICENSE), allowing for research and commercial use within defined limitations. Refer to the [Acceptable Use Policy](https://llama.meta.com/llama{{ version }}/use-policy) for specific restrictions.

