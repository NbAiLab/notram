# Preparing the mC4
This guide is sort of outdated now since AllenAI has done this job and published this entire dataset on HuggingFace. Keeping just for the archive.


Procedure for downloading and preparing the Common Crawl Corpus. Start with setting up a new VM following [this guide](https://github.com/NBAiLab/notram/blob/master/set_up_vm.md) or loading a prebuilt image. Make sure you have a bucket and change the bucket name in the script below.

First, you need to clone `https://github.com/tensorflow/datasets/` and add your own config in `datasets/tensorflow_datasets/text/c4.py` (as of this writing, we used the latest version of the repo on March 1st, 2021). Specifically, we patched locally [0db70eb](https://github.com/tensorflow/datasets/commit/0db70eb1c379dbde1b56dfbe1d9be7194d9e9605) to include a `nordic` config and ignore the unknown languages (see [nordic_dump2013-20.patch](https://github.com/tensorflow/datasets/files/6060456/nordic_dump2013-20.patch.txt)):

```python
  C4Config(
      "norwegian",
      languages=["no"],
      cc_versions=ALL_CC_VERSIONS,
      clean=True,
      paragraph_filter=True,
      dedupe=True,
      badwords_filter=False,
      description=
      "Norwegian split Common Crawl dumps."),
```

```bash
# Settings
DATASET_NAME=c4
DATASET_CONFIG=norwegian
GCP_PROJECT=nancy-194708
GCS_BUCKET=gs://nb-us-central1-mc4
GCS_BUCKET_REGION=us-central1  # Do not include here a letter as in VMs, like "us-central1-a"
```

Or to get all Nordic languages

```python
  C4Config(
      "nordic",
      languages=["no", "sv", "da", "is"],
      cc_versions=ALL_CC_VERSIONS,
      clean=True,
      paragraph_filter=True,
      dedupe=True,
      badwords_filter=False,
      description=
      "Nordic split Common Crawl dumps. "
      "It includes Norwegian, Swedish, Danish, and Islandic"),
```

```bash
# Settings
DATASET_NAME=c4
DATASET_CONFIG=nordic
GCP_PROJECT=nancy-194708
GCS_BUCKET=gs://nordic-mc4-us-central1
GCS_BUCKET_REGION=us-central1  # Do not include here a letter as in VMs, like "us-central1-a"
```

In most cases, you'll want to exclude pages classified as "unknown language" if you are extracting a language portion of mC4. In order to do that, try commenting out `c4_utils.UNKNOWN_LANGUAGE` in [line 391 (the `foor...loop`)](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/c4.py#L391).

This is the exact patch we used to succesfully run the whole process for one single dump:

```diff
diff --git a/tensorflow_datasets/text/c4.py b/tensorflow_datasets/text/c4.py
index 3d5e981c..678f8688 100644
--- a/tensorflow_datasets/text/c4.py
+++ b/tensorflow_datasets/text/c4.py
@@ -90,7 +90,9 @@ OPENWEBTEXT_CC_VERSIONS = (  # August 2018 - July 2019
     "2019-30", "2019-26", "2019-22", "2019-13", "2019-09", "2019-04", "2018-51",
     "2018-47", "2018-43", "2018-39", "2018-34")

-ALL_CC_VERSIONS = (  # as of September 23, 2020
+ALL_CC_VERSIONS = ("2013-20", )
+
+_ALL_CC_VERSIONS = (  # as of September 23, 2020
     "2013-20", "2013-48", "2014-10", "2014-15", "2014-23", "2014-35", "2014-41",
     "2014-42", "2014-49", "2014-52", "2015-06", "2015-11", "2015-14", "2015-18",
     "2015-22", "2015-27", "2015-32", "2015-35", "2015-40", "2015-48", "2016-07",
@@ -258,6 +260,17 @@ class C4(tfds.core.BeamBasedBuilder):
           description=
           "Multilingual C4 (mC4) has 101 languages and is generated from 71 "
           "Common Crawl dumps."),
+      C4Config(
+          "nordic",
+          languages=["no", "sv", "da", "is"],
+          cc_versions=ALL_CC_VERSIONS,
+          clean=False,
+          paragraph_filter=True,
+          dedupe=True,
+          badwords_filter=False,
+          description=
+          "Nordic split Common Crawl dumps. "
+          "It includes Norwegian, Swedish, Danish, and Islandic"),
   ]

   def _info(self):
@@ -350,7 +363,7 @@ class C4(tfds.core.BeamBasedBuilder):
       ]

     splits = []
-    for lang in self.builder_config.languages + [c4_utils.UNKNOWN_LANGUAGE]:
+    for lang in self.builder_config.languages:  # + [c4_utils.UNKNOWN_LANGUAGE]:
       splits.extend([
           tfds.core.SplitGenerator(
               name=lang,
```

## Download and process the corpus
```bash
# Adding requirements for local and Apache Beam (workers)
rm /tmp/beam_requirements.txt
echo "apache-beam[gcp]"  >> /tmp/beam_requirements.txt
echo "tensorflow-datasets[$DATASET_NAME]"  >> /tmp/beam_requirements.txt
echo "google-apitools"  >> /tmp/beam_requirements.txt
# there's an error with avro-python3 and dill, dill version needs to be fixed
# https://github.com/tensorflow/datasets/issues/2636#issuecomment-722551597
echo "dill<0.3.2,>=0.3.1.1"  >> /tmp/beam_requirements.txt
python -m pip install tensorflow
python -m pip install -r /tmp/beam_requirements.txt
python -m pip install -e datasets
```

The next command successfully processed the 105TB and almost 2 billion files of the `CC-MAIN-2013-20` dump. Using 75 workers, it took 31 hours. That's roughly 3.3TB per hour. The default disk size was increased to 100GB (it might be unnecessarily big), we forced v2 of the runner, and enabled shuffle mode. The total cost was around $1000.

```bash
# Starting the main script
python -m tensorflow_datasets.scripts.download_and_prepare \
  --datasets=$DATASET_NAME/$DATASET_CONFIG \
  --data_dir=$GCS_BUCKET/tensorflow_datasets \
  --beam_pipeline_options=\
  "region=$GCS_BUCKET_REGION,runner=DataflowRunner,project=$GCP_PROJECT,"\
  "job_name=$DATASET_NAME-$DATASET_CONFIG-1dump-gen,"\
  "staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
  "dataflow_job_file=$GCS_BUCKET/job_file.json,requirements_file=/tmp/beam_requirements.txt,"\
  "autoscaling_algorithm=NONE,disk_size_gb=100,num_workers=75,experiments=shuffle_mode=service,"\
  "experiments=use_runner_v2," 2>&1 | tee nordic-mc4-1dump.log
```

## Loading and exporting the data in plain text format

Using the local installation with the properly [patched files](https://github.com/tensorflow/datasets/files/6060456/nordic_dump2013-20.patch.txt), one can easily copy the results from the bucket locally and load them using Tensorflow Datasets.

The next code will split the dataset per language and also create two versions of it, one with the raw data as it was extracted from CC, and other removing those documents with not legible characters:

```python
from pathlib import Path

import tensorflow_datasets as tfds
from tqdm import tqdm

# The path ~/tensorflow_datasets/c4/nordic/3.0.1 must exist
# gsutil -m cp -r gs://nordic-mc4-us-central1/tensorflow_datasets/c4 ~/tensorflow_datasets/
nordic_c4 = tfds.load("c4/nordic:3.0.1", download=False)

path_chars = (
    ("/some/path", ""),
    ("/some/path/raw", "�")
)
for path, char_error in path_chars:
    for split, dataset in nordic_c4.items():
        filename = Path(path) / f"{split}.txt"
        with filename.open(mode="w") as split_file:
            for entry in tqdm(dataset.as_numpy_iterator(), desc=split):
                text = entry["text"].decode("utf8")
                if not (char_error and char_error in text):
                    split_file.write(text)
                    split_file.write("\n\n")
```

## Notes

The MC4 is a cleaned version of Common Crawl. The following precedure have been applied:

> Unfortunately, the majority of [the text in Common Crawl] is not natural language. Instead, it largely comprises gibberish or boiler-plate text like menus, error messages, or duplicate text. Furthermore, a good deal of the scraped text contains content that is unlikely to be helpful for any of the tasks we consider (offensive language, placeholder text, source code, etc.). To address these issues, we used the following heuristics for cleaning up Common Crawl's web extracted text:
>- We only retained lines that ended in a terminal punctuation mark (i.e. a period, exclamation mark, question mark, or end quotation mark).
>- We removed any page that contained any word on the "List of Dirty, Naughty, Obscene or Otherwise Bad Words". [https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and...]
>- Many of the scraped pages contained warnings stating that Javascript should be enabled so we removed any line with the word Javascript.
>- Some pages had placeholder "lorem ipsum" text; we removed any page where the phrase "lorem ipsum" appeared.
>- Some pages inadvertently contained code. Since the curly bracket "{" appears in many programming languages (such as Javascript, widely used on the web) but not in natural text,we removed any pages that contained a curly bracket.
> - To deduplicate the dataset, we discarded all but one of any three-sentence span occurring more than once in the dataset. Additionally, since most of our downstream tasks are focused on English-language text, we used langdetect [https://pypi.org/project/langdetect/] to filter out any pages that were not classified as English with a probability of at least 0.99.
