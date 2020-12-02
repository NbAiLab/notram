# Development Models

## NoTram mBERT
Trained from Tensorflow mBERT. Original model is a BERT Base with 12 hidden layers and 12 attention heads. The vocab has 119.547 tokens. The original model is trained on 104 languages. After a hyperparameter search, the following settings were chosen for trainng on a TPU v3-8:

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
Number of words:
Size:
Number of tokens:
Dupe factor:
Number of training examples total:
Number of training examples per epoch:
Vocabulary: 119.547 tokens

```
