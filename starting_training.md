# Starting training
This goes through the process of training on a TPU v3-8. Before attempting this, make sure that you have the following files:
* Generated tfrecord-files
* Vocab-file used for generating the tfrecord-files (for instance the file bundled with BERT)
* Get the bert_config.json file describing the network (for instance the file bundled with BERT)
* Get the pre-trained model if you do not want to randomly initiating the weights

## Create a VM
The VM needs to be in the same zone as your TPU and bucket. There are a lot of ways of creating the VM, and in many cases you will create from a stored image. However, if you want to create one from scratch, you can go through https//console.cloud.google.com -> Compute Engine -> VM Instances. Click "Create Instance". 

A n2-standard-8 (8 vCPUs, 32 GB memory) for $200/month is sufficient for training a v3-128. For the v3-8 you can get away with a n2-standard-2 (2 vCPU, 8GB memory) for $60/month. Often it is convenient to have some storage, so set it up with a 200GB disk.

Connect to the new VM (either through the browser or by looking at the "gcloud command"). Add public keys for ./ssh/authorized_keys for easy access.

It is a lot easier to build upon a pre-installed image. All you would do then would be to pull from github and authenticate. However, follow [this instruction](https://github.com/NBAiLab/notram/blob/master/set_up_vm.md) for setting up a VM from scratch. 


### Authenticate
Run both these command to make sure the VM is correctly authenticated. You might also have to run this on the local machine to be able to copy to the bucket. In most cases only one of these is needed. However, it is frustrating to figure out which is needed, so simply just run both.

```bash
gcloud auth login
gcloud auth application-default login

#You might also have to run this if the project id is wrong
gcloud config set project PROJECT_ID

```


## Create a bucket
The bucket needs to be in the same zone as your TPU and VM. The easiest way to create a bucket is through https//console.cloud.google.com -> Storage. Click "Create Bucket". Here a bucket called "notram-myzone" is created. Use standard settings, however choosing the non-default "unigram" access control should be sufficient and make things easier later.

### Copy necessary files to the bucket
Upload the correct cased-wwm-BERT-model (for TF2.0) to the bucket named "notram-myzone". Then upload the tfrecord-files.

```bash
#Copy tfrecord
gsutil -m cp -r *.tfrecords gs://notram-myzone/notram_v1/pretrain/pretrain_data/

#Unpack and change to the correct directory to copy the unpacked BERT files to the bucket
gsutil -m cp -r *.* gs://notram-myzone/notram_v1/pretrained_models/bert/tf_20/wwm_cased_L-24_H-1024_A-16/

```



