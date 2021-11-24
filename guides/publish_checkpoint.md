# Publish Pretrained Tensorflow Checkpoints

This assumes having pretrained a model with [covid-twitter-bert](https://github.com/digitalepidemiologylab/covid-twitter-bert). Basically this is onlye relevant if you have followed the training procedure of nb-bert-base.

## Huggingface

1. Download TF checkpoint (full model) to local

```bash
$ cd /disk4/folder1/working/checkpoints/huggingface/
$ mkdir T1_NoTram_mBERT_181220
$ cd T1_NoTram_mBERT_181220
$ mkdir native_pytorch
$ mkdir final_huggingface_model

$ gsutil -m cp gs://notram-west4-a/notram_v1/pretrain/runs/run_2020-12-16_08-55-26_727642_T1_NoTram_mBERT_step3/ctl_step_1200000.ckpt-2* .

$ ls -l 
total 2.3G
-rw-rw-r-- 1 perk perk 116K Dec 18 11:32 ctl_step_1200000.ckpt-2.data-00000-of-00002
-rw-rw-r-- 1 perk perk 2.0G Dec 18 11:33 ctl_step_1200000.ckpt-2.data-00001-of-00002
-rw-rw-r-- 1 perk perk  11K Dec 18 11:32 ctl_step_1200000.ckpt-2.index
```

2. Convert to native PyTorch model

```bash
# change directory
$ cd /home/tensor/covid-twitter-bert/convert_tf2_to_pytorch

# run script
python convert_tf2_to_pytorch_pretrain.py --tf_checkpoint_path /disk4/folder1/working/checkpoints/huggingface/T1_NoTram_mBERT_181220/ctl_step_1200000.ckpt-2 \
--bert_config_file /disk4/folder1/nancy/content/text/v3/pretrained_models/bert/keras_bert/multi_cased_L-12_H-768_A-12/bert_config.json \
--output_folder /disk4/folder1/working/checkpoints/huggingface/T1_NoTram_mBERT_181220/native_pytorch/
```

3. Copy over vocab file

```bash
$ cp /disk4/folder1/nancy/content/text/v3/pretrained_models/bert/keras_bert/multi_cased_L-12_H-768_A-12/vocab.txt /disk4/folder1/working/checkpoints/huggingface/T1_NoTram_mBERT_181220/native_pytorch/
```

4. Run `publish_huggingface.py` script

This adds all necessary files for the final upload to Huggingface. Also compare with the [official docs](https://huggingface.co/transformers/model_sharing.html) in case this changes in the future

```bash
# make sure to be in this directory
$ cd /home/perk/covid-twitter-bert-analysis

# run script
python publish_huggingface.py \
--path_to_pytorch_model /disk4/folder1/working/checkpoints/huggingface/T1_NoTram_mBERT_181220/native_pytorch/ \
--output_folder /disk4/folder1/working/checkpoints/huggingface/T1_NoTram_mBERT_181220/final_huggingface_model/ \
--model_name NoTram_mBERT_prerelease_181220
```

After this the final folder should contain:
```bash
$ ls /disk4/folder1/working/checkpoints/huggingface/T1_NoTram_mBERT_181220/final_huggingface_model/NoTram_mBERT_prerelease_181220/
config.json              pytorch_model.bin        special_tokens_map.json  tf_model.h5              tokenizer_config.json    vocab.txt
```

Do a minor edit in the tokenizer_config.json if this is an uncased model
̀̀̀̀``
vim /disk4/folder1/working/checkpoints/huggingface/T1_NoTram_mBERT_181220/final_huggingface_model/NoTram_mBERT_prerelease_181220/tokenizer_config.json
change "do_lower_case": true" to "do_lower_case": false"
```

5. Add README.md

Fill out [template](https://github.com/huggingface/model_card) and place it in the same folder with the other files.

6. Upload to Huggingface
Use the `transformers-cli` to upload

```bash
transformers-cli upload covid-twitter-bert-v2
```

## TF-Hub

Note: The following makes the submodel available. For publishing the full model one would need to make some adjustments in the script.

1. Download TF checkpoint (sub model, under `./pretrained/` sub directory) to local

```bash
$ ls -l data/covid_bert_v2/checkpoint/pretrained
-rw-r--r--  1 martin  staff    59K Sep 29 14:21 bert_model.ckpt-3.data-00000-of-00002
-rw-r--r--  1 martin  staff   1.2G Sep 29 14:22 bert_model.ckpt-3.data-00001-of-00002
-rw-r--r--  1 martin  staff   6.2K Sep 29 14:21 bert_model.ckpt-3.index
```

2. Run script to create tfhub directory structure

```bash
python publish_tfhub.py \
  --path_to_checkpoint covid_twitter_bert/data/covid_bert_v2/checkpoint/pretrained/bert_model.ckpt-3 \
  --output_folder covid_twitter_bert/data/covid_bert_v2/tfhub \
  --model_class bert_large_uncased_wwm
```
This will automaticall pull the config and vocab files into the new directory. The output dir looks like this:

```bash
$ tree .
.
├── assets
│   └── bert-large-uncased-whole-word-masking-vocab.txt
├── saved_model.pb
└── variables
    ├── variables.data-00000-of-00001
    └── variables.index

2 directories, 4 files
```

3. Package model
This is following the guide [here](https://github.com/tensorflow/hub/tree/master/tfhub_dev).

First, tar the model and upload it to S3:

```bash
pwd
# /Users/martin/projects/covid-twitter-bert-analysis/covid_twitter_bert/data/covid_bert_v2
MODEL_DIR=tfhub
tar -cvz -f covid-twitter-bert-v2.tar.gz -C "${MODEL_DIR}" .
```

Then upload it to a public S3 or Google Cloud bucket

```bash
aws s3 cp covid-twitter-bert-v2.tar.gz s3://crowdbreaks-public/models/covid-twitter-bert/v2/tfhub/ --acl public-read
```

4. Write the documentation

Compare with the guide above or the [existing docs](https://github.com/tensorflow/hub/tree/master/tfhub_dev/assets/digitalepidemiologylab).


5. Run validator to make sure everything works

Clone TF-hub repo, place the documentation in the appropriate place under `tfhub_dev/assets/digitalepidemiologylab/models/covid-twitter-bert` and run the validator tool:

```bash
python tfhub_dev/tools/validator.py digitalepidemiologylab/models/covid-twitter-bert/2.md
```

6. Submit PR to TFhub
