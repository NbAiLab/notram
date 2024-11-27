import os
from huggingface_hub import HfApi
from jinja2 import Template

# Read the Hugging Face token from an environment variable
HF_TOKEN = os.environ.get('HF_TOKEN')
if not HF_TOKEN:
    print("Please set the HF_TOKEN environment variable.")
    exit(1)

# Load the model card template
with open('quant_llama_template.md', 'r') as file:
    model_card_template = file.read()

# Define the base and quantized models
base_models = [
    {
        "model_id": "north/nb-llama-3.2-3B",
        "model_name": "NB-Llama-3.2-3B",
        "base_model_name": "Llama-3.2-3B",
        "base_model_link": "https://huggingface.co/north/nb-llama-3.2-3B",
        "parameter_count": "3 billion",
        "version": "3.2"
    },
    {
        "model_id": "north/nb-llama-3.2-1B",
        "model_name": "NB-Llama-3.2-1B",
        "base_model_name": "Llama-3.2-1B",
        "base_model_link": "https://huggingface.co/north/nb-llama-3.2-1B",
        "parameter_count": "1 billion",
        "version": "3.2"
    },
    {
        "model_id": "north/nb-llama-3.1-8B",
        "model_name": "NB-Llama-3.1-8B",
        "base_model_name": "Llama-3.1-8B",
        "base_model_link": "https://huggingface.co/north/nb-llama-3.1-8B",
        "parameter_count": "8 billion",
        "version": "3.1"
    },
    {
        "model_id": "north/nb-llama-3.1-70B",
        "model_name": "NB-Llama-3.1-70B",
        "base_model_name": "Llama-3.1-70B",
        "base_model_link": "https://huggingface.co/north/nb-llama-3.1-70B",
        "parameter_count": "70 billion",
        "version": "3.1"
    }
]

# Generate quantized models
quantized_models = []
for base_model in base_models:
    quantized_models.append({
        "model_id": f"{base_model['model_id']}-Q4_K_M-GGUF",
        "model_name": f"{base_model['model_name']}-Q4_K_M-GGUF",
        "base_model_name": base_model['model_name'],
        "base_model_link": base_model['base_model_link'],
        "quantized_model_filename": f"{base_model['model_name'].lower()}-q4_k_m.gguf"
    })

# Initialize the Hugging Face API
api = HfApi()

for model in quantized_models:
    try:
        # Fill in the template
        template = Template(model_card_template)
        model_card_content = template.render(**model)
        # Upload the README.md file directly to the repo
        repo_id = model['model_id']
        api.upload_file(
            path_or_fileobj=model_card_content.encode('utf-8'),
            path_in_repo="README.md",
            repo_id=repo_id,
            token=HF_TOKEN,
        )
        print(f"Successfully updated README.md for {repo_id}")
    except Exception as e:
        print(f"Failed to update {model['model_id']}: {e}")
        continue
