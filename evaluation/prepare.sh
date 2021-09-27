#!/bin/bash

NAME="$1"
CHECKPOINT="$2"
LANG="$3"
CASE="$4"
CONFIG="${5:-base}"
MODEL=`basename $2`

mkdir -p "checkpoints/$NAME"
gsutil -m cp -r "${CHECKPOINT}*" "checkpoints/$NAME"
cp "configs/bert_config_${CONFIG}_${LANG}_${CASE}.json" "checkpoints/$NAME/config.json"
cp "tokenizers/${LANG}_${CASE}_tokenizer_config.json" "checkpoints/$NAME/tokenizer_config.json"
cp "vocabs/${LANG}_${CASE}_vocab.txt" "checkpoints/$NAME/vocab.txt"
python convert_tf2_to_pytorch_pretrain.py \
  --tf_checkpoint_path "checkpoints/$NAME/$MODEL" \
  --bert_config_file "checkpoints/$NAME/config.json" \
  --output_folder "checkpoints/$NAME"
python -c "from transformers import TFAutoModelForPreTraining as TFA; TFA.from_pretrained('checkpoints/$NAME', from_pt=True).save_pretrained('checkpoints/$NAME')"
