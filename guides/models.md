# Models

## NoTram mBERT
We are using the **multi_cased_L-12_H-768_A-12** model as the base model. This is basically a BERT Base model where the vocabulary is extended to 119,547 tokens. The original model is trained on 104 languages. This is the exact configuration:
```bash
{
  "attention_probs_dropout_prob": 0.1, 
  "directionality": "bidi", 
  "hidden_act": "gelu", 
  "hidden_dropout_prob": 0.1, 
  "hidden_size": 768, 
  "initializer_range": 0.02, 
  "intermediate_size": 3072, 
  "max_position_embeddings": 512, 
  "num_attention_heads": 12, 
  "num_hidden_layers": 12, 
  "pooler_fc_size": 768, 
  "pooler_num_attention_heads": 12, 
  "pooler_num_fc_layers": 3, 
  "pooler_size_per_head": 128, 
  "pooler_type": "first_token_transform", 
  "type_vocab_size": 2, 
  "vocab_size": 119547
}
```

After a hyperparameter search, the following settings were chosen for training on a TPU v3-8:

```bash
RUN_PREFIX=notram_mBERT_2760_4e4 
TRAIN_BATCH_SIZE=2760
NUM_EPOCHS=50
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=4e-4
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=10000
WARMUP_STEPS=10000
OPTIMIZER_TYPE=lamb
INIT_WEIGHTS=False

then

RUN_PREFIX=notram_mBERT_2760_4e4 
TRAIN_BATCH_SIZE=2760
NUM_EPOCHS=50
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=4e-4
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=2000?
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_WEIGHTS=False

then

RUN_PREFIX=notram_mBERT_2760_4e4 
TRAIN_BATCH_SIZE=2760
NUM_EPOCHS=50
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=5000
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_WEIGHTS=False
```

```bash
Model url:
Training time:
MLM Accuracy:
MLM Loss:
NSP Accuracy:
NSP Loss:

```
## NoTram Devlin 
Same corpus and training time as above. Based on recommended settings in Devlin. Randomly initiated weights.

```bash
RUN_PREFIX=notram_devlin_256_1e4_adam 
TRAIN_BATCH_SIZE=256
NUM_EPOCHS=50
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=1e-4
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=10000
WARMUP_STEPS=10000
OPTIMIZER_TYPE=adam
INIT_WEIGHTS=True
```

## NoTram Devlin mBERT
Same corpus and training time as above. Based on recommended settings in Devlin. Weights initiated from mBERT

```bash
RUN_PREFIX=notram_devlin_mbert_256_2e5_decay
TRAIN_BATCH_SIZE=256
NUM_EPOCHS=50
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=2e-5
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=10000
WARMUP_STEPS=0
OPTIMIZER_TYPE=adam
INIT_WEIGHTS=False
```

# Corpus v1
```bash
{
    "counts": {
        "default": {
            "num_documents": 40810085,
            "num_instances": 1216064986
        }
    },
    "time_taken_min": 836.8924871484438,
    "run_name": "notram_v1",
    "max_seq_length": 128,
    "model_class": "bert_multi_cased",
    "dupe_factor": 3,
    "gzipped": false,
    "short_seq_prob": 0.1,
    "max_predictions_per_seq": 19,
    "random_seed": 42,
    "masked_lm_prob": 0.15,
    "num_logged_samples": 10,
    "max_num_cpus": 40,
    "data_dir": "/disk4/folder1/nancy/content/text/v3/sentence_segm_5/split100MB/",
    "output_dir": "/disk4/folder1/nancy/content/text/v3/tfrecords_6/bert_multi_seq128_dup3/",
    "vocab_dir": "/disk4/folder1/nancy/content/text/v3/",
    "run_in_parallel": true
}
'bert_multi_cased': {
            'bucket_location': 'pretrained_models/bert/keras_bert/multi_cased_L-12_H-768_A-12',
            'hub_url': 'tensorflow/bert_multi_cased_L-12_H-768_A-12/2',
            'config': 'bert_config_multi_cased.json',
            'is_tfhub_model': True,
            'vocab_file': 'vocab.txt',
            'lower_case': False,
            'do_whole_word_masking': True
            }

```
## Summary
| <!-- -->   | <!-- -->  | 
| -------- |  -----:| 
|Size |1,890 TB|
|Training time | - |
|Dupe factor | 6 |
|Training examples| 2,432,129,972 |
|Vocabulary| 119.547|
