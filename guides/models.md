# Models and Training Set
The basic design is to train the same number of iterations as the original BERT model is trained. There will be a model with maximum batch size and [the lamb optimizer](https://arxiv.org/pdf/1904.00962.pdf). This will be compared to two standard BERT Base as described in [Devlin & al](https://www.aclweb.org/anthology/N19-1423.pdf). One with a typical 1e-4 learning rate, and one with the 2e-5 that is [recommended](https://github.com/google-research/bert#pre-training-tips-and-caveats) when you continue from an existing BERT checkpoint.

### Devlin
Devlin & al use a batch size of 256. They mix the sequence length and train 90% at sequence length 128 and 10% at sequence length 512. 

They claim to have trained 1,000,000 iterations at batch size 256, meaning they trained 900,000 at sequence length 128 and 100,000 at sequence length 512. They do not seem to adjust learning rate and batch size but they probably do not have to since they have plenty of memory. 

They have a 3.3 B word corpus and say that 1,000,000 iterations equals 40 epochs on this corpus.

### NoTram mBERT
Our corpus is 18.4 B words.

When we are using sequence length 128 we are able to generate a corpus of 405,354,995 examples from one epoch. 

To train 900.000 steps with a batch size of 2,760 means we need 2,484,000,000 training examples. This is equivalent to 6,1 epochs on our corpus, so a dup_factor of 6 is fine. 

After that we train 100.000 steps with a sequence length of 512. We will then need 276,000,000 training examples, but we are only able to make 101,338,748 from one epoch (since the sequence length is 4X as long). We should therefore generate a dataset equivalent to 2,7 epochs. A dupe_factor of 3 is sufficient. 

We use a slight alteration of this, since we want to train at max learning rate for longer. We also extend the warmup since we are continuing from pretrained weights. We train at maximum batch size for all sequence lengths and do linear scaling of the learning rate.
50k warmup 0 -> 4e-4 @ 128 - BS 2760
650k - fixed 4e-4 @ 128 - BS 2760
100k - fixed 1e-4 @ 512 - BS 688
200k - decaying 4e-4 -> 0 @128 - BS 2760

A control to see if this is done correctly, is to calculate the size of our corpus compared to Devlin's corpus. In total we are training for 6.1+2.7=8.8 epochs. At the same time our corpus is 5.6 times larger. If we trained for an equivalent number of training examples on Devlin's corpus it would have meant that we trained for 49 epochs (8.8 * 5.6). Word  counting can be done in multiple ways, and this probably explains the difference. 


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
NUM_EPOCHS=7
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=4e-4
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=50000
OPTIMIZER_TYPE=lamb
INIT_WEIGHTS=False

then

RUN_PREFIX=notram_mBERT_2760_4e4 
TRAIN_BATCH_SIZE=688
NUM_EPOCHS=1
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=4e-4
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_WEIGHTS=False

then

RUN_PREFIX=notram_mBERT_2760_4e4 
TRAIN_BATCH_SIZE=2760
NUM_EPOCHS=2
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=20000
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
NUM_EPOCHS=9
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=1e-4
END_LEARNING_RATE=1e-5
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=10000
OPTIMIZER_TYPE=adam
INIT_WEIGHTS=True

then

RUN_PREFIX=notram_devlin_256_1e4_adam 
TRAIN_BATCH_SIZE=256
NUM_EPOCHS=1
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=1e-5
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=adam
INIT_WEIGHTS=True
```

## NoTram Devlin mBERT
Same corpus and training time as above. Based on recommended settings in Devlin. Weights initiated from mBERT

```bash
RUN_PREFIX=notram_devlin_mbert_256_2e5_decay
TRAIN_BATCH_SIZE=256
NUM_EPOCHS=9
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=2e-5
END_LEARNING_RATE=2e-6
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=10000
OPTIMIZER_TYPE=adam
INIT_WEIGHTS=True

then

RUN_PREFIX=notram_devlin_mbert_256_2e5_decay
TRAIN_BATCH_SIZE=256
NUM_EPOCHS=1
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=2e-6
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=adam
INIT_WEIGHTS=True
```

# Training Set - Corpus v1
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
## Summary Training Set
| <!-- -->   | <!-- -->  | 
| -------- |  -----:| 
|Training Size |1,890 TB|
|Training time | - |
|Dupe factor | 6 |
|Training examples| 2,432,129,972 |
|Vocabulary| 119.547|
