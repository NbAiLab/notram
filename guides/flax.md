
# Setting up TPU VM for Flax
Following these documents:
```bash
https://cloud.google.com/tpu/docs/jax-quickstart-tpu-vm
https://github.com/huggingface/transformers/tree/master/examples/flax/language-modeling#masked-language-modeling
https://github.com/huggingface/transformers/tree/master/examples/research_projects/jax-projects#how-to-install-relevant-libraries
https://cloud.google.com/tpu/docs/system-architecture-tpu-vm
```

Run this on local machine to make sure the necessary libraries are installed:
```bash
gcloud auth login
gcloud services enable tpu.googleapis.com
gcloud beta services identity create --service tpu.googleapis.com
```

Create the TPU VM. The procedure here depends on whether to need an extra disk. If you do not, just do this:
```bash
gcloud alpha compute tpus tpu-vm create flax --zone europe-west4-a --accelerator-type v3-8 --version v2-alpha
gcloud alpha compute tpus tpu-vm ssh flax --zone europe-west4-a
```

However, if an additional disk is required. This sets up the VM with an external disk of 1TB
```bash
gcloud compute disks create flaxdisk1 --size 1000 --zone europe-west4-a
gcloud alpha compute tpus tpu-vm create gptneo-red --zone europe-west4-a --accelerator-type v3-8 --version v2-alpha --data-disk source=projects/nancy-194708/zones/europe-west4-a/disks/flaxdisk1
gcloud alpha compute tpus tpu-vm ssh gptneo-red --zone europe-west4-a
```

After starting the VM, the disk needs to be formatted according to this: https://cloud.google.com/compute/docs/disks/add-persistent-disk#formatting
```bash
sudo lsblk
#Find the disk here, and the device name. Most likely it will be "sdb". Given that is correct, format the disk with this command: 
sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb
#Mount the disk - and give everyone 
sudo mkdir -p /mnt/disks/flaxdisk
sudo mount -o discard,defaults /dev/sdb /mnt/disks/flaxdisk
sudo chmod a+w /mnt/disks/flaxdisk
#Configure automatic mount on restarts
sudo cp /etc/fstab /etc/fstab.backup
#Find the uid of the disk - you need this value in the following steps
sudo blkid /dev/sdb
#Add this to /etc/fstab with the correct uuid
UUID=52af08e4-f249-4efa-9aa3-7c7a9fd560b0 /mnt/disks/flaxdisk ext4 discard,defaults,nofail 0 2
```
Make a sane virtual environment. Here we give it the name of the project "gptneo-red"
```bash
sudo apt-get update
python3 -m pip install --user --upgrade pip
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
sudo apt install python3.8-venv
python3 -m venv gptneo-red
source gptneo-red/bin/activate
```

Run this on the VM. Dont worry if the first command returns a few errors.:
```bash
pip install --upgrade clu
pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
export USE_TORCH=False
```

Run this in python to verify that all works:
```python
import jax
jax.device_count()
>> 8
```

Set up Transformers
```bash
git clone https://github.com/huggingface/transformers.git
cd transformers
git remote add upstream https://github.com/huggingface/transformers.git

# Recommended in the Workshop but noe necessary here since we are not planning on making changes here
# git checkout -b [Any descriptive name]

pip install -e ".[flax]"
pip install -e ".[transformers]"
cd ~/

git clone https://github.com/huggingface/datasets.git
cd datasets
pip install -e ".[streaming]"
cd ~/
```

Make sure you are logged into Hugging Face, GCloud and that your Git credentials are stored appropriately
```bash
#Install Git LFS
sudo apt-get install git-lfs

#Login to Huggingface
huggingface-cli login

#Replace name and email below
git config --global user.name "Per E Kummervold" 
git config --global user.email "per@capia.no"

#Make sure username and password will then be stored globally after first login
git config --global credential.helper store

#!!Following this, it is a good idea to make a push to the git, just to make sure your username is saved. If not, the scripts below might crash after the first epoch

#Log in to GCloud
gcloud auth login
gcloud auth application-default login 

#You might have to change to another project for billing and access
gcloud config set project <MY-PROJECT-ID>
```

# Model Specific Installations

## RoBERTa
There is quite a lot of other information available on (https://github.com/huggingface/transformers). This is based on this code but also adds some extra details. Use the external disk here for everything since the models are taking a lot of space:
```bash
cd /mnt/disks/flaxdisk/

# Create a repo if it doesn not exist
huggingface-cli repo create norwegian-roberta-base

# Clone the repo
git clone https://huggingface.co/<your Github handle>/norwegian-roberta-base
cd norwegian-roberta-base

#Make sure the repo is configured
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
git lfs track "*tfevents*"
git lfs track "*model*"

#Lets copy the main script from the transformers example
cp ~/transformers/examples/flax/language-modeling/run_mlm_flax.py .
```

### Create configs
We will use exactly the same configs here that are used on the official RoBERTa model


Follow the FLAX-instructions. Make a script for training a tokenizer. Make a script for creating config. Run them. This goes without any issues, and creates the tokenizer and the config in the norwegian-roberta-base - folder.


Trying to run run_mlm_flax-script:
```bash
python ./run_mlm_flax.py --output_dir="./runs" --model_type="roberta" --config_name="${MODEL_DIR}" --tokenizer_name="${MODEL_DIR}" --dataset_name="oscar" --dataset_config_name="unshuffled_deduplicated_no" --max_seq_length="128" --weight_decay="0.01" --per_device_train_batch_size="128" --per_device_eval_batch_size="128"  --learning_rate="3e-4" --warmup_steps="1000" --overwrite_output_dir --pad_to_max_length --num_train_epochs="10" --adam_beta1="0.9" --adam_beta2="0.98"
```

## GTP Neo
Since this requires a lot of disk space, everything here should be done in /mnt/disks/flaxdisk/

```bash
cd /mnt/disks/flaxdisk/

#Create the repo if it does not exist
huggingface-cli repo create norwegian-gptneo-red

#Clone it
git clone https://huggingface.co/pere/norwegian-gptneo-red
cd norwegian-gptneo-red
git lfs track "*tfevents*"
git lfs track "*model*"
huggingface-cli lfs-enable-largefiles /mnt/disks/flaxdisk/norwegian-gptneo-red/
cd ..

#Make cache dir
mkdir cache

#Copy and rename corpus files
mkdir corpus
cd corpus
gsutil -m cp gs://notram-west4-a/pretrain_datasets/notram_v2_social_media/splits/social_train.jsonl social_train.json
gsutil -m cp gs://notram-west4-a/pretrain_datasets/notram_v2_social_media/splits/social_validation.jsonl social_validation.json

```

To continue we need a tokenizer and a model to start with.

### Train the tokenizer or copy an existing one
Training a tokenizer is explained above. Here we just copy the tokenizer trained in norwegian-gpt2. The vocab-size needs to be 50264.
```bash
cd git clone https://huggingface.co/pere/norwegian-gpt2
no norwegian-gpt2
cp *token* ../norwegian-gptneo-red/
cp vocab.json ../norwegian-gptneo-red/
cd ..
```

### Setting up the model
Setting up the model requires recreating the EleutherAI-model as described here: https://github.com/huggingface/transformers/tree/master/examples/research_projects/jax-projects/model%20parallel. You need to copy the two files from this page transformers to the home directory.

```bash
cp ~/transformers/examples/research_projects/jax-projects/model parallel/*.py ../norwegian-gptneo-red/
```

We are using a slighlty modified script to initiate the model and save it in the home directory:
```python
import jax
import jax.numpy as jnp
from transformers import FlaxGPTNeoForCausalLM, GPTNeoConfig

model = FlaxGPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
emb = jnp.zeros((50264, model.config.hidden_size))

# update the first 50257 weights using pre-trained weights
emb = jax.ops.index_update(emb, jax.ops.index[:50257, :], model.params["transformer"]["wte"]["embedding"])
params = model.params
params["transformer"]["wte"]["embedding"] = emb

# initialize a random model with the right vocab_size
config = GPTNeoConfig.from_pretrained("EleutherAI/gpt-neo-1.3B", vocab_size=50264)
model = FlaxGPTNeoForCausalLM(config)

# assign the pre-trained weights and save the model.
model.params = params
model.save_pretrained("./")
```

### Start Training
Save the following script as run.sh
```bash
python run_clm_mp.py \
        --model_name_or_path /mnt/disks/flaxdisk/norwegian-gptneo-red/ \
        --tokenizer_name /mnt/disks/flaxdisk/norwegian-gptneo-red/ \
        --train_file /mnt/disks/flaxdisk/corpus/social_train.json \ 
        --validation_file /mnt/disks/flaxdisk/corpus/social_validation.json \   
        --do_train \ 
        --do_eval  \   
        --block_size 1024 \     
        --num_train_epochs 10 \     
        --learning_rate 4e-6 \
        --per_device_train_batch_size 3 \ 
        --per_device_eval_batch_size 3 \    
        --overwrite_output_dir \
        --output_dir /mnt/disks/flaxdisk/norwegian-gptneo-red \
        --cache_dir /mnt/disks/flaxdisk/cache/ \
        --dtype bfloat16 \   
        --logging_steps 97 \ 
        --eval_steps 96 \
        --push_to_hub
```

Start tmux, then start training
```bash
tmux new
sh ./run.sh
```




