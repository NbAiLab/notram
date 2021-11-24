# Configure a Notram VM for Training with Tensorflow
This guide explains a standard setup of a VM for BERT training. It installs the necessary dependencies and sets up a few necessary tools. It also clones the Notram-github and the Notram-branch of the CT-BERT-github. If you are connecting as a new user to an existing VM you will have to run most of these steps as well.

## Get some general tools and generate the public key
```bash
sudo apt-get install ssh git tmux wget locales htop byobu jq python-dev clang gcc pv

#Having Nordic Characters might be handy. Run this script and install the languages you need. Make sure you have nb_NO.utf8 and nn_NO.utf8 installed.
sudo dpkg-reconfigure locales

#Then you might switch locale by this command. You might have to log in and out of the ssh for this to take effect. 
sudo update-locale LC_ALL="nb_NO.utf8"

#Replace email address with your git email address and press ENTER on all questions
ssh-keygen -t rsa -C "per@capia.no"
```
After the public key is generated it will tell you the placement. This might be a good time to add this to the git repositories under "Setting" - "Deploy keys" if you plan on pushing changes to the git. You should also copy the copy the public keay from your local machine to the authoriced_keys
```bash
#On local machine
cat ~/.ssh/id_rsa.pub   

#On VM
vim ~/.ssh/authorized_keys

#Copy the public key to the end of this file
```

## Install Conda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

```
After you have answered "yes" to the last question you still have to close and reopen connection.

## Create a conda environment and auto restart it
```bash
conda create -n python38 python=3.8 
echo "conda activate python38" >> ~/.bashrc 
```
Close and reopen connection. When logging in the command line should state “python38”

## Set up git credentials
```bash
#Replace name and email
git config --global user.name "Per E Kummervold" 
git config --global user.email "per@capia.no"
#Make sure username and password will then be stored globally after first login
git config --global credential.helper store
```

## Clone Notram
```bash
git clone https://github.com/NBAiLab/notram.git
pip install -r notram/requirements.txt
python -m spacy download nb_core_news_sm
```

## Clone CT-bert and checkout Notram branch 
Please note that both the Notram and CT-BERT has a lot NLP-tools as requirements, including Tensorflow. It might be useful running the requirements-file even if you do not clone the libraries. 

```bash
git clone https://github.com/digitalepidemiologylab/covid-twitter-bert.git
pip install -r covid-twitter-bert/requirements.txt
cd covid-twitter-bert
git checkout notram
git submodule update --init
cd ..

```

## Install GCloud and authenticate
```bash
#Install GCloud if necessary
curl https://sdk.cloud.google.com | bash
source ~/.bashrc

gcloud auth login
gcloud auth application-default login 

#You might have to change to another project for billing and access
gcloud config set project nancy-194708

```
Congratulations! You now have a clean VM image set up with all necessary authentications. If you plan on setting up multiple VMs this might be a good time to save this image in the [Google Cloud Console](https://console.cloud.google.com/).


## Preparing Tensorflow

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
  
