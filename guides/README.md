# Guides
A collection of documentation and guides used for creating the NB-models. This is used internally as a collaboration tool. However, we also hope that it can be useful for other that want to replicate our work. The is the complete set of scripts needed going from source to corpus file and HF (HugingFace) dataset.

The process consists of five separate steps from source to corpus and HuggingFace (HF) dataset.

## Specifications
* [Process overview] (corpus_building.md)
* [Internal jsonl-format](text_extraction_format.md)

## Creating da*taset
* [Creating the Norwegian Collossal Corpus v2](creating_corpus_v2.md)
* [Exporting dataset to HuggingFace](creating_huggingface_dataset.md)
* [Processing MC4 (obsolete)](prepare_common_crawl.md)

## Flax
* [Guide for setting up Flax and training RoBERTa, T5 and GPTNeo](flax.md)

## Tensorflow
* [Trained Tensorflow models](models_tensorflow.md)
* [Configuring a VM](configure_vm_tensorflow.md)
* [Create VM, bucket and TPU](create_vm_bucket_tpu_tensorflow.md)
* [Starting training](start_training_tensorflow.md)
* [Publish Tensorflow Checkpoint](publish_checkpoint.md)

