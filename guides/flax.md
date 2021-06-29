Main documents:
```bash
https://cloud.google.com/tpu/docs/jax-quickstart-tpu-vm
https://github.com/huggingface/transformers/tree/master/examples/flax/language-modeling#masked-language-modeling
```

#Running everything from the console seems to be the only thing that works:
Trying to run this from Dante.
```bash
gcloud auth login
gcloud services enable tpu.googleapis.com
gcloud beta services identity create --service tpu.googleapis.com
gcloud alpha compute tpus tpu-vm create flax --zone europe-west4-a --accelerator-type v3-8 --version v2-alpha
gcloud alpha compute tpus tpu-vm ssh flax --zone europe-west4-a
```

Install latest jax and transformers
```bash
pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```

Test if it all works:
```bash
python3
>>import jax
>>jax.device_count()
>>8
```

Fork the repository by clicking on the 'Fork' button on the repository's page (https://github.com/huggingface/transformers). This creates a copy of the code under your GitHub user account.
```bash
$ git clone https://github.com/<your Github handle>/transformers.git
$ cd transformers
$ git remote add upstream https://github.com/huggingface/transformers.git
$ git checkout -b norwegian-roberta-base-oscar (Any descriptive name)
$ sudo pip -e install ".[flax]" 
$ sudo pip install -e ".[transformers]"

$ cd ~/
$ git clone https://github.com/huggingface/datasets.git
$ cd datasets
$ pip install -e ".[streaming]"
$ sudo apt install python-is-python3

```
Start python, and verify that you can runthe script on https://github.com/huggingface/transformers/tree/master/examples/research_projects/jax-projects#how-to-install-relevant-libraries

```bash
$ git clone https://huggingface.co/pere/norwegian-roberta-base
$ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
$ sudo apt-get install git-lfs
$ cd norwegian-roberta-base
$ git lfs track "*tfevents*"
$ cd ..
$ export MODEL_DIR="./norwegian-roberta-base"
$ ln -s ~/transformers/examples/flax/language-modeling/run_mlm_flax.py run_mlm_flax.py
```

Follow the instructions. Make a script for training a tokenizer. Make a script for creating config. Run them

We are now ready to run the training script:

Start training
```bash
python3 ./run_mlm_flax.py --output_dir="./runs" --model_type="roberta" --config_name="${MODEL_DIR}" --tokenizer_name="${MODEL_DIR}" --dataset_name="oscar" --dataset_config_name="unshuffled_deduplicated_no" --max_seq_length="128" --weight_decay="0.01" --per_device_train_batch_size="128" --per_device_eval_batch_size="128"  --learning_rate="3e-4" --warmup_steps="1000" --overwrite_output_dir --pad_to_max_length --num_train_epochs="10" --adam_beta1="0.9" --adam_beta2="0.98"
```






