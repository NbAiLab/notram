# Routines for creating a Huggingface Dataset

The example here is from the Bokmål Nynorsk Balanced corpus. It is preshuffled and has a total of 9725051 lines. We are splitting this in a 90% train and a 5% validation and 5% test set.

Basically this means we are aiming for:
Train = 8752545
Validation = 486253
Test = 486253

```
head -n 8752545 nb_nn_balanced_shuffled.json > nb_nn_balanced_shuffled_train.json
tail -n +8752546 nb_nn_balanced_shuffled.json > validation_and_test.json
head -n 486253 validation_and_test.json > nb_nn_balanced_shuffled_validation.json
tail -n +486254 validation_and_test.json > nb_nn_balanced_shuffled_test.json
rm validation_and_test.json
wc -l
```

We will then split the train set in 1024 train chunks, each with 8547 lines. Using the same chunk length on validation and test set gives us 57 chunks in each of these sets. (The exapmple below actually creates 1025 chunks. Should be adjusted. For now, I am just deleting the last one)

```
split --numeric-suffixes=1 -a 4 --additional-suffix "-of-1024.json" -l 8547 nb_nn_balanced_shuffled_train.json "nb_nn_balanced_shuffled_train-shard-" &&
split --numeric-suffixes=1 -a 4 --additional-suffix "-of-0057.json" -l 8547 nb_nn_balanced_shuffled_test.json "nb_nn_balanced_shuffled_test-shard-" &&
split --numeric-suffixes=1 -a 4 --additional-suffix "-of-0057.json" -l 8547 nb_nn_balanced_shuffled_validation.json "nb_nn_balanced_shuffled_validation-shard-"
```

Here is a similar example for the notram_v2_official_short100k. The train file here is 256GB, while the validation file is 1GB. We want it all in 1GB chunks. The train file has 215849980 lines, meaning we want 843164 lines in each file.

```
split --numeric-suffixes=1 -a 4 --additional-suffix "-of-0256.json" -l 843164 norwegian_colossal_corpus_train.jsonl "norwegian_colossal_corpus_train-shard-"
mv norwegian_colossal_corpus_validation.jsonl norwegian_colossal_corpus_validation-shard-0001-of-0001.json
```


In the end we gzip all the individual files.

```
gzip *

## Run this in parallel to save some time
parallel gzip ::: *
```

And upload all the sharded files to the bucket

```
gsutil -m cp *shard*.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/shards/ &&
gsutil -m cp nb_nn_balanced_shuffled_train.json.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/splits/ &&
gsutil -m cp nb_nn_balanced_shuffled_test.json.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/splits/ &&v
gsutil -m cp nb_nn_balanced_shuffled_validation.json.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/splits/

```
