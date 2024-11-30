#!/bin/bash

# Define an array with the script names
scripts=(
    "update_dpo_llama_model_cards.py"
    "update_dpo_quant_model_cards.py"
    "update_llama_model_cards.py"
    "update_quant_model_cards.py"
    "update_sft_llama_model_cards.py"
    "update_sft_quant_model_cards.py"
)

# Loop through the scripts and run each one
for script in "${scripts[@]}"; do
    echo "Running $script..."
    python "$script"
    if [ $? -ne 0 ]; then
        echo "Error: $script failed to run." >&2
        exit 1
    fi
done

echo "All scripts ran successfully."
