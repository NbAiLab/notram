# Starting training
This goes through the process of training on a TPU v3-8. Before attempting this, make sure that you have the following files:
* Generated tfrecord-files
* Vocab-file used for generating the tfrecord-files (for instance the file bundled with BERT)
* Get the bert_config.json file describing the network (for instance the file bundled with BERT)
* Get the pre-trained model if you do not want to randomly initiating the weights

## Create a bucket
The bucket needs to be in the same zone as your TPU and VM. The easiest way to create a bucket is through https//console.google.com -> Storage. Click "Create Bucket". Here a bucket called "notram-myzone" is created. Use standard settings, however choosing the non-default "unigram" access control should be sufficient and make things easier later.

### Copy necessary files to the bucket
Upload the correct cased-wwm-BERT-model (for TF2.0) to the bucket named "notram-myzone". Then upload the tfrecord-files.

```bash
#Copy tfrecord
gsutil -m cp -r *.tfrecords gs://notram-myzone/notram_v1/pretrain/pretrain_data/

#Unpack and change to the correct directory to copy the unpacked BERT files to the bucket
gsutil -m cp -r *.* gs://notram-myzone/notram_v1/pretrained_models/bert/tf_20/wwm_cased_L-24_H-1024_A-16/

```



### Authenticate
Run both these command to make sure the VM is correctly authenticated. You might also have to run this on the local machine to be able to copy to the bucket. In most cases only one of these is needed. However, it is frustrating to figure out which is needed, so simply just run both.

```bash
gcloud auth login
gcloud auth application-default login

#You might also have to run this if the project id is wrong
gcloud config set project PROJECT_ID

```

