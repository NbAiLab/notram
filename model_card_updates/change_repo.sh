#!/bin/bash

# Find all .py files and replace 'north/' with 'NbAiLab/' in-place
for file in *.py; do
    sed -i 's|north/|NbAiLab/|g' "$file"
    echo "Updated $file"
done

echo "All *.py files have been updated."
