# Preparing the mC4
Procedure for downloading and preparing the Common Crawl Corpus. Start with setting up a new VM following [this guide](https://github.com/NBAiLab/notram/blob/master/set_up_vm.md) or loading a prebuilt image. Make sure you have a bucket and change the bucket name in the script below. 


## Download the corpus
```bash


pip install tensorflow-datasets
pip install tfds-nightly

DATASET_NAME=c4
DATASET_CONFIG=multilingual
GCP_PROJECT=nancy-194708
GCS_BUCKET=gs://nb-us-central1-mc4

wget https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-40/wet.paths.gz
gunzip wet.paths.gz
gsutil cp wet.paths "$GCS_BUCKET/manual/"

echo "tensorflow_datasets[$DATASET_NAME]" >> /tmp/beam_requirements.txt
echo "tfds-nightly[$DATASET_NAME]" >> /tmp/beam_requirements.txt
python -m pip install -r /tmp/beam_requirements.txt
python -m tensorflow_datasets.scripts.download_and_prepare \
  --datasets=$DATASET_NAME/$DATASET_CONFIG \
  --data_dir=$GCS_BUCKET/tensorflow_datasets \
  --beam_pipeline_options=\
"region=us-central1-a, runner=DataflowRunner,project=$GCP_PROJECT,job_name=$DATASET_NAME-gen,"\
"staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
"requirements_file=/tmp/beam_requirements.txt"
```
