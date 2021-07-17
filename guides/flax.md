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
$ pip install --upgrade clu
$ pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
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
$ git clone https://github.com/huggingface/transformers.git
$ cd transformers
$ git remote add upstream https://github.com/huggingface/transformers.git
$ # Not necessary since we are not planning on making changes here
$ # git checkout -b norwegian-roberta-base-oscar (Any descriptive name)
$ pip install -e ".[flax]"
$ pip install -e ".[transformers]"

$ cd ~/
$ git clone https://github.com/huggingface/datasets.git
$ cd datasets
$ pip install -e ".[streaming]"
$ cd 

```

#Model Specific Installations

Fork the repository by clicking on the 'Fork' button on the repository's page (https://github.com/huggingface/transformers). You can also use this command:
```bash
huggingface-cli repo create norwegian-roberta-base
```


Set up the RoBERTa scripts. Here the norwegian-roberta-base is already forked (if not see above):

```bash
$ git clone https://huggingface.co/<your Github handle>/norwegian-roberta-base
$ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
$ sudo apt-get install git-lfs
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
Lead to this error:
```bash
RuntimeError: tensorflow/compiler/xla/xla_client/computation_client.cc:273 : Missing XLA configuration
```

Fix this simply by setting:

```bash
$ export USE_TORCH=False
```

How to set up neo-gpt-red. There are some files in 
https://huggingface.co/pere/norwegian-gptneo-red. Copy them, and run the setup_devices.py.





