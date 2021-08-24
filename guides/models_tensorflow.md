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

After that we train 100.000 steps with a sequence length of 512. We will then need 276,000,000 training examples, but we are only able to make 101,338,748 from one epoch (since the sequence length is 4X as long). We should therefore generate a dataset equivalent to 2.7 epochs. A dupe_factor of 3 is sufficient. 

We use a slight alteration of this, since we want to train at max learning rate for longer. We also extend the warmup since we are continuing from pretrained weights. We train at maximum batch size for all sequence lengths and do linear scaling of the learning rate.
* 50k warmup 0 -> 4e-4 @ 128 - BS 2760
* 650k - fixed 4e-4 @ 128 - BS 2760
* 100k - fixed 1e-4 @ 512 - BS 688
* 200k - decaying 4e-4 -> 0 @128 - BS 2760

A control to see if this is done correctly, is to calculate the size of our corpus compared to Devlin's corpus. In total we are training for 6.1+2.7=8.8 epochs. At the same time our corpus is 5.6 times larger. If we trained for an equivalent number of training examples on Devlin's corpus it would have meant that we trained for 49 epochs (8.8 * 5.6). Word  counting can be done in multiple ways, and this probably explains the difference. 


## T1 NoTram mBERT
We are using the **multi_cased_L-12_H-768_A-12** model as the base model. This is basically a BERT Base model where the vocabulary is extended to 119,547 tokens. The original model is trained on 104 languages. 

This is the exact configuration:
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
PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.163.87.82
RUN_PREFIX=T1_NoTram_mBERT_step1
TRAIN_BATCH_SIZE=2760
PRETRAIN_DATA=corpus1_128
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=7
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=4e-4
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=50000
OPTIMIZER_TYPE=lamb

# TimeHistory: 1016.72 seconds, 2714.60 examples/second between steps 699000 and 700000
# Train Step: 700000/700000  / loss = 2.18837833404541  masked_lm_accuracy = 0.588048  lm_example_loss = 2.122653  next_sentence_accuracy = 0.975460  next_sentence_loss = 0.065726  lr = 0.000400
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-04_14-43-17_109795_T1_NoTram_mBERT_step1/ctl_step_700000.ckpt-7
# Finished training after 11870.7 min

then
# Run training for 7 epochs, 100,000 steps each, processing 481,600,000 training examples in total...
# Run training for 8 epochs, 100,000 steps each, processing 550,400,000 training examples in total... - This value seem to be based on 512 seq...
# Run training for 14 epochs, 100,000 steps each, processing 537,600,000 training examples in total...

PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.163.87.82
RUN_PREFIX=T1_NoTram_mBERT_step2
TRAIN_BATCH_SIZE=384
PRETRAIN_DATA=corpus1_512
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=10 ##Note: Batch size needs to be reduced with a factor of roughly 7. Not sure if iterations or examples should be the basis. Choosing in between
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=77
LEARNING_RATE=4e-4
END_LEARNING_RATE=4e-4
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_CHECKPOINT=run_2020-12-04_14-43-17_109795_T1_NoTram_mBERT_step1/ctl_step_700000.ckpt-7
LOAD_MLM_NSP_WEIGHTS=True
EXPECT_PARTIAL=True #Unable to load LAMB optimizer

# Train Step: 1000000/1400000  / loss = 2.0590381622314453  masked_lm_accuracy = 0.607627  lm_example_loss = 2.009415  next_sentence_accuracy = 0.982240  next_sentence_loss = 0.049624 
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-13_11-33-27_046420_T1_NoTram_mBERT_step2/ctl_step_1000000.ckpt-3         

then
# Run training for 12 epochs, 100,000 steps each, processing 460,800,000 training examples in total...

PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.163.87.82
RUN_PREFIX=T1_NoTram_mBERT_step3
TRAIN_BATCH_SIZE=384
PRETRAIN_DATA=corpus1_512
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=12 ##Note: Batch size needs to be reduced with a factor of roughly 7. Not sure if iterations or examples should be the basis. Choosing in between
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=77
LEARNING_RATE=24e-4 # For it to reach 4e-4 at 10 epochs
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_CHECKPOINT=run_2020-12-13_11-33-27_046420_T1_NoTram_mBERT_step2/ctl_step_1000000.ckpt-3
LOAD_MLM_NSP_WEIGHTS=True
EXPECT_PARTIAL=True #Unable to load LAMB optimizer


# Train Step: 1200000/1200000  / loss = 1.9271330833435059  masked_lm_accuracy = 0.626467  lm_example_loss = 1.883928  next_sentence_accuracy = 0.984688  next_sentence_loss = 0.043205  lr = 0.000000
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-16_08-55-26_727642_T1_NoTram_mBERT_step3/ctl_step_1200000.ckpt-2


# Training Summary: {'total_training_steps': 1200000, 'train_loss': 1.9271330833435059}
# Finished training after 2644.6 min
# Writing final training log to gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-16_08-55-26_727642_T1_NoTram_mBERT_step3/run_logs.json...

then

# Run training for 20 epochs, 100,000 steps each, processing 5,520,000,000 training examples in total...

PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.163.87.82
RUN_PREFIX=T1_NoTram_mBERT_step4
TRAIN_BATCH_SIZE=2640 # Do not know why we have less memory available here now.
PRETRAIN_DATA=corpus1_128
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=20
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=10e-4 # To reach 4e-4 after the warmup at 12 epochs.
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0 # With the current code it will not be possible to use warmup here (since it is lineary scaled from startup)
OPTIMIZER_TYPE=lamb
INIT_CHECKPOINT=run_2020-12-16_08-55-26_727642_T1_NoTram_mBERT_step3/ctl_step_1200000.ckpt-2
LOAD_MLM_NSP_WEIGHTS=True
EXPECT_PARTIAL=True #Unable to load LAMB optimizer

```

```bash
Model url: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-18_15-38-54_557295_T1_NoTram_mBERT_step4/ctl_step_2000000.ckpt-8
Training log: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-18_15-38-54_557295_T1_NoTram_mBERT_step4/run_logs.json
MLM Accuracy: 0.6104
MLM Loss: 1.983
NSP Accuracy: 0.9792
NSP Loss: 0.0573
```

We did also train an alternative model here where the decay is slower and much longer for 512 sequences. We then restored from step2 
```bash
PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.109.182.242
RUN_PREFIX=T1_NoTram_mBERT_step3b
TRAIN_BATCH_SIZE=384
PRETRAIN_DATA=corpus1_512
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=20 
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=77
LEARNING_RATE=8e-4 # For it to reach 4e-4 at 10 epochs
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_CHECKPOINT=run_2020-12-13_11-33-27_046420_T1_NoTram_mBERT_step2/ctl_step_1000000.ckpt-3
LOAD_MLM_NSP_WEIGHTS=True
EXPECT_PARTIAL=True #Unable to load LAMB optimizer
```
```bash
Model url: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-18_16-55-01_574997_T1_NoTram_mBERT_step3b/ctl_step_2000000.ckpt-10
Training log: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-18_16-55-01_574997_T1_NoTram_mBERT_step3b/run_logs.json
MLM Accuracy: 0.635123
MLM Loss: 1.833115
NSP Accuracy: 0.985521
NSP Loss: 0.041957
```


## T2 NoTram Devlin 
Same corpus and training time as above. Based on recommended settings in Devlin. Randomly initiated weights.

```bash
PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.62.187.170
RUN_PREFIX=T2_NoTram_Devlin_step1
TRAIN_BATCH_SIZE=256
PRETRAIN_DATA=corpus1_128
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=9
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=1e-4
END_LEARNING_RATE=1e-5
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=10000
OPTIMIZER_TYPE=adamw
INIT_WEIGHTS=True
LOAD_MLM_NSP_WEIGHTS=True

# Run training for 10 epochs, 100,000 steps each, processing 256,000,000 training examples in total...
# Train Step: 900000/900000  / loss = 2.409637212753296  masked_lm_accuracy = 0.557035  lm_example_loss = 2.333266  next_sentence_accuracy = 0.970781  next_sentence_loss = 0.076371  lr = 0.000010
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-04_14-19-36_926551_T2_NoTram_Devlin_step1/ctl_step_900000.ckpt-9
# Finished training after 1864.7 min


then

PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.66.153.58
RUN_PREFIX=T2_NoTram_Devlin_step2 
TRAIN_BATCH_SIZE=256
PRETRAIN_DATA=corpus1_512
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=10
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=77
LEARNING_RATE=1e-4
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=adamw
INIT_CHECKPOINT=run_2020-12-04_14-19-36_926551_T2_NoTram_Devlin_step1/ctl_step_900000.ckpt-9
LOAD_MLM_NSP_WEIGHTS=True


# Train Step: 1000000/1000000  / loss = 2.2283148765563965  masked_lm_accuracy = 0.581281  lm_example_loss = 2.176687  next_sentence_accuracy = 0.980977  next_sentence_loss = 0.051627  lr = 0.000000
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-07_14-37-43_750726_T2_NoTram_Devlin_step2/ctl_step_1000000.ckpt-1
# Finished training after 854.7 min

```

## T3 NoTram Devlin mBERT
Same corpus and training time as above. Based on recommended settings in Devlin. Weights initiated from mBERT

```bash
PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.107.135.34
RUN_PREFIX=T3_NoTram_Devlin_mBERT_step1
TRAIN_BATCH_SIZE=256
PRETRAIN_DATA=corpus1_128
MODEL_CLASS=bert_multi_cased
NUM_EPOCHS=9
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=2e-5
END_LEARNING_RATE=2e-6
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=10000
OPTIMIZER_TYPE=adamw

# Run training for 10 epochs, 100,000 steps each, processing 256,000,000 training examples in total...
# Train Step: 900000/900000  / loss = 2.4459850788116455  masked_lm_accuracy = 0.553771  lm_example_loss = 2.365007  next_sentence_accuracy = 0.969648  next_sentence_loss = 0.080979  lr = 0.000002
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-04_15-03-22_229120_T3_NoTram_Devlin_mBERT_step1/ctl_step_900000.ckpt-9
# Finished training after 1889.1 min
# Writing final training log to gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-04_15-03-22_229120_T3_NoTram_Devlin_mBERT_step1/run_logs.json


then

PROJECT_NAME=notram_v1
BUCKET_NAME=notram-west4-a
TPU_IP=10.109.182.242
RUN_PREFIX=T2_NoTram_Devlin_mBERT_step2
MODEL_CLASS=bert_multi_cased
TRAIN_BATCH_SIZE=256
PRETRAIN_DATA=corpus1_512
NUM_EPOCHS=10
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=77
LEARNING_RATE=2e-5
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=adamw
INIT_CHECKPOINT=run_2020-12-04_15-03-22_229120_T3_NoTram_Devlin_mBERT_step1/ctl_step_900000.ckpt-9
LOAD_MLM_NSP_WEIGHTS=True

# Train Step: 1000000/1000000  / loss = 2.288719415664673  masked_lm_accuracy = 0.573113  lm_example_loss = 2.236540  next_sentence_accuracy = 0.980820  next_sentence_loss = 0.052180  lr = 0.000000
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-07_21-00-07_215892_T2_NoTram_Devlin_mBERT_step2/ctl_step_1000000.ckpt-1
# Finished training after 854.5 min


```
## T4 BERT Norwegian
Created with a 50k vocab-file. Base training strategy is to train twice the amount of time from avove on 4e-4 (Since we are initiating from random weights). First one is trained on a v3-8 since the pods are unavailable. Mainly for testing.

Step 1
```bash
PROJECT_NAME=notram_v2
BUCKET_NAME=notram-west4-a
TPU_IP=10.126.138.58
RUN_PREFIX=T4_noTram2_BERT_norwegian_cased
TRAIN_BATCH_SIZE=2760
PRETRAIN_DATA=corpus2_cased_128
MODEL_CLASS=bert_base_norwegian_cased
NUM_EPOCHS=14
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=4e-4
END_LEARNING_RATE=4e-4
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=50000
OPTIMIZER_TYPE=lamb
INIT_WEIGHTS=True

```

Step 2
```bash
PROJECT_NAME=notram_v2
BUCKET_NAME=notram-west4-a
TPU_IP=10.121.163.42
RUN_PREFIX=T5_noTram2_BERT_norwegian_uncased
TRAIN_BATCH_SIZE=2760
PRETRAIN_DATA=corpus2_uncased_128
MODEL_CLASS=bert_base_norwegian_uncased
NUM_EPOCHS=14
MAX_SEQ_LENGTH=128
MAX_PREDICTIONS_PER_SEQ=19
LEARNING_RATE=76e-5
END_LEARNING_RATE=4e-5
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_CHECKPOINT=run_2021-02-04_22-14-57_961229_T5_noTram2_BERT_norwegian_uncased/ctl_step_800000.ckpt-8
LOAD_MLM_NSP_WEIGHTS=True
EXPECT_PARTIAL=True #Unable to load LAMB optimizer
```
```bash

# Train Step: 1400000/1400000  / loss = 2.134629249572754  masked_lm_accuracy = 0.603281  lm_example_loss = 2.082853  next_sentence_accuracy = 0.981094  next_sentence_loss = 0.051776  lr = 0.000040
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-02-22_16-20-34_406304_T4_noTram2_BERT_norwegian_cased/ctl_step_1400000.ckpt-1
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-02-22_16-20- 34_406304_T4_noTram2_BERT_norwegian_cased/pretrained/bert_model.ckpt-1
```

Step 3
```bash
PROJECT_NAME=notram_v2
BUCKET_NAME=notram-west4-a
TPU_IP=10.126.138.58
RUN_PREFIX=T4_noTram2_BERT_norwegian_cased
TRAIN_BATCH_SIZE=384
PRETRAIN_DATA=corpus2_cased_512
MODEL_CLASS=bert_base_norwegian_cased
NUM_EPOCHS=25
MAX_SEQ_LENGTH=512
MAX_PREDICTIONS_PER_SEQ=77
LEARNING_RATE=909e-7
END_LEARNING_RATE=0
STEPS_PER_LOOP=100
NUM_STEPS_PER_EPOCH=100000
WARMUP_STEPS=0
OPTIMIZER_TYPE=lamb
INIT_CHECKPOINT=run_2021-02-22_16-20-34_406304_T4_noTram2_BERT_norwegian_cased/ctl_step_1400000.ckpt-1
LOAD_MLM_NSP_WEIGHTS=True

python run_pretrain.py \
  --run_prefix $RUN_PREFIX \
  --project_name $PROJECT_NAME \
  --bucket_name $BUCKET_NAME \
  --tpu_ip $TPU_IP \
  --pretrain_data $PRETRAIN_DATA \
  --model_class $MODEL_CLASS \
  --train_batch_size $TRAIN_BATCH_SIZE \
  --num_epochs $NUM_EPOCHS \
  --max_seq_length $MAX_SEQ_LENGTH \
  --max_predictions_per_seq $MAX_PREDICTIONS_PER_SEQ \
  --learning_rate $LEARNING_RATE \
  --end_lr $END_LEARNING_RATE \
  --steps_per_loop $STEPS_PER_LOOP \
  --num_steps_per_epoch $NUM_STEPS_PER_EPOCH \
  --warmup_steps $WARMUP_STEPS \
  --optimizer_type $OPTIMIZER_TYPE \
  --init_checkpoint $INIT_CHECKPOINT \
  --load_mlm_nsp_weights $LOAD_MLM_NSP_WEIGHTS
```

Norwegian Cased Model (08.03.2021)
```bash
# Train Step: 2500000/2500000  / loss = 1.9603041410446167  masked_lm_accuracy = 0.628408  lm_example_loss = 1.920373  next_sentence_accuracy = 0.985651 next_sentence_loss = 0.039930  lr = 0.000000
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-05_06-43-40_204936_T4_noTram2_BERT_norwegian_cased/ctl_step_2500000.ckpt-3 
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-05_06-43 40_204936_T4_noTram2_BERT_norwegian_cased/pretrained/bert_model.ckpt-3                                                                                             
# Writing final training log to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-05_06-43-40_204936_T4_noTram2_BERT_norwegian_cased/run_logs.json...         
# Writing BERT config to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-05_06-43-40_204936_T4_noTram2_BERT_norwegian_cased/bert_config.json... 
```
Norwegian Uncased Model (07.03.2021)
```bash
# Train Step: 2500000/2500000  / loss = 1.9390231370925903  masked_lm_accuracy = 0.630239  lm_example_loss = 1.898049  next_sentence_accuracy = 0.985547 next_sentence_loss = 0.040973  lr = 0.000000
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-03_09-06-53_919550_T5_noTram2_BERT_norwegian_uncased/ctl_step_2500000.ckpt-4
# Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-03_09-06-53_919550_T5_noTram2_BERT_norwegian_uncased/pretrained/bert_model.ckpt-4
# Writing final training log to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-03_09-06-53_919550_T5_noTram2_BERT_norwegian_uncased/run_logs.json...
# Writing BERT config to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-03_09-06-53_919550_T5_noTram2_BERT_norwegian_uncased/bert_config.json...  

```
## T6 BERT Norwegian Cased
Following the same principle and training schedule as T4. However, this time we are using the Huggingface tokenizer for creating the dataset.

```bash
Train Step: 3800000/3800000  / loss = 1.901314377784729  masked_lm_accuracy = 0.636563  lm_example_loss = 1.864438  next_sentence_accuracy = 0.987370  next_sentence_loss = 0.036877  lr = 0.000000
Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-21-39_382880_T6_noTram2_BERT_norwegian_cased/ctl_step_3800000.ckpt-6
Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-21-39_382880_T6_noTram2_BERT_norwegian_cased/pretrained/bert_model.ckpt-6
Training Summary: {'total_training_steps': 3800000, 'train_loss': 1.901314377784729}
Finished training after 7021.7 min
Writing final training log to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-21-39_382880_T6_noTram2_BERT_norwegian_cased/run_logs.json...
Writing BERT config to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-21-39_382880_T6_noTram2_BERT_norwegian_cased/bert_config.json...
```

The POD-version is a bit simplified, where step 1 and 2 is together and a decaying learning rate. The trained POD-version of the model is available here. Here the batch sizes are 32k and 5120:
gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-03_06-25-01_581252_T6POD_BERT_base_norwegian_cased_decay/ctl_step_380000.ckpt-5

## T7 BERT Norwegian Uncased
Following the same principle and training schedule as T5. However, this time we are using the Huggingface tokenizer for creating the dataset.
```bash
Train Step: 3800000/3800000  / loss = 1.8729134798049927  masked_lm_accuracy = 0.638725  lm_example_loss = 1.835060  next_sentence_accuracy = 0.987057  next_sentence_loss = 0.037853  lr = 0.000000                                                                                                                                                  
Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-47-13_534396_T7_noTram2_BERT_norwegian_uncased/ctl_step_3800000.ckpt-6
Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-47-13_534396_T7_noTram2_BERT_norwegian_uncased/pretrained/bert_model.ckpt-6
Training Summary:{'total_training_steps': 3800000, 'train_loss': 1.8729134798049927}
Finished training after 7015.5 min
Writing final training log to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-47-13_534396_T7_noTram2_BERT_norwegian_uncased/run_logs.json...
Writing BERT config to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-47-13_534396_T7_noTram2_BERT_norwegian_uncased/bert_config.json...
```
The trained POD-version of the model is available here. Here the batch sizes are 32k and 5120:
gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-03-28_19-36-06_145747_T7POD_BERT_base_norwegian_uncased_decay/ctl_step_380000.ckpt-10


## T8 BERT Scandinavian Uncased
Following the same principle and training schedule as T4 and T5. However, it uses the 50.500 vocab created by KBS based on Oscar of sv+no+dk. Swedish is overrrepresented in this corpus. The reason for training the model is to get an idea if this affects training significantly.
```bash
Train Step: 3800000/3800000  / loss = 1.912283182144165  masked_lm_accuracy = 0.627946  lm_example_loss = 1.873785  next_sentence_accuracy = 0.986276  next_sentence_loss = 0.038499  lr = 0.000000                                                                                                                                                   
Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-42-03_908002_T8_noTram2_scandinavian_uncased/ctl_step_3800000.ckpt-10
Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-42-03_908002_T8_noTram2_scandinavian_uncased/pretrained/bert_model.ckpt-10
Training Summary:{'total_training_steps': 3800000, 'train_loss': 1.912283182144165}
Finished training after 11694.6 min
Writing final training log to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-42-03_908002_T8_noTram2_scandinavian_uncased/run_logs.json...
Writing BERT config to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-20_13-42-03_908002_T8_noTram2_scandinavian_uncased/bert_config.json...
```

The trained POD-version of the model is available here. Here the batch sizes are 32k and 5120:
```bash
Train Step: 380000/380000  / loss = 1.9606670141220093  masked_lm_accuracy = 0.620199  lm_example_loss = 1.917404  next_sentence_accuracy = 0.984572  next_sentence_loss = 0.043262  lr = 0.000000                                                                                                                       Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-19_07-16-40_520813_T8POD_BERT_base_scandinavian_uncased_decay/ctl_step_380000.ckpt-10
Saving model as TF checkpoint: gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-19_07-16-40_520813_T8POD_BERT_base_scandinavian_uncased_decay/pretrained/bert_model.ckpt-10
Training Summary:{'total_training_steps': 380000, 'train_loss': 1.9606670141220093}
Finished training after 1333.3 min
Writing final training log to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-19_07-1640_520813_T8POD_BERT_base_scandinavian_uncased_decay/run_logs.json...
Writing BERT config to gs://notram-west4-a/notram_v2/pretrain/runs/run_2021-04-19_07-16-40_520813_T8POD_BERT_base_scandinavian_uncased_decay/bert_config.json...
```

## T9 BERT Large Norwegian Uncased
NOTE: Disregard model. Started with the wrong number of layers!

First attempt at training a large Norwegian model on the v3-256 preempt pod. Basically using the settings from the 76 minutes article.

The seq128 was run with a bs of 32k and a lr of 50e-4 decaying to 0 over 100.000 steps with a 10.000 step warmup. For the 512seq it was run for 6.000 steps with a bs of 8192 and a lr of 25e-4, also decaying to 0 and a warmup of 10.000 steps. Some instability during training, and it needed to be reinitiated a few times. 

Final file is available here: gs://notram-east1-d/notram_v2/pretrain/runs/run_2021-03-31_18-43-35_029328_T9_BERT_large_norwegian_uncased/ctl_step_60000.ckpt-6. 
Stats after 512seq: Train Step: 60000/60000  / loss = 1.9550302028656006  masked_lm_accuracy = 0.628962  lm_example_loss = 1.912292  next_sentence_accuracy = 0.984841  next_sentence_loss = 0.042739  lr = 0.000000

## T10 Bert Large Long Norwegian Uncased
Duplicating the T9 experiment but this time with the right model name. Doubling number of epochs. Because of instability in the training, the learning rate is reduced to 25e-4.


## T11 BERT Norwegian Supercased
Following the same principle and training schedule as T5. However, this time we are using the Huggingface tokenizer for creating the dataset.


# Training Set - Corpus1_128
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

# Create Evaluation Sets for Release Candidate 150121
```bash
eval1 = bert-base-multilingual-cased

gsutil cp -r gs://notram-public/nb_models/NoTram_Devlin_081220/*.* gs://notram-public/nb_models/eval/eval2/
gsutil cp -r gs://notram-public/nb_models/NoTram_mBERT_prerelease_181220/*.* gs://notram-public/nb_models/eval/eval3/
gsutil cp -r gs://notram-public/nb_models/NoTram_mBERT_prerelease_311220/T1_NoTram_mBERT_step3b_9/*.* gs://notram-public/nb_models/eval/eval4/
gsutil cp -r gs://notram-public/nb_models/NoTram_mBERT_prerelease_311220/T1_NoTram_mBERT_step4_8/*.* gs://notram-public/nb_models/eval/eval5/
```

## Summary Training Set
| <!-- -->   | <!-- -->  | 
| -------- |  -----:| 
|Training Size |1,890 TB + 1,198 TB|
|Training time | - |
|Dupe factor | 6 + 3 |
|Training examples| 2,432,129,972 + 467,567,520|
|Vocabulary| 119.547|
