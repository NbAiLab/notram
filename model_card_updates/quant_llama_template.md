---
base_model: "{{ base_model_name }}"
tags:
- llama-cpp
- gguf
- quantization
---

# {{ model_name }}
This model is a **quantized** version of the original [{{ base_model_name }}]({{ base_model_link }}), converted into the **GGUF format** using [llama.cpp](https://github.com/ggerganov/llama.cpp). Quantization significantly reduces the model's memory footprint, enabling efficient inference on a wide range of hardware, including personal devices, without compromising too much quality. These quantized models are mainly provided so that people can test out the models with moderate hardware. If you want to benchmark the models or further finetune the models, we strongly recommend the non-quantized versions. 

## What is `llama.cpp`?
[`llama.cpp`](https://github.com/ggerganov/llama.cpp) is a versatile tool for running large language models optimized for efficiency. It supports multiple quantization formats (e.g., GGML and GGUF) and provides inference capabilities on diverse hardware, including CPUs, GPUs, and mobile devices. The GGUF format is the latest evolution, designed to enhance compatibility and performance.

## Benefits of This Model
- **High Performance**: Achieves similar quality to the original model while using significantly less memory.
- **Hardware Compatibility**: Optimized for running on a variety of hardware, including low-resource systems.
- **Ease of Use**: Seamlessly integrates with `llama.cpp` for fast and efficient inference.

## Installation
Install `llama.cpp` using Homebrew (works on Mac and Linux):

```bash
brew install llama.cpp
```

## Usage Instructions

### Using with `llama.cpp`
To use this quantized model with `llama.cpp`, follow the steps below:

#### CLI:
```bash
llama-cli --hf-repo {{ model_id }} --hf-file {{ quantized_model_filename }} -p "Your prompt here"
```

#### Server:
```bash
llama-server --hf-repo {{ model_id }} --hf-file {{ quantized_model_filename }} -c 2048
```

For more information, refer to the [llama.cpp repository](https://github.com/ggerganov/llama.cpp).

## Additional Resources
- [Original Model Card]({{ base_model_link }})
- [llama.cpp Repository](https://github.com/ggerganov/llama.cpp)
- [GGUF Format Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/llama)
