Following these documents:
```bash
https://cloud.google.com/tpu/docs/jax-quickstart-tpu-vm
https://github.com/huggingface/transformers/tree/master/examples/flax/language-modeling#masked-language-modeling
https://github.com/huggingface/transformers/tree/master/examples/research_projects/jax-projects#how-to-install-relevant-libraries
https://cloud.google.com/tpu/docs/system-architecture-tpu-vm
```

Running this on local machine:
```bash
$ gcloud auth login
$ gcloud services enable tpu.googleapis.com
$ gcloud beta services identity create --service tpu.googleapis.com
$ gcloud alpha compute tpus tpu-vm create flax --zone europe-west4-a --accelerator-type v3-8 --version v2-alpha
$ gcloud alpha compute tpus tpu-vm ssh flax --zone europe-west4-a
```

If you need to set up an VM with an extra disk
```bash
$ gcloud compute disks create flaxdisk1 --size 1000 --zone europe-west4-a
$ gcloud alpha compute tpus tpu-vm create gptneo-red --zone europe-west4-a --accelerator-type v3-8 --version v2-alpha --data-disk source=projects/nancy-194708/zones/europe-west4-a/disks/flaxdisk1
gcloud alpha compute tpus tpu-vm ssh gptneo-red --zone europe-west4-a
```

After starting the VM, the disk needs to be formatted according to this: https://cloud.google.com/compute/docs/disks/add-persistent-disk#formatting
```bash
sudo lsblk
#Find the disk here, and the device name. Most likely it will be "sdb". Given that name, procede with 
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
python3 -m pip install --user --upgrade pip
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
sudo apt install python3.8-venv
python3 -m venv gptneo-red
source gptneo-red/bin/activate
```

Run this on the VM. Dont worry if the first commend has some errors.:
```bash
pip install --upgrade clu
pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
export USE_TORCH=False
```
Test if it all works:
```bash
$ python
>>import jax
>>jax.device_count()
8
```

Set up Transformers
```bash
git clone https://github.com/huggingface/transformers.git
cd transformers
git remote add upstream https://github.com/huggingface/transformers.git
# Not necessary since we are not planning on making changes here
# git checkout -b norwegian-roberta-base-oscar (Any descriptive name)
pip install -e ".[flax]"
pip install -e ".[transformers]"
cd ~/

git clone https://github.com/huggingface/datasets.git
cd datasets
pip install -e ".[streaming]"
cd ~/
```

Make sure you are logged into Huggingface, GCloud and that your Git credentials are stored appropriately
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

#Log in to GCloud
gcloud auth login
gcloud auth application-default login 

#You might have to change to another project for billing and access
gcloud config set project <MY-PROJECT-ID>
```

# Model Specific Installations

## RoBERTa
Fork the repository by clicking on the 'Fork' button on the repository's page (https://github.com/huggingface/transformers). You can also use this command:
```bash
huggingface-cli repo create norwegian-roberta-base

$ git clone https://huggingface.co/<your Github handle>/norwegian-roberta-base
$ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash

$ cd norwegian-roberta-base
$ git lfs track "*tfevents*"
$ cd ..
$ export MODEL_DIR="./norwegian-roberta-base"
$ ln -s ~/transformers/examples/flax/language-modeling/run_mlm_flax.py run_mlm_flax.py

```

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
```

To continue we need a tokenizer and a model to start with.

### Train the tokenizer or copy an existing one
Training a tokenizer is explained above. We just copy the tokenizer trained in norwegian-gpt2. The vocab-size needs to be 50264.
```bash
cd git clone https://huggingface.co/pere/norwegian-gpt2
no norwegian-gpt2
cp *token* ../norwegian-gptneo-red/
cp vocab.json ../norwegian-gptneo-red/
cd ..
```

Setting up the model requires recreating the EleutherAI-model as described here: https://github.com/huggingface/transformers/tree/master/examples/research_projects/jax-projects/model%20parallel. We are using a slighlty modified script:
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

Run the following script in Python to set up the model


How to set up neo-gpt-red. There are some files in 
https://huggingface.co/pere/norwegian-gptneo-red. Copy them, and run the setup_devices.py.





