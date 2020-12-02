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
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
```

