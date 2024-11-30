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

The Instruct-model is trained using Supervised FineTuning (SFT) and then Direct Preference Optimalisation (DPO). The SFT training is based on synthetic datasets, the English [Magpie](https://huggingface.co/Magpie-Align) dataset and a translated/filtered version of this dataset. The DPO training is based on [Anthropics Helpful and Harmless](https://huggingface.co/datasets/Anthropic/hh-rlhf) dataset. The training is supposed to be fairly basic, giving the models a decent undertstanding of a chat template. 

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

For SFT and DPO the following data were used:
- [Magpie](https://huggingface.co/Magpie-Align)
- [Anthropics Helpful and Harmless](https://huggingface.co/datasets/Anthropic/hh-rlhf)
- Various synthetic and translated datasets
- See [{{ base_model_name }}]({{ base_model_link }}) for more details on the pretraining data and data selection

---

### Licensing

The model is released under the [Llama {{ version }} Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama{{ version }}/LICENSE), allowing for research and commercial use within defined limitations. Refer to the [Acceptable Use Policy](https://llama.meta.com/llama{{ version }}/use-policy) for specific restrictions.

---

### Citing & Authors
The model was trained and documentation written by Per Egil Kummervold. 
