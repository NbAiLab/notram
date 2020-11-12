# Preparing the mC4
Procedure for downloading and preparing the Common Crawl Corpus. Start with setting up a new VM following [this guide](https://github.com/NBAiLab/notram/blob/master/set_up_vm.md) or loading a prebuilt image. Make sure you have a bucket and change the bucket name in the script below.

First, you need to clone `https://github.com/tensorflow/datasets/` and add your own config in `datasets/tensorflow_datasets/text/c4.py` (as of this writing, we used the latest version of the repo on November 10th, 2020):
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

## Download and process the corpus
```bash
# All 72 Common Crawl dumps from https://commoncrawl.org/the-data/get-started/
rm wet.paths.urls
echo "CC-MAIN-2013-20" >> wet.paths.urls
echo "CC-MAIN-2013-48" >> wet.paths.urls
echo "CC-MAIN-2014-10" >> wet.paths.urls
echo "CC-MAIN-2014-15" >> wet.paths.urls
echo "CC-MAIN-2014-23" >> wet.paths.urls
echo "CC-MAIN-2014-35" >> wet.paths.urls
echo "CC-MAIN-2014-41" >> wet.paths.urls
echo "CC-MAIN-2014-42" >> wet.paths.urls
echo "CC-MAIN-2014-49" >> wet.paths.urls
echo "CC-MAIN-2014-52" >> wet.paths.urls
echo "CC-MAIN-2015-06" >> wet.paths.urls
echo "CC-MAIN-2015-11" >> wet.paths.urls
echo "CC-MAIN-2015-14" >> wet.paths.urls
echo "CC-MAIN-2015-18" >> wet.paths.urls
echo "CC-MAIN-2015-22" >> wet.paths.urls
echo "CC-MAIN-2015-27" >> wet.paths.urls
echo "CC-MAIN-2015-32" >> wet.paths.urls
echo "CC-MAIN-2015-35" >> wet.paths.urls
echo "CC-MAIN-2015-40" >> wet.paths.urls
echo "CC-MAIN-2015-48" >> wet.paths.urls
echo "CC-MAIN-2016-07" >> wet.paths.urls
echo "CC-MAIN-2016-18" >> wet.paths.urls
echo "CC-MAIN-2016-22" >> wet.paths.urls
echo "CC-MAIN-2016-26" >> wet.paths.urls
echo "CC-MAIN-2016-30" >> wet.paths.urls
echo "CC-MAIN-2016-36" >> wet.paths.urls
echo "CC-MAIN-2016-40" >> wet.paths.urls
echo "CC-MAIN-2016-44" >> wet.paths.urls
echo "CC-MAIN-2016-50" >> wet.paths.urls
echo "CC-MAIN-2017-04" >> wet.paths.urls
echo "CC-MAIN-2017-09" >> wet.paths.urls
echo "CC-MAIN-2017-13" >> wet.paths.urls
echo "CC-MAIN-2017-17" >> wet.paths.urls
echo "CC-MAIN-2017-22" >> wet.paths.urls
echo "CC-MAIN-2017-26" >> wet.paths.urls
echo "CC-MAIN-2017-30" >> wet.paths.urls
echo "CC-MAIN-2017-34" >> wet.paths.urls
echo "CC-MAIN-2017-39" >> wet.paths.urls
echo "CC-MAIN-2017-43" >> wet.paths.urls
echo "CC-MAIN-2017-47" >> wet.paths.urls
echo "CC-MAIN-2017-51" >> wet.paths.urls
echo "CC-MAIN-2018-05" >> wet.paths.urls
echo "CC-MAIN-2018-09" >> wet.paths.urls
echo "CC-MAIN-2018-13" >> wet.paths.urls
echo "CC-MAIN-2018-17" >> wet.paths.urls
echo "CC-MAIN-2018-22" >> wet.paths.urls
echo "CC-MAIN-2018-26" >> wet.paths.urls
echo "CC-MAIN-2018-30" >> wet.paths.urls
echo "CC-MAIN-2018-34" >> wet.paths.urls
echo "CC-MAIN-2018-39" >> wet.paths.urls
echo "CC-MAIN-2018-43" >> wet.paths.urls
echo "CC-MAIN-2018-47" >> wet.paths.urls
echo "CC-MAIN-2018-51" >> wet.paths.urls
echo "CC-MAIN-2019-04" >> wet.paths.urls
echo "CC-MAIN-2019-09" >> wet.paths.urls
echo "CC-MAIN-2019-13" >> wet.paths.urls
echo "CC-MAIN-2019-18" >> wet.paths.urls
echo "CC-MAIN-2019-22" >> wet.paths.urls
echo "CC-MAIN-2019-26" >> wet.paths.urls
echo "CC-MAIN-2019-30" >> wet.paths.urls
echo "CC-MAIN-2019-35" >> wet.paths.urls
echo "CC-MAIN-2019-39" >> wet.paths.urls
echo "CC-MAIN-2019-43" >> wet.paths.urls
echo "CC-MAIN-2019-47" >> wet.paths.urls
echo "CC-MAIN-2019-51" >> wet.paths.urls
echo "CC-MAIN-2020-05" >> wet.paths.urls
echo "CC-MAIN-2020-10" >> wet.paths.urls
echo "CC-MAIN-2020-16" >> wet.paths.urls
echo "CC-MAIN-2020-24" >> wet.paths.urls
echo "CC-MAIN-2020-29" >> wet.paths.urls
echo "CC-MAIN-2020-34" >> wet.paths.urls
echo "CC-MAIN-2020-40" >> wet.paths.urls

# Putting WET files into the bucket
for wetpath in `cat wet.paths.urls` ; do curl -s https://commoncrawl.s3.amazonaws.com/crawl-data/$wetpath/wet.paths.gz | gunzip | pv --name $wetpath --bytes | gsutil -q cp - "$GCS_BUCKET/tensorflow_datasets/downloads/manual/crawl-data/$wetpath/web.paths" ; done

# Adding requirements for local and Apache Beam (workers)
rm /tmp/beam_requirements.txt
echo "tensorflow_datasets[$DATASET_NAME]" >> /tmp/beam_requirements.txt
echo "tfds-nightly[$DATASET_NAME]" >> /tmp/beam_requirements.txt
echo "google-apitools" >> /tmp/beam_requirements.txt
echo "-e datasets" >> /tmp/beam_requirements.txt
# there's an error with avro-python3 and dill, dill version needs to be fixed
# https://github.com/tensorflow/datasets/issues/2636#issuecomment-722551597
echo "dill==0.3.1.1" >> /tmp/beam_requirements.txt
python -m pip install tensorflow
python -m pip install -r /tmp/beam_requirements.txt
```

Since the job file JSON is larger than 10MB, you will beed to append the flag `experiments=upload_graph`, which might make the Dataflow UI unstable:
```bash
# Starting the main script
python -m tensorflow_datasets.scripts.download_and_prepare \
  --datasets=$DATASET_NAME/$DATASET_CONFIG \
  --data_dir=$GCS_BUCKET/tensorflow_datasets \
  --beam_pipeline_options=\
"region=$GCS_BUCKET_REGION,runner=DataflowRunner,project=$GCP_PROJECT,job_name=$DATASET_NAME-$DATASET_CONFIG-gen,"\
"staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
"dataflow_job_file=$GCS_BUCKET/job_file.json,"\
"requirements_file=/tmp/beam_requirements.txt,"\
"autoscaling_algorithm=NONE,num_workers=450,"\
"experiments=shuffle_mode=service,experiments=upload_graph" 2>&1 | tee nb-mc4.log
```

In either case, the Dataflow pipeline should run for about 24 hours.

# Notes
The MC4 is a cleaned version of Common Crawl. The following precedure have been applied:

> Unfortunately, the majority of [the text in Common Crawl] is not natural language. Instead, it largely comprises gibberish or boiler-plate text like menus, error messages, or duplicate text. Furthermore, a good deal of the scraped text contains content that is unlikely to be helpful for any of the tasks we consider (offensive language, placeholder text, source code, etc.). To address these issues, we used the following heuristics for cleaning up Common Crawl's web extracted text:
> - We only retained lines that ended in a terminal punctuation mark (i.e. a period, exclamation mark, question mark, or end quotation mark).
> - We removed any page that contained any word on the "List of Dirty, Naughty, Obscene or Otherwise Bad Words". [https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and...]
> * Many of the scraped pages contained warnings stating that Javascript should be enabled so we removed any line with the word Javascript.
> - Some pages had placeholder "lorem ipsum" text; we removed any page where the phrase "lorem ipsum" appeared.
>- Some pages inadvertently contained code. Since the curly bracket "{" appears in many programming languages (such as Javascript, widely used on the web) but not in natural text,we removed any pages that contained a curly bracket.
> - To deduplicate the dataset, we discarded all but one of any three-sentence span occurring more than once in the dataset.
Additionally, since most of our downstream tasks are focused on English-language text, we used langdetect [https://pypi.org/project/langdetect/] to filter out any pages that were not classified as English with a probability of at least 0.99. 
