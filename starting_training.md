# Starting training
This goes through the process of actually the training on a TPU v3-8. Before attempting this, make sure that you have the following files:
* Generated tfrecord-files
* Vocab-file used for generating the tfrecord-files
* Config.js file describing the network
* Pre-trained model if you do not want to randomly initiating the weights


### Authenticate
Run both these command to make sure the VM is correctly authenticated.

```bash
gclour auth login
gcloud auth application-default login
```

