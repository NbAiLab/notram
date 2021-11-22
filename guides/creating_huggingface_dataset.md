# Routines for creating a Huggingface Dataset

This is a general description for creating a huggingface dataset. It shows all the necessary steps to do the process from data to finished dataset in huggingface. As an example we use one of our open datasets so the process can be visible. All scripts used for this task is available from this site. We use the dataset "nynorsk" as the example. 

Log in to your huggingface account and create your empty corpus:

# Create empty dataset

*In your top right menu from huggingface, select "new dataset". Set the proper settings private/public, although you will be better off to set the dataset to public for the duration of the creation. After this you can switch the dataset to private. This is done through the huggingface menus for datasets.*

*Go to your local environment (where you store your different corpi) and create the directory for the corpus:*
**Warning: if you're corpus contains files over 1 GB do not use nfsmounted storage.**

```bash
$ cd <corpi storage dir>
$ mkdir nynorsk

```

Checkout first version of the corpus:

```bash
$ cd <corpi_storage_dir>
$ mkdir nynorsk
$ cd nynorsk
$ git co https://huggingface.co/datasets/<owner>/nynorsk.git
$ git lfs track "*tfevents*"
$ git lfs track "*model*"
$ git lfs track "*gz*"
$ git lfs track "*md*"

```
After this you can create the contents of your dataset with our huggingface dataset builder:

```bash
$ python corpus_dataset_builder.py --dataset_input_file <json file with all dataset files> --output_dir <corpi_storage_dir>/nynorsk

```

The dataset builder does the following tasks:

* Generate a datacard
* Read and shuffle your dataset file
* Create a train and validation split (each train shard is by default 1 Gb and the validation split is 1 GB) on the proper format. Changeable.
* Train and validation files s
* Create dummy training and a dummy validation file on the proper format.
* Creates statistics of your dataset (word counts,year distribution,no of documents).
* Generates a python loader functions *"nynorsk.py"*

After this you can check in your dataset. Here we do a check in of the example "nynorsk":
```bash

$ cd <corpi_storage_dir>/nynorsk
$ git add .
$ git commit -m "First commit of dataset nynorsk"
$ git push

```
All files are named and packed with the naming rules of huggingface in mind.


And upload all the sharded files to the bucket

```
gsutil -m cp *shard*.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/shards/ &&
gsutil -m cp nb_nn_balanced_shuffled_train.json.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/splits/ &&
gsutil -m cp nb_nn_balanced_shuffled_test.json.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/splits/ &&v
gsutil -m cp nb_nn_balanced_shuffled_validation.json.gz gs://notram-west4-a/pretrain_datasets/nb_nn_balanced_shuffled/splits/

```
