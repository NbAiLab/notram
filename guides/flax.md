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

Running this on the VM:
```bash
$ pip install --upgrade clu
$ pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```

Fork the repository by clicking on the 'Fork' button on the repository's page (https://github.com/huggingface/transformers). This creates a copy of the code under your GitHub user account.
```bash
$ git clone https://github.com/huggingface/transformers.git
$ cd transformers
$ git remote add upstream https://github.com/huggingface/transformers.git
$ git checkout -b norwegian-roberta-base-oscar (Any descriptive name)
$ pip install --user --no-use-pep517 -e ".[flax]"
$ pip install --user --no-use-pep517 -e ".[transformers]"

$ cd ~/
$ git clone https://github.com/huggingface/datasets.git
$ cd datasets
$ pip install -e ".[streaming]"
$ sudo apt install python-is-python3

```

Test if it all works:
```bash
$ python3
>>import jax
>>jax.device_count()
8
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

Then tried setting this variable:

```bash
$ export XRT_TPU_CONFIG="localservice;0;localhost:51011"
```

After this the script runs, but do not find the TPU. Number of TPU_cores is also null.






