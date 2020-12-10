# Publish pretrain checkpoints

This assumes having pretrained a model with [covid-twitter-bert](https://github.com/digitalepidemiologylab/covid-twitter-bert).

## Huggingface

1. Download TF checkpoint (full model) to local

```bash
$ ls -l data/covid_bert_v2/checkpoint
total 7880808
-rw-r--r--  1 martin  staff   224K Sep 28 16:20 ctl_step_779700.ckpt-3.data-00000-of-00002
-rw-r--r--  1 martin  staff   3.8G Sep 28 16:25 ctl_step_779700.ckpt-3.data-00001-of-00002
-rw-r--r--  1 martin  staff    20K Sep 28 16:20 ctl_step_779700.ckpt-3.index
```

2. Convert to native PyTorch model

```bash
# make sure to be in this directory
$ pwd
/Users/martin/projects/covid-twitter-bert-analysis/covid_twitter_bert/convert_tf2_to_pytorch

# run script
python convert_tf2_to_pytorch_pretrain.py \
  --tf_checkpoint_path ../data/covid_bert_v2/checkpoint/ctl_step_779700.ckpt-3 \
  --bert_config_file ../configs/bert_config_large_uncased_wwm.json \
  --output_folder ../data/covid_bert_v2/native_pytorch
```

3. Copy over vocab file

```bash
$ cp vocabs/bert-large-uncased-whole-word-masking-vocab.txt data/covid_bert_v2/native_pytorch/vocab.txt
```

4. Run `publish_huggingface.py` script

This adds all necessary files for the final upload to Huggingface. Also compare with the [official docs](https://huggingface.co/transformers/model_sharing.html) in case this changes in the future

```bash
# make sure to be in this directory
$ pwd
/Users/martin/projects/covid-twitter-bert-analysis

# run script
python publish_huggingface.py \
  --path_to_pytorch_model covid_twitter_bert/data/covid_bert_v2/native_pytorch \
  --output_folder covid_twitter_bert/data/covid_bert_v2/huggingface/ \
  --model_name covid-twitter-bert-v2
```

After this the final folder should contain:
```bash
$ ls covid-twitter-bert-v2
config.json              pytorch_model.bin        special_tokens_map.json  tf_model.h5              tokenizer_config.json    vocab.txt
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
