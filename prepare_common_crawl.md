# Preparing the mC4
Procedure for downloading and preparing the Common Crawl Corpus.

## Download the corpus
```bash
pip3 install tensorflow-datasets
pip3 install tfds-nightly

DATASET_NAME=c4
DATASET_CONFIG=multilingual
GCP_PROJECT=nancy-194708
GCS_BUCKET=gs://nb-mc4
echo "tensorflow_datasets[$DATASET_NAME]" > /tmp/beam_requirements.txt
echo "tfds-nightly[$DATASET_NAME]" > /tmp/beam_requirements.txt
python3 -m pip install /tmp/beam_requirements.txt
python3 -m tensorflow_datasets.scripts.download_and_prepare \
  --datasets=$DATASET_NAME/$DATASET_CONFIG \
  --data_dir=$GCS_BUCKET/tensorflow_datasets \
  --beam_pipeline_options=\
"runner=DataflowRunner,project=$GCP_PROJECT,job_name=$DATASET_NAME-gen,"\
"staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
"requirements_file=/tmp/beam_requirements.txt"
```
