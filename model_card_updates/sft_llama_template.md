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
This is the SFT-version of the NB-Llama-models. This means the model has gone through supervised finetuning, and it now understands a basic template. Note that this model has not yet been aligned, so it will behave fairly unpredictable. It is most suited for additional fine tuning. 

**{{ model_name }}** is part of the **NB-Llama-{{ version }}** series of models, trained on top of [{{ base_model_name }}]({{ base_model_link }}). This multilingual generative model was fine-tuned specifically to support Norwegian Bokmål, Norwegian Nynorsk, and English, with partial support for Swedish and Danish.

The basic idea with this model series was to explore how current state-of-the-art models could be improved for Norwegian by training only on publicly available data. While these models are trained by the National Library of Norway, they do not include data only available through legal deposit. They do, however, contain public data like governmental reports that are both publicly available and legally deposited.

---

### Key Features

- **Base Model**: Built on {{ base_model_name }}.
- **Languages**:
  - Full support: Norwegian Bokmål (nb), Norwegian Nynorsk (nn), English (en).
  - Partial support: Swedish (sv), Danish (da).
- **Purpose**: Supports Norwegian-specific tasks such as question-answering, summarization, and language modeling, while being capable of multilingual generation and translation. Efforts have been made to preserve the English capabilities from the underlying Meta Llama model.
- **Training Data**: Combines publicly available multilingual datasets with synthetic data generation, focusing on Norwegian, English, Swedish, and Danish sources. Additional details are provided below.
- **Architecture**: The model uses the Llama {{ version }} architecture. It is an auto-regressive language model with an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and Direct Preference Optimization (DPO) for alignment.

---

### Model Details

- **Developer**: National Library of Norway (NB-AiLab).
- **Parameters**: {{ parameter_count }}.
- **Knowledge Cutoff**: May 2024.
- **License**: [Llama {{ version }} Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama{{ version }}/LICENSE).

---

### Motivation

The primary goal of **{{ model_name }}** is to advance support for Norwegian language technologies and strengthen support for Norwegian Bokmål and Norwegian Nynorsk. Since much knowledge and culture are also expressed in English, Swedish, and Danish, open sources in these languages are included in the training datasets when possible.

---

### Intended Use

#### Use Cases

- Dialogue systems.
- General multilingual text generation and language modeling.
- Norwegian-specific tasks such as:
  - Summarization of texts in Bokmål or Nynorsk.
  - Question-answering tailored to Norwegian cultural and linguistic contexts.

#### Out-of-Scope

- Use in violation of applicable laws or regulations.
- Tasks outside the supported languages without additional fine-tuning.
- High-risk domains without appropriate safety measures.

---

### How to Use

Please note tht this is still a research project, and the purpose of releasing the models are to investigate the potential in adapting these models for Norwegian language. The intented use case is experiemental. For end-users, we strongly recommend using the instruction-tuned models. We provide quantized models with close to the same accuracy that will run much faster on most platforms. When fine-tuning the instruction-tuned models, best results are obtained when applying the appropriate templates from Llama {{ version }}.

#### Using `transformers`

```python
import torch
from transformers import pipeline

model_id = "{{ model_id }}"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
messages = [
    {"role": "user", "content": "Hvem er du?"},
]
outputs = pipe(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])

```
---

### Training Data

**Overview:**

The training data is based entirely on publicly available datasets and synthetically generated data. A key aspect of the training process was leveraging high-quality knowledge sources in Norwegian, English, Swedish, and Danish.

Parts of the following publicly available datasets were used:

- [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)
- [High Performance Language Technologies (HPLT)](https://huggingface.co/datasets/HPLT/hplt_monolingual_v1_2)
- [Norwegian Colossal Corpus (NCC)](https://huggingface.co/datasets/NCC/Norwegian-Colossal-Corpus)
- [Wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia)

---

### Data Selection

To ensure the highest quality training data, only a small subset of the original raw data was used. An encoder-only classifier built on [nb-bert-base](https://huggingface.co/NbAiLab/nb-bert-base) was trained to evaluate both educational value and linguistic quality of the training samples.

- **Categorization Methods:**
  - Inspired by the [FineWeb](https://example.com/FineWeb) project.
  - Evaluated for:
    - **Educational Value:** Prioritizing high-value training samples.
    - **Linguistic Quality:** Ensuring clarity and accuracy in training data.
- **Guidance and Release:**
  - Categorization was guided by insights from [Gemini 1.5](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/#gemini-15).
  - The classifiers are released alongside this model and are [available here](https://classifier-release-link-here).

---

### Licensing

The model is released under the [Llama {{ version }} Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama{{ version }}/LICENSE), allowing for research and commercial use within defined limitations. Refer to the [Acceptable Use Policy](https://llama.meta.com/llama{{ version }}/use-policy) for specific restrictions.

---

### Citing & Authors
The model was trained and documentation written by Per Egil Kummervold.

---
