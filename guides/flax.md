Main documents:
https://cloud.google.com/tpu/docs/jax-quickstart-tpu-vm
https://github.com/huggingface/transformers/tree/master/examples/flax/language-modeling#masked-language-modeling

Running everything from the console seems to be the only thing that works:
gcloud auth login
gcloud services enable tpu.googleapis.com
gcloud beta services identity create --service tpu.googleapis.com
gcloud alpha compute tpus tpu-vm create flax2 --zone europe-west4-a --accelerator-type v3-8 --version v2-alpha

Then get into the correct box...
gcloud alpha compute tpus tpu-vm ssh flax2 --zone europe-west4-a

Install latest jax
pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

Install transformers
pip install transformers

Test if it all works:
python3
>>import jax
>>jax.device_count()
>>8

Clone transformers and notram:
git clone https://github.com/huggingface/transformers.git
https://github.com/NBAiLab/notram.git

Create some folders
mkdir -p
cd notram/flax
ln -s ~/transformers/examples/flax/language-modeling/run_mlm_flax.py run_mlm_flax.py






