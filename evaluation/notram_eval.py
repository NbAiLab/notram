# -*- coding: utf-8 -*-
"""Evaluating NoTram models from the National Library of Norway: NER and POS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qUO9l7iyRi8j62IwcCUMgfs8Oxhm4zDw

# Evaluating NoTram models from the National Library of Norway: NER and POS

## Finetuning using Huggingface
In this notebook we will finetune NoTram-BERT for Named Entity Recognition (NER) or Part of Speech (POS) tags using the transformers library by Huggingface.

It is intended for experimentation with the pre-release NoTram models from the National Library of Norway.

Learn more about this library [here](https://huggingface.co/transformers/).

## Before proceeding
Create a copy of this notebook by going to "File - Save a Copy in Drive"

# Settings
"""
# !pip -q install https://github.com/huggingface/transformers/archive/0ecbb698064b94560f24c24fbfbd6843786f088b.zip
# !pip install -qU scikit-learn datasets seqeval conllu pyarrow

import os
#@title ##Model, Dataset, and Task

#model_name = os.environ.get("MODEL_NAME", "bert-base-multilingual-cased")  #@param ["bert-base-multilingual-cased", "./nb_models/eval/eval2", "./nb_models/eval/eval3", "./nb_models/eval/eval4", "./nb_models/eval/eval5", "ltgoslo/norbert"]
model_name = "bert-base-multilingual-cased"

#dataset_name = os.environ.get("DATASET_NAME", "NbAiLab/norne")  #@param ["NbAiLab/norne", "norwegian_ner"]
dataset_name = "NbAiLab/norne"

#dataset_config = os.environ.get("DATASET_CONFIG", "bokmaal")  #@param ["bokmaal", "nynorsk", "samnorsk"]
dataset_config = "bokmaal"

#task_name = os.environ.get("TASK_NAME", "pos")  #@param ["ner", "pos"]
task_name = "pos"

#num_epochs = float(os.environ.get("NUM_EPOCHS", "3.0"))
num_epochs = 1.0

#@title ##General
overwrite_cache = False  #@param {type:"boolean"}
cache_dir = ".cache" #@param {type:"string"}
#output_dir = os.environ.get("OUTPUT_DIR", "./output") #@param {type:"string"}
output_dir = "/var/ml/log"

overwrite_output_dir = True #@param {type:"boolean"}

seed = 42 #@param {type:"number"}

#@title ##Tokenizer
padding = False  #@param ["False", "'max_length'"] {type: 'raw'}
max_length = 512 #@param {type: "number"}
label_all_tokens = False #@param {type:"boolean"}

#@title ## Training
per_device_train_batch_size = 8  #@param {type: "integer"}
per_device_eval_batch_size = 8  #@param {type: "integer"}
learning_rate = 3e-05  #@param {type: "number"}
weight_decay = 0.0  #@param {type: "number"}
adam_beta1 = 0.9  #@param {type: "number"}
adam_beta2 = 0.999  #@param {type: "number"}
adam_epsilon = 1e-08  #@param {type: "number"}
max_grad_norm = 1.0  #@param {type: "number"}
num_train_epochs = num_epochs  #@param {type: "number"}
warmup_steps = 0  #@param {type: "number"}
save_total_limit = 1  #@param {type: "integer"}
load_best_model_at_end = True  #@param {type: "boolean"}

"""# Dependencies and helper functions"""


import logging
import os
import sys
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_datasets as tfds
import transformers
# from datasets import ClassLabel
from datasets import load_dataset
from seqeval.metrics import accuracy_score
from seqeval.metrics import f1_score
from seqeval.metrics import precision_score
from seqeval.metrics import recall_score
from seqeval.metrics import classification_report
# from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
# from sklearn.preprocessing import MultiLabelBinarizer
from tqdm import tqdm
from transformers import (
    AutoConfig,
    AutoModelForTokenClassification,
    AutoTokenizer,
    DataCollatorForTokenClassification,
    PreTrainedTokenizerFast,
    Trainer,
    TrainingArguments,
    pipeline,
    set_seed,
)
from IPython.display import Markdown
from IPython.display import display

#Set seed
set_seed(seed)

# Helper Funtions
def printm(string):
    print(str(string))

"""# Loading Dataset"""

dataset = load_dataset(dataset_name, dataset_config)
dataset

column_names = dataset["train"].column_names
features = dataset["train"].features
text_column_name = "tokens" if "tokens" in column_names else column_names[0]
label_column_name = (
    f"{task_name}_tags" if f"{task_name}_tags" in column_names else column_names[1]
)
dataset["train"].data.to_pandas()[[text_column_name, label_column_name]]

label_list = features[label_column_name].feature.names
label_to_id = {i: i for i in range(len(label_list))}
num_labels = len(label_list)
print(f"Number of labels: {num_labels}")
print({label.split("-")[-1] for label in label_list})

"""# Download Norwegian Models

Downloading the model directly from a GCP bucket should not take longer than 3 minutes.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# # Download Models
# if model_name.startswith("./nb_models") and not os.path.exists("./nb_models"):
#     !mkdir -p nb_models/eval/
#     !gsutil -m cp -r gs://notram-public/nb_models/eval/* nb_models/eval/

"""# Training"""

config = AutoConfig.from_pretrained(
    model_name,
    num_labels=num_labels,
    finetuning_task=task_name,
    cache_dir=cache_dir,
)
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    cache_dir=cache_dir,
    use_fast=True,
)
model = AutoModelForTokenClassification.from_pretrained(
    model_name,
    from_tf=bool(".ckpt" in model_name),
    config=config,
    cache_dir=cache_dir,
)

# Preprocessing the dataset

# Tokenize all texts and align the labels with them.
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(
        examples[text_column_name],
        max_length=max_length,
        padding=padding,
        truncation=True,
        # We use this argument because the texts in our dataset are lists of words (with a label for each word).
        is_split_into_words=True,
    )
    labels = []
    for i, label in enumerate(examples[label_column_name]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            # Special tokens have a word id that is None. We set the label to -100 so they are automatically
            # ignored in the loss function.
            if word_idx is None:
                label_ids.append(-100)
            # We set the label for the first token of each word.
            elif word_idx != previous_word_idx:
                label_ids.append(label_to_id[label[word_idx]])
            # For the other tokens in a word, we set the label to either the current label or -100, depending on
            # the label_all_tokens flag.
            else:
                label_ids.append(label_to_id[label[word_idx]] if label_all_tokens else -100)
            previous_word_idx = word_idx

        labels.append(label_ids)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

tokenized_datasets = dataset.map(
    tokenize_and_align_labels,
    batched=True,
    load_from_cache_file=not overwrite_cache,
    num_proc=os.cpu_count(),
)

# Data collator
data_collator = DataCollatorForTokenClassification(tokenizer)

# Metrics
def compute_metrics(pairs):
    predictions, labels = pairs
    predictions = np.argmax(predictions, axis=2)

    # Remove ignored index (special tokens)
    true_predictions = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]

    # mlb = MultiLabelBinarizer()  # sparse_output=True
    # true_predictions = mlb.fit_transform(true_predictions)
    # mlb = MultiLabelBinarizer()  # sparse_output=True
    # true_labels = mlb.fit_transform(true_labels)

    return {
        "accuracy_score": accuracy_score(true_labels, true_predictions),
        "precision": precision_score(true_labels, true_predictions),
        "recall": recall_score(true_labels, true_predictions),
        "f1": f1_score(true_labels, true_predictions),
        "report": classification_report(true_labels, true_predictions, digits=4)
    }

from transformers.training_args import TrainingArguments

training_args = TrainingArguments(
    output_dir=output_dir,
    overwrite_output_dir=overwrite_output_dir,
    do_train=True,
    do_eval=True,
    do_predict=True,
    per_device_train_batch_size=per_device_train_batch_size,
    per_device_eval_batch_size=per_device_eval_batch_size,
    learning_rate=learning_rate,
    weight_decay=weight_decay,
    adam_beta1=adam_beta1,
    adam_beta2=adam_beta2,
    adam_epsilon=adam_epsilon,
    max_grad_norm=max_grad_norm,
    num_train_epochs=num_train_epochs,
    warmup_steps=warmup_steps,
    load_best_model_at_end=load_best_model_at_end,
    seed=seed,
    save_total_limit=save_total_limit,
    # weight_decay=0.0,
    # adam_beta1=0.9,
    # adam_beta2=0.999,
    # adam_epsilon=1e-08,
    # max_grad_norm=1.0,
    # num_train_epochs=3.0,
    # warmup_steps=0,
    # load_best_model_at_end=True
    # per_device_train_batch_size=8,
    # per_device_eval_batch_size=8,
)
training_args

# Initialize our Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

train_result = trainer.train()
trainer.save_model()  # Saves the tokenizer too for easy upload

output_train_file = os.path.join(output_dir, "train_results.txt")
with open(output_train_file, "w") as writer:
    printm("**Train results**")
    for key, value in sorted(train_result.metrics.items()):
        printm(f"{key} = {value}")
        writer.write(f"{key} = {value}\n")
# Need to save the state, since Trainer.save_model saves only the tokenizer with the model
trainer.state.save_to_json(os.path.join(training_args.output_dir, "trainer_state.json"))

"""# Evaluation"""

printm("**Evaluate**")
results = trainer.evaluate()

output_eval_file = os.path.join(output_dir, "eval_results_ner.txt")
with open(output_eval_file, "w") as writer:
    printm("**Eval results**")
    for key, value in results.items():
        printm(f"{key} = {value}")
        writer.write(f"{key} = {value}\n")

"""# Prediction"""

printm("**Predict**")
test_dataset = tokenized_datasets["test"]
predictions, labels, metrics = trainer.predict(test_dataset)
predictions = np.argmax(predictions, axis=2)

output_test_results_file = os.path.join(output_dir, "test_results.txt")
with open(output_test_results_file, "w") as writer:
    printm("**Predict results**")
    for key, value in sorted(metrics.items()):
        printm(f"{key} = {value}")
        writer.write(f"{key} = {value}\n")

# Remove ignored index (special tokens)
true_predictions = [
    [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
    for prediction, label in zip(predictions, labels)
]

# Save predictions
output_test_predictions_file = os.path.join(output_dir, "test_predictions.txt")
with open(output_test_predictions_file, "w") as writer:
    for prediction in true_predictions:
        writer.write(" ".join(prediction) + "\n")



#Log the results
logfile = os.path.join(output_dir,"evaluation_1301.txt")


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)
test_results = trainer.evaluate()

#Check if logfile exist
try:
    f = open(logfile)
    f.close()
except FileNotFoundError:
    with open(logfile, 'a+') as f:
        print("Creating new log file")
        f.write("model_name" + "\t" + "data_language" + "\t" + "task_name" + "\t" "learning_rate"+ "\t" + "num_epochs"+ "\t" + "validation_f1"+"\t"+"test_f1"+"\n")
    with open(logfile, 'a') as f:
        print("Writing log")
        print(results)
        #import pdb; pdb.set_trace()
        f.write(model_name + "\t" + dataset_config + "\t" + task_name + "\t" + str(learning_rate) + "\t" + str(num_epochs)+ "\t"  + str(results['eval_f1']) + "\t" + str(test_results['eval_f1']) + "\n")




"""---

##### Copyright 2020 &copy; National Library of Norway
"""
