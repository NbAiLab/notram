# -*- coding: utf-8 -*-
"""Evaluating NoTram models from the National Library of Norway: NER and POS
Copyright 2020 &copy; National Library of Norway

Evaluating NoTram models from the National Library of Norway: NER and POS
"""

# Dependencies
# !pip -q install https://github.com/huggingface/transformers/archive/0ecbb698064b94560f24c24fbfbd6843786f088b.zip
# !pip install -qU scikit-learn datasets seqeval conllu pyarrow

# Dependencies and helper functions
import argparse
import logging
import os
import random
import sys
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Optional

import datasets
import numpy as np
import pandas as pd
import transformers
# from datasets import ClassLabel
from datasets import load_dataset
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from seqeval.metrics.sequence_labeling import accuracy_score as seq_accuracy_score
from seqeval.metrics.sequence_labeling import f1_score as seq_f1_score
from seqeval.metrics.sequence_labeling import precision_score as seq_precision_score
from seqeval.metrics.sequence_labeling import recall_score as seq_recall_score
from seqeval.metrics.sequence_labeling import classification_report as seq_classification_report
from sklearn.metrics import accuracy_score as sk_accuracy_score
from sklearn.metrics import f1_score as sk_f1_score
from sklearn.metrics import precision_score as sk_precision_score
from sklearn.metrics import recall_score as sk_recall_score
from sklearn.metrics import classification_report as sk_classification_report
# from sklearn.preprocessing import MultiLabelBinarizer
from tqdm import tqdm
from transformers import (
    AutoConfig,
    AutoModelForTokenClassification,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    RobertaTokenizer,
    RobertaTokenizerFast,
    DataCollatorForTokenClassification,
    DataCollatorWithPadding,
    PreTrainedTokenizerFast,
    Trainer,
    TrainingArguments,
    pipeline,
    set_seed,
)
# from transformers.training_args import TrainingArguments
import wandb


# Helper Funtions
def printm(string):
    print(str(string))


def supercase_token(token):
    shift = "⇧"
    caps = "⇪"
    # Check if entire token is at least two characters and is entirely uppercased
    if len(token) >= 2 and token == token.upper() and token[0].isalpha():
        return token.lower() + caps
    # Check if upper
    elif token[0].isupper():
        return token.lower() + shift
    # If none of this is true, return original
    else:
        return token.lower()


def supercase_text(text):
    return TreebankWordDetokenizer().detokenize(
        map(supercase_token, word_tokenize(text))
    )


def supercase(text, is_split_into_words=False):
    supercase_func = supercase_token if is_split_into_words else supercase_text
    if isinstance(text, str):
        return supercase_func(text)
    elif isinstance(text, list):
        if all(isinstance(elem, list) for elem in text):
            return [list(map(supercase_func, t)) for t in text]
        else:
            return list(map(supercase_func, text))
    else:
        return text


# Tokenize all texts and align the labels with them.
def tokenize_and_align_labels(
    tokenizer, examples, text_column_name, max_length, padding,
    label_column_name, label_to_id, label_all_tokens, do_supercase=False
):
    tokenized_inputs = tokenizer(
        supercase(
            examples[text_column_name], is_split_into_words=True
        ) if do_supercase else examples[text_column_name],
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


# Metrics
def token_compute_metrics(pairs, label_list):
    """Token metrics based on seqeval"""
    raw_predictions, labels = pairs
    predictions = np.argmax(raw_predictions, axis=2)

    # Remove ignored index (special tokens)
    true_predictions = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_probas = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    raw_scores = (
        np.exp(raw_predictions) / np.exp(raw_predictions).sum(-1, keepdims=True)
    )
    scores = raw_scores.max(axis=2)
    true_scores = [
        [(s, l) for (s, l) in zip(score, label) if l != -100]
        for score, label in zip(scores, labels)
    ]

    # mlb = MultiLabelBinarizer()  # sparse_output=True
    # true_predictions = mlb.fit_transform(true_predictions)
    # mlb = MultiLabelBinarizer()  # sparse_output=True
    # true_labels = mlb.fit_transform(true_labels)
    # wandb.log({
    #     "roc" : wandb.plot.roc_curve(
    #         labels,
    #         predictions,
    #         labels=label_list
    # )})
    metrics = {
        "accuracy": seq_accuracy_score(true_labels, true_predictions),
        "precision_micro": seq_precision_score(true_labels, true_predictions, average="micro"),
        "recall_micro": seq_recall_score(true_labels, true_predictions, average="micro"),
        "f1_micro": seq_f1_score(true_labels, true_predictions, average="micro"),
        "precision_macro": seq_precision_score(true_labels, true_predictions, average="macro"),
        "recall_macro": seq_recall_score(true_labels, true_predictions, average="macro"),
        "f1_macro": seq_f1_score(true_labels, true_predictions, average="macro"),
        # "report": seq_classification_report(true_labels, true_predictions, digits=4)
    }
    reports = seq_classification_report(
        true_labels, true_predictions, output_dict=True, zero_division=0,
    )
    for label, report in reports.items():
        for metric_key, metric_value in report.items():
            metric_title = metric_key.replace(" avg", "_avg", 1)
            metrics.update({
                f"label_{label}_{metric_title}": metric_value,
            })
    # labels_to_plot = label_list.copy()
    # if "O" in labels_to_plot:
    #     labels_to_plot.remove("O")
    flat_true_labels = sum(true_labels, [])
    flat_true_predictions = sum(true_predictions, [])
    wandb.log({
        # "roc": wandb.plot.roc_curve(
        #     labels.reshape(-1),
        #     raw_scores.reshape(-1, raw_predictions.shape[-1]),
        #     labels=label_list,
        #     classes_to_plot=labels_to_plot,
        # ),
        "matrix": wandb.sklearn.plot_confusion_matrix(
            flat_true_labels, flat_true_predictions, label_list
        )
    })
    return metrics


def sequence_compute_metrics(pairs, label_list):
    """Sequence metrics based on sklearn"""
    raw_predictions, labels = pairs
    predictions = np.argmax(raw_predictions, axis=1)
    metrics = {
        "accuracy": sk_accuracy_score(labels, predictions),
        "precision_micro": sk_precision_score(labels, predictions, average="micro"),
        "recall_micro": sk_recall_score(labels, predictions, average="micro"),
        "f1_micro": sk_f1_score(labels, predictions, average="micro"),
        "precision_macro": sk_precision_score(labels, predictions, average="macro"),
        "recall_macro": sk_recall_score(labels, predictions, average="macro"),
        "f1_macro": sk_f1_score(labels, predictions, average="macro"),
        # "report": sk_classification_report(labels, predictions, digits=4)
    }
    reports = sk_classification_report(
        labels, predictions, target_names=label_list, output_dict=True,
    )
    for label, report in reports.items():
        if not isinstance(report, dict):
            report = {"": report}
        for metric_key, metric_value in report.items():
            metric_title = metric_key.replace(" avg", "_avg", 1)
            metrics.update({
                f"label_{label}_{metric_title}": metric_value,
            })
    wandb.log({
        "roc": wandb.plot.roc_curve(
            labels, raw_predictions, labels=label_list
        ),
        "matrix": wandb.sklearn.plot_confusion_matrix(
            labels, predictions, label_list
        )
    })
    return metrics


def write_file(kind, metrics, output_dir, save_artifact=False):
    output_file = output_dir / f"{kind}_results.txt"
    headers = []
    label_headers = []
    data = []
    label_data = []
    with open(output_file, "w") as writer:
        printm(f"**{kind.capitalize()} results**")
        for key, value in metrics.items():
            printm(f"\t{key} = {value}")
            writer.write(f"{key} = {value}\n")
            title = key.replace("eval_", "", 1)
            if title.startswith("label_"):
                label_headers.append(title.replace("label_", "", 1))
                label_data.append(value)
            else:
                headers.append(title)
                data.append(value)
            wandb.log({f"{kind}:{title}": value})
    wandb.log({kind: wandb.Table(data=[data], columns=headers)})
    if label_headers:
        wandb.log({
            f"{kind}:labels": wandb.Table(
                data=[label_data], columns=label_headers
            )
        })
    if save_artifact:
        artifact = wandb.Artifact(kind, type="result")
        artifact.add_file(str(output_file))
        wandb.log_artifact(artifact)


def dataset_select(dataset, size):
    dataset_len = len(dataset)
    if size < 0 or size > dataset_len:
        return dataset
    elif size <= 1:  # it's a percentage
        return dataset.select(range(int(size * dataset_len)))
    else:  # it's a number
        return dataset.select(range(int(size)))


def extract_revision(name):
    if name and "@" in name:
        return name.split("@")
    else:
        return name, None


def main(args):
    # Set seed
    if args.run:
        seed = random.randrange(10**3)
    else:
        seed = args.seed
    set_seed(seed)
    # Run name
    model_name = args.model_name
    model_name = model_name[2:] if model_name.startswith("./") else model_name
    model_name = model_name[1:] if model_name.startswith("/") else model_name
    run_name = f"{model_name}_{args.task_name}"
    run_name = f"{run_name}_{args.dataset_config or args.dataset_name}"
    run_name = run_name.replace("/", "-")
    run_name = f"{run_name}_e{str(args.num_train_epochs)}"
    run_name = f"{run_name}_lr{str(args.learning_rate)}"
    run_name = f"{run_name}_ws{str(args.warmup_steps)}"
    run_name = f"{run_name}_wd{str(args.weight_decay)}"
    run_name = f"{run_name}_ab1{str(args.adam_beta1)}"
    run_name = f"{run_name}_ab2{str(args.adam_beta2)}"
    run_name = f"{run_name}_ae{str(args.adam_epsilon)}"
    run_name = f"{run_name}_s{str(seed)}"

    if args.max_length != 512:
        run_name = f"{run_name}_seq{str(args.max_length)}"
    if args.label_all_tokens:
        run_name = f"{run_name}_labelall"
    do_supercase = args.supercase or "supercased" in run_name
    if do_supercase and "supercased" not in run_name:
        run_name = f"{run_name}_supercased"
    if args.run:
        run_name = f"{run_name}_r{str(args.run)}"
    output_dir = Path(args.output_dir) / run_name
    # Tokenizer settings
    padding = args.task_name not in ("ner", "pos")  # default: False @param ["False", "'max_length'"] {type: 'raw'}
    max_length = args.max_length #@param {type: "number"}
    # Training settings
    weight_decay = args.weight_decay  #@param {type: "number"}
    adam_beta1 = args.adam_beta1  # 0.9  #@param {type: "number"}
    adam_beta2 = args.adam_beta2  # 0.999  #@param {type: "number"}
    adam_epsilon = args.adam_epsilon  # 1e-08  #@param {type: "number"}
    max_grad_norm = 1.0  #@param {type: "number"}
    save_total_limit = 1  #@param {type: "integer"}
    load_best_model_at_end = False  #@param {type: "boolean"}
    # wandb
    wandb.init(name=run_name, entity="nbailab")
    wandb.log({
        "seed": int(seed),
    })
    # Loading Dataset
    print("\n\n#####################################")
    print(args.model_name)
    print(args.task_name)
    print(args.dataset_config)
    train_split = args.dataset_split_train
    test_split = args.dataset_split_test
    validation_split = args.dataset_split_validation
    if ":" in args.dataset_name:
        dataset_name, dataset_config = args.dataset_name.split(":")
    else:
        dataset_name = args.dataset_name
        dataset_config = args.dataset_config
    if dataset_config is None or len(dataset_config) == 0:
        dataset = load_dataset(dataset_name)
    else:
        dataset = load_dataset(dataset_name, dataset_config)
    column_names = dataset[train_split].column_names
    features = dataset[train_split].features
    if "tokens" in column_names:
        text_column_name = "tokens"
    elif "text" in column_names:
        text_column_name = "text"
    else:
        text_column_name = column_names[0]
    if f"{args.task_name}_tags" in column_names:
        label_column_name = f"{args.task_name}_tags"
    elif "label" in column_names:
        label_column_name = "label"
    else:
        label_column_name = column_names[1]
    if isinstance(features[label_column_name], datasets.features.Sequence):
        label_list = features[label_column_name].feature.names
    else:
        label_list = features[label_column_name].names
    label_to_id = {i: i for i in range(len(label_list))}
    num_labels = len(label_list)
    print(f"Number of labels: {num_labels}")
    print({label.split("-")[-1] for label in label_list})

    # Download Norwegian Models
    # Downloading the model directly from a GCP bucket should not take longer than 3 minutes.
    # if args.model_name.startswith("./nb_models") and not os.path.exists("./nb_models"):
    #     !mkdir -p nb_models/eval/
    #     !gsutil -m cp -r gs://notram-public/nb_models/eval/* nb_models/eval/

    # Training
    model_name, revision = extract_revision(args.model_name)
    config = AutoConfig.from_pretrained(
        model_name,
        num_labels=num_labels,
        finetuning_task=args.task_name,
        cache_dir=args.cache_dir,
        force_download=args.force_download,
        revision=revision,
        use_auth_token=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        cache_dir=args.cache_dir,
        use_fast=True,
        force_download=args.force_download,
        revision=revision,
        use_auth_token=True,
    )
    if isinstance(tokenizer, (RobertaTokenizer, RobertaTokenizerFast)):
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            cache_dir=args.cache_dir,
            use_fast=True,
            force_download=args.force_download,
            revision=revision,
            use_auth_token=True,
            add_prefix_space=True,
        )
    tokenizer_test_sentence = """
    Denne gjengen håper at de sammen skal bidra til å gi kvinnefotballen i Kristiansand et lenge etterlengtet løft.
    """.strip()
    printm("""Tokenizer test""")
    printm(f"> {tokenizer_test_sentence}")
    if do_supercase:
        tokenizer_test_sentence = supercase(tokenizer_test_sentence, args.task_name in ("pos", "ner"))
    printm(tokenizer.tokenize(tokenizer_test_sentence))
    printm(tokenizer(tokenizer_test_sentence).input_ids)
    # Token tasks
    if args.task_name in ("pos", "ner"):
        model = AutoModelForTokenClassification.from_pretrained(
            model_name,
            from_tf=bool(".ckpt" in args.model_name),
            config=config,
            cache_dir=args.cache_dir,
            force_download=args.force_download,
            from_flax=args.from_flax,
            revision=revision,
            use_auth_token=True,
        )
        # Preprocessing the dataset
        tokenized_datasets = dataset.map(
            lambda examples: tokenize_and_align_labels(
                tokenizer, examples, text_column_name, max_length, padding,
                label_column_name, label_to_id, args.label_all_tokens,
                do_supercase),
            batched=True,
            load_from_cache_file=not args.overwrite_cache,
            num_proc=os.cpu_count(),
        )
        # Data collator
        data_collator = DataCollatorForTokenClassification(tokenizer)
        compute_metrics = token_compute_metrics
    # Sequence tasks
    else:
        model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            from_tf=bool(".ckpt" in model_name),
            config=config,
            cache_dir=args.cache_dir,
            force_download=args.force_download,
            from_flax=args.from_flax,
            revision=revision,
            use_auth_token=True,
        )
        # Preprocessing the dataset
        tokenized_datasets = dataset.map(
            lambda examples: tokenizer(
                supercase(
                    examples[text_column_name], is_split_into_words=False
                ) if do_supercase else examples[text_column_name],
                max_length=max_length,
                padding=padding,
                truncation=True,
                is_split_into_words=False,
            ),
            batched=True,
            load_from_cache_file=not args.overwrite_cache,
            num_proc=os.cpu_count(),
        )
        # Data collator
        data_collator = DataCollatorWithPadding(
            tokenizer,
            max_length=max_length,
            padding=padding,
        )
        compute_metrics = sequence_compute_metrics
    train_dataset = dataset_select(
        tokenized_datasets[train_split], args.max_train_size
    )
    test_dataset = dataset_select(
        tokenized_datasets[test_split], args.max_test_size
    )
    validation_dataset = dataset_select(
        tokenized_datasets[validation_split], args.max_validation_size
    )
    wandb.log({
        "train_size": len(train_dataset),
        "test_size": len(test_dataset),
        "validation_size": len(validation_dataset),
    })
    samples_per_batch = (
        train_dataset.shape[0] / args.train_batch_size
    )
    total_steps = args.num_train_epochs * samples_per_batch
    warmup_steps = int(args.warmup_steps * total_steps)
    wandb.log({
        "total_steps": int(total_steps),
        "total_warmup_steps": warmup_steps
    })
    do_eval = args.do_eval and (validation_split in tokenized_datasets)
    do_test = args.do_test and (test_split in tokenized_datasets)
    do_predict = args.do_predict and (test_split in tokenized_datasets)
    training_args = TrainingArguments(
        output_dir=output_dir.as_posix(),
        overwrite_output_dir=args.overwrite_output_dir,
        do_train=args.do_train,
        do_eval=do_eval,
        do_predict=do_test or do_predict,
        per_device_train_batch_size=int(args.train_batch_size),
        per_device_eval_batch_size=int(args.eval_batch_size or args.train_batch_size),
        learning_rate=float(args.learning_rate),
        weight_decay=weight_decay,
        adam_beta1=adam_beta1,
        adam_beta2=adam_beta2,
        adam_epsilon=adam_epsilon,
        max_grad_norm=max_grad_norm,
        num_train_epochs=args.num_train_epochs,
        warmup_steps=warmup_steps,
        load_best_model_at_end=load_best_model_at_end,
        seed=seed,
        save_total_limit=save_total_limit,
        run_name=run_name,
        disable_tqdm=False,
        eval_steps=500,
        report_to="all",
    )
    # Initialize our Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=validation_dataset if do_eval else None,
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=lambda pairs: compute_metrics(pairs, label_list),
    )
    if args.do_train:
        train_result = trainer.train()
        trainer.save_model()  # Saves the tokenizer too for easy upload
        write_file("train", train_result.metrics, output_dir, save_artifact=args.save_artifacts)
        # Need to save the state, since Trainer.save_model saves only the tokenizer with the model
        trainer.state.save_to_json(output_dir / "trainer_state.json")
    # Evaluation
    if do_eval:
        printm(f"**Evaluate**")
        results = trainer.evaluate()
        write_file("eval", results, output_dir, save_artifact=args.save_artifacts)
    # Tesing and predicting
    if do_test or do_predict:
        printm("**Test**" if not do_predict else "***Predict***")
        predictions, labels, metrics = trainer.predict(test_dataset)
        if not do_predict:
            write_file("test", metrics, output_dir, save_artifact=args.save_artifacts)
        if args.task_name in ("ner", "pos"):
            predictions = np.argmax(predictions, axis=2)
            # Remove ignored index (special tokens)
            true_predictions = [
                [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
                for prediction, label in zip(predictions, labels)
            ]
        else:
            predictions = np.argmax(predictions, axis=1)
            true_predictions = [
                label_list[p] for (p, l) in zip(predictions, labels) if l != -100
            ]
        # Save predictions
        output_test_predictions_file = os.path.join(output_dir, "test_predictions.txt")
        output_test_predictions = "\n".join(" ".join(map(str, p)) for p in true_predictions)
        with open(output_test_predictions_file, "a+") as writer:
            writer.write(output_test_predictions)
        if args.save_artifacts:
            artifact = wandb.Artifact("predictions", type="result")
            artifact.add_file(output_test_predictions_file)
            wandb.log_artifact(artifact)
    # # Log the results
    # logfile = output_dir / "evaluation.csv"
    # # Check if logfile exist
    # try:
    #     f = open(logfile)
    #     f.close()
    # except FileNotFoundError:
    #     with open(logfile, 'a+') as f:
    #         f.write("model_name" + "\t" + "data_language" + "\t" + "task_name" + "\t" "learning_rate"+ "\t" + "num_epochs"+ "\t" + "warmup_steps"+ "\t" + "validation_f1" +"\t"+"test_f1"+"\n")
    # with open(logfile, 'a') as f:
    #     print(results)
    #     f.write(args.model_name + "\t" + (args.dataset_config or args.dataset_name) + "\t" + args.task_name + "\t" + str(args.learning_rate) + "\t" + str(args.num_train_epochs)+ "\t" + str(warmup_steps)+ "\t" + str(results['eval_f1']) + "\t" + str(metrics['eval_f1']) + "\n")


if __name__ == "__main__":
    # yesno = lambda x: str(x).lower() in {'true', 't', '1', 'yes', 'y'}
    parser = argparse.ArgumentParser(description=f""
    f"Evaluating NoTraM models for token and sequence classification"""
    f"", epilog=f"""Example usage:
    {__file__} --task_name ner --model_name "NbAiLab/nb-bert-base"
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--model_name',
        metavar='model_name', help='Model name or path')
    parser.add_argument('--dataset_name', default="NbAiLab/norne",
        metavar='dataset_name', help='Dataset name. It might enforce a config if added after a semicolon: "conll2002:es". This will ignore dataset_config, useful when run in grid search')
    parser.add_argument('--dataset_config',
        metavar='dataset_config', help='Dataset config name')

    parser.add_argument('--dataset_split_train', default="train",
        metavar='dataset_split_train', help='Dataset train split name')
    parser.add_argument('--dataset_split_test', default="test",
        metavar='dataset_split_test', help='Dataset test split name')
    parser.add_argument('--dataset_split_validation', default="validation",
        metavar='dataset_split_validation', help='Dataset validation split name')

    parser.add_argument('--max_train_size', type=float, default=-1.0,
        metavar='max_train_size', help='Percentage of train dataset or number of rows to use')
    parser.add_argument('--max_test_size', type=float, default=-1.0,
        metavar='max_test_size', help='Percentage of test dataset or number of rows to use')
    parser.add_argument('--max_validation_size', type=float, default=-1.0,
        metavar='max_validation_size', help='Percentage of validation dataset or number of rows to use')

    parser.add_argument('--do_train',
        metavar='do_train', default=True, type=bool,
        help='Run training',
    )
    parser.add_argument('--do_eval',
        metavar='do_eval', default=True, type=bool,
        help='Run evaluation on validation test',
    )
    parser.add_argument('--do_test',
        metavar='do_test', default=True, type=bool,
        help='Run evaluation on test set',
    )
    parser.add_argument('--do_predict',
        metavar='do_predict', default=False, type=bool,
        help='Run prediction only on test set',
    )

    parser.add_argument('--supercase',
        metavar='supercase', type=bool, default=False,
        help='Supercase (lower case and add casing token) datasets',
    )
    parser.add_argument('--task_name',
        metavar='task_name', default="ner",
        help='Task name (supported in the dataset), either ner or pos',
    )
    parser.add_argument('--num_train_epochs',
        metavar='num_train_epochs', default=4, type=float,
        help='Number of training epochs',
    )
    parser.add_argument('--cache_dir',
        metavar='cache_dir', default="/var/ml/cache/",
        help='Cache dir for the transformer library',
    )
    parser.add_argument('--overwrite_cache',
        metavar='overwrite_cache', default=False, type=bool,
        help='Overwrite cache dir if present',
    )
    parser.add_argument('--output_dir',
        metavar='output_dir', default="/var/ml/output/",
        help='Output dir for models and logs',
    )
    parser.add_argument('--overwrite_output_dir',
        metavar='overwrite_output_dir', default=True, type=bool,
        help='Overwrite output dir if present',
    )
    parser.add_argument('--seed',
        metavar='seed', type=int, default=2021,
        help='Seed for the experiments',
    )
    parser.add_argument('--run',
        metavar='run', type=int,
        help='Control variable for doing several runs of the same experiment. It will force random seeds even across the same set of parameters fo a grid search',
    )
    parser.add_argument('--train_batch_size',
        metavar='train_batch_size', type=int, default=8,
        help='Batch size for training',
    )
    parser.add_argument('--eval_batch_size',
        metavar='eval_batch_size', type=int,
        help='Batch size for evaluation. Defaults to train_batch_size',
    )
    parser.add_argument('--max_length',
        metavar='max_length', type=int, default=512,
        help='Maximum sequence length',
    )
    parser.add_argument('--learning_rate',
        metavar='learning_rate', type=str, default="3e-05",
        help='Learning rate',
    )
    parser.add_argument('--warmup_steps',
        metavar='warmup_steps', type=float, default=0.0,
        help='Warmup steps as percentage of the total number of steps',
    )
    parser.add_argument('--weight_decay',
        metavar='weight_decay', type=float, default=0.0,
        help='Weight decay',
    )
    parser.add_argument('--adam_beta1',
        metavar='adam_beta1', type=float, default=0.9,
        help='AdamW beta1',
    )
    parser.add_argument('--adam_beta2',
        metavar='adam_beta2', type=float, default=0.999,
        help='AdamW beta2',
    )
    parser.add_argument('--adam_epsilon',
        metavar='adam_epsilon', type=float, default=1e-8,
        help='AdamW epsilon',
    )
    parser.add_argument('--label_all_tokens',
        metavar='label_all_tokens', type=bool, default=False,
        help=('Whether to put the label for one word on all tokens of '
              'generated by that word or just on the one (in which case the '
              'other tokens will have a padding index).'),
    )
    parser.add_argument('--force_download',
        metavar='force_download', type=bool, default=False,
        help='Force the download of model, tokenizer, and config',
    )
    parser.add_argument('--save_artifacts',
        metavar='save_artifacts', type=bool, default=False,
        help='Save train, eval, and test files in Weight & Biases',
    )

    parser.add_argument('--from_flax',
        metavar='from_flax', default=False, type=bool,
        help='Load models from Flax format',
    )

    args = parser.parse_args()
    main(args)
