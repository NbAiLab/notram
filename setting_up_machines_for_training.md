# Setting up machines for training
This goes through the process of setting up the machines necessary for training on a TPU. Before attempting this, you should have generated some tfrecod-files with your training data.

## Create a VM
The VM needs to be in the same zone as your TPU and bucket. There are a lot of ways of creating the VM, and in many cases you will create from a stored image. However, if you want to create one from scratch, you can go through https//console.cloud.google.com -> Compute Engine -> VM Instances. Click "Create Instance". 

A n2-standard-8 (8 vCPUs, 32 GB memory) for $200/month is sufficient for training a v3-128. For the v3-8 you can get away with a n2-standard-2 (2 vCPU, 8GB memory) for $60/month. Often it is convenient to have some storage, so set it up with a 200GB disk.

Connect to the new VM (either through the browser or by looking at the "gcloud command"). Add public keys for ./ssh/authorized_keys for easy access.

[This guide](https://github.com/NBAiLab/notram/blob/master/set_up_vm.md) explains in details how to set up a Notram VM from scratch. You might have to load a pre-built VM image instead. This is easier. You will however will need to check out the latest code from the git and authenticate with gcloud. You will find details about this in the guide as well.

## Create a bucket
The bucket needs to be in the same zone as your TPU and VM. The easiest way to create a bucket is through https//console.cloud.google.com -> Storage. Click "Create Bucket". Create a bucket called "notram-myzone" (replace myzone with the zone you are using). Use standard settings, however choosing the non-default "unigram" access control should be sufficient and make things easier later.

### Copy necessary files to the bucket
You will find a [bucket](gs://cloud-tpu-checkpoints/bert) with pretrained NLP models [here](https://github.com/tensorflow/models/tree/93490036e00f37ecbe6693b9ff4ae488bb8e9270/official/nlp/bert#access-to-pretrained-checkpoints). You will need the vocab to be able to generate the tfrecord-files, and might as well download the other files as well. You can of course copy all the files from bucket to bucket. 

When you have generated the tfrecord-files, upload them to the bucket. Then upload the correct cased-wwm-BERT-model to the bucket named "notram-myzone". 

```bash
#Copy tfrecord
gsutil -m cp -r *.tfrecords gs://notram-myzone/notram_v1/pretrain/pretrain_data/

#Unpack and change to the correct directory to copy the unpacked BERT files to the bucket
gsutil -m cp -r *.* gs://notram-myzone/notram_v1/pretrained_models/bert/tf_20/wwm_cased_L-24_H-1024_A-16/

```

## Create a TPU
The TPU needs to be in the same zone as your bucket and VM. The easiest way to create a TPU is through https//console.cloud.google.com -> Compute Engine -> TPUs. Click "CREATE TPU NODE".Create a TPU called "notram-myzone-tpu1". Select for instance a "v3-8". It is important that the TPU runs exactly the same version as the VM. To make sure there has been no updates here, go to the VM and type:
```bash
python -c 'import tensorflow as tf; print(tf.__version__)' 
```
Select the same same version for the "TPU sonftware version" and create the TPU. It will take a minute or two and then your newly created TPU should appear in the console. It will have an internal ip-address that should be used later.
