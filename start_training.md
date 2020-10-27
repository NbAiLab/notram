# Start training
If you have read [Setting up Machines for Training](https://github.com/NBAiLab/notram/blob/master/setting_up_machines_for_training.md) and [Set up Notram VM](https://github.com/NBAiLab/notram/blob/master/set_up_vm.md), you should be ready to start the training.

The training script located in the covid-twitter-bert can be run directly. It does however have have quite a few parameters, and these might be useful to store for later. We therefore recommend creating a shell script called "run1.sh" with the parameters and running this script instead.

If you have followed the guide earlier, the paths to the bucket should now be correct.

```bash
RUN_PREFIX=exp1_1e4_nodecay
PROJECT_NAME=notram_v1
BUCKET_NAME=cb-tpu-us-central1
TPU_IP=1.1.1.1 #Replace with the internal IP of your TPU 
PRETRAIN_DATA=run_2020-06-16_22-20-47_002555_wwm_v2


MODEL_CLASS=bert_large_uncased_wwm
TRAIN_BATCH_SIZE=1024
EVAL_BATCH_SIZE=1024



python run_pretrain.py \
  --run_prefix $RUN_PREFIX \
  --project_name $PROJECT_NAME \
  --bucket_name $BUCKET_NAME \
  --tpu_ip $TPU_IP \
  --pretrain_data $PRETRAIN_DATA \
  --model_class $MODEL_CLASS \
  --train_batch_size $TRAIN_BATCH_SIZE \
  --eval_batch_size $EVAL_BATCH_SIZE \
  --num_epochs 10 \
  --max_seq_length 96 \
  --learning_rate 1e-4 \
  --steps_per_loop 1000 \
  --num_steps_per_epoch 125000 \
  --end_lr 1e-4 \
  --do_eval
  
  
PRETRAIN_DATA=run_2020-06-16_22-20-47_002555_wwm_v2
RUN_PREFIX=expB16_160e5_decay
BUCKET_NAME=cb-tpu-west4
#TPU_NAME=tpu-west4-v3-256-preempt
TPU_NAME=tpu-west4-v3-128	
MODEL_CLASS=bert_large_uncased_wwm
TRAIN_BATCH_SIZE=16384
EVAL_BATCH_SIZE=1024
PROJECT_NAME=covid-bert-v2


python run_pretrain.py \
  --run_prefix $RUN_PREFIX \
  --project_name $PROJECT_NAME \
  --bucket_name $BUCKET_NAME \
  --tpu_name $TPU_NAME \
  --pretrain_data $PRETRAIN_DATA \
  --model_class $MODEL_CLASS \
  --train_batch_size $TRAIN_BATCH_SIZE \
  --eval_batch_size $EVAL_BATCH_SIZE \
  --num_epochs 100 \
  --max_seq_length 96 \
  --learning_rate 160e-5 \
  --steps_per_loop 100 \
  --num_steps_per_epoch 7797 \
  --warmup_steps 10000 \
  --optimizer_type lamb \
  --end_lr 0 \
  --do_not_do_eval
  
  
  
  ```
  
  It is strongly recommended to run all training inside of tmux. If not, the training might be interrupted by the closing of your terminal. This command starts a new tmux-session called "run1". You can detach from it with "ctl-b d", and reattach with "tmux a -t run1". It is usually no problem running a few training sessions on different TPUs on a single VM.
  ```bash
  tmux new -s run1
  ```
  
  Since you have stored the script in the file 'run1.sh' you can now start it easily with:
  ```bash
  sh run1.sh
  ```
  
