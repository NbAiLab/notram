Main documents:
```bash
https://cloud.google.com/tpu/docs/jax-quickstart-tpu-vm
https://github.com/huggingface/transformers/tree/master/examples/flax/language-modeling#masked-language-modeling
```

Running everything from the console seems to be the only thing that works:
```bash
gcloud auth login
gcloud services enable tpu.googleapis.com
gcloud beta services identity create --service tpu.googleapis.com
gcloud alpha compute tpus tpu-vm create flax2 --zone europe-west4-a --accelerator-type v3-8 --version v2-alpha
gcloud alpha compute tpus tpu-vm ssh flax2 --zone europe-west4-a
```

Install latest jax and transformers
```bash
pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
pip install transformers
pip install flax
```

Test if it all works:
```bash
python3
>>import jax
>>jax.device_count()
>>8
```

Clone transformers and notram:
```bash
git clone https://github.com/huggingface/transformers.git
git clone https://github.com/NBAiLab/notram.git
```

Create some folders
```bash
mkdir -p
cd notram/flax
ln -s ~/transformers/examples/flax/language-modeling/run_mlm_flax.py run_mlm_flax.py
```

Train a tokenizer (script already copied to notram/flax/ for training on the ascar corpus)
```bash
python3 train_tokenizer.py
python3 create_config.py
```

Start training
```bash
python3 ./run_mlm_flax.py --output_dir="./runs" --model_type="roberta" --config_name="${MODEL_DIR}" --tokenizer_name="${MODEL_DIR}" --dataset_name="oscar" --dataset_config_name="unshuffled_deduplicated_no" --max_seq_length="128" --weight_decay="0.01" --per_device_train_batch_size="128" --per_device_eval_batch_size="128"  --learning_rate="3e-4" --warmup_steps="1000" --overwrite_output_dir --pad_to_max_length --num_train_epochs="10" --adam_beta1="0.9" --adam_beta2="0.98"
```






