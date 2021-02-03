
# Preparations
Currently this requires Tensorflow 2.2 and Python 3.8. With the newest conda there is a few errors. Run the following:
```bash
pip install numpy==1.19.5
pip install tensorflow-addons==0.10.0
  ```
  
# Start training
If you have read [Setting up Machines for Training](https://github.com/NBAiLab/notram/blob/master/setting_up_machines_for_training.md) and [Set up Notram VM](https://github.com/NBAiLab/notram/blob/master/set_up_vm.md), you should be ready to start the training.

The training script located in the covid-twitter-bert can be run directly. It does however have have quite a few parameters, and these might be useful to store for later. We therefore recommend creating a shell script called "run1.sh" with the parameters and running this script instead.

If you have followed the guide earlier, the paths to the bucket should now be correct.

```bash
RUN_PREFIX=first_experiment #Prefix that is used on all training. Up to you what to put here. Makes it easier to identify runs.
PROJECT_NAME=notram_v1 #First level in the bucket. Where all the files are kept
BUCKET_NAME=notram-myzone #Set bucket name
TPU_IP=10.113.99.154 #Replace with the internal IP of your TPU. When training on pods, use tpu_name instead
PRETRAIN_DATA=corpus1 #Subdirectory where the training data is held
MODEL_CLASS=bert_large_cased_wwm #This name needs to exist in the file called config.py. File should be self explanatory
TRAIN_BATCH_SIZE=1024 #Maximum size depends on seq_length. On a v3-8 we should go for max size. Should be dividable by 8
NUM_EPOCHS=3 #Not to be confused with real epochs. This is the time between each round, and will finish when writing a checkpoint
MAX_SEQ_LENGTH=128 #Sequence length is set when creating tfrecord-files and can not be changed here
MAX_PREDICTIONS_PER_SEQ=19 #Set this to the same value as the one used when creating the tfrecords files
LEARNING_RATE=1e-4 #1e-4 is a recommended learning rate when training from scratch with this batch size. Reduce for domain specific pre-training and scale with batch size
END_LEARNING_RATE=1e-4 #Set to the same as the start learning_rate here. Typically we would however decrease it to 0
STEPS_PER_LOOP=100 #Not critical. Leave like this
NUM_STEPS_PER_EPOCH=10000 #Mainly for calculating when the checkpoints should be written, and what should internally be considered an epoch
WARMUP_STEPS=500 #Lineary increases learning rate during warmup. Important especially when training from scratch
OPTIMIZER_TYPE=adamw #This is the correct choice here. However, when training on pods and huge batch sizes, change this to lamb

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
  --optimizer_type $OPTIMIZER_TYPE
  ```
  
  It is strongly recommended to run all training inside of tmux. If not, the training might be interrupted by the closing of your terminal. This command starts a new tmux-session called "run1". You can detach from it with "ctl-b d", and reattach with "tmux a -t run1". It is usually no problem running a few training sessions on different TPUs on a single VM.
  ```bash
  tmux new -s run1
  ```
  
  Since you have stored the script in the file 'run1.sh' you can now start it easily with:
  ```bash
  sh run1.sh
  ```
  
