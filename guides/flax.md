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
```

Test if it all works:
```
python3
>>import jax
>>jax.device_count()
>>8
```

Clone transformers and notram:
```bash
git clone https://github.com/huggingface/transformers.git
https://github.com/NBAiLab/notram.git
```

Create some folders
```bash
mkdir -p
cd notram/flax
ln -s ~/transformers/examples/flax/language-modeling/run_mlm_flax.py run_mlm_flax.py
```bash

Train a tokenizer (script already copied to notram/flax/ for training on the ascar corpus)
python3 train_tokenizer.py







