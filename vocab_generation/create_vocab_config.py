import glob

import random, json, glob, os, codecs, random
import numpy as np

import argparse
from os import path

from tokenizers import BertWordPieceTokenizer, tokenizers

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('GeneratedTokenizer', help='generated tokenizer')
    # args = parser.parse_args()

    for tok in glob.glob('tokenizers/*.json'):
        printed=[0] * 500000
        jsonFile = open(tok)
        data = json.load(jsonFile)
        model = data['model']
        vocab = sorted(model['vocab'])
        dname = tok.split("/")[-1]
        if not os.path.exists(dname):
            os.mkdir(dname)
        ofp = open(dname + "/vocab.txt", "w+")
        newvocab = [f'[unused{n}]' for n in range(0, 99)]
        newvocab.extend([t for t in vocab if t.startswith('[') and t.endswith(']')])
        newvocab.extend([t for t in vocab if len(t) == 1])
        newvocab.extend([t for t in vocab if not t.startswith('##') and t not in newvocab])
        newvocab.extend([t for t in vocab if t not in newvocab])
        newvocab = [f'[unused{n}]' for n in range(0, 99)]

        for t in newvocab:
            ofp.write(t +"\n")


        ofp.close()
        specialDataSet = {}
        for i in vocab:
            if i == "[UNK]":
                specialDataSet["unk_token"] = i
            if i == "[SEP]":
                specialDataSet["sep_token"] = i
            if i == "[PAD]":
                specialDataSet["pad_token"] = i
            if i == "[CLS]":
                specialDataSet["cls_token"] = i
            if i == "[MASK]":
                specialDataSet["mask_token"] = i
        outputfile = str(dname) + "/special_tokens_map.json"
        with open(outputfile, 'w+') as f:
            json.dump(specialDataSet, f)

    # print(data["normalizer"]["lowercase"])
        specialDataSet["do_lower_case"] = data["normalizer"]["lowercase"]
        specialDataSet["tokenize_chinese_chars"] = "true"
        specialDataSet["strip_accents"] = "null"
        specialDataSet["special_tokens_map_file"] = "null"
        specialDataSet["name_or_path"] = "/some/path/or/name"
        specialDataSet["do_basic_tokenize"] = "true"
        specialDataSet["never_split"] = "null"
        tokenizerConfigFileName = str(dname) + "/" + str(dname.split(".")[0]) + "_config.json"
        #print(tokenizerConfigFileName)
        with open(tokenizerConfigFileName, 'w+') as f:
            json.dump(specialDataSet, f)
        configSet = {}
        configSet["_name_or_path"] = "someNameOrPath"
        configSet["attention_probs_dropout_prob"] = 0.1
        configSet["directionality"] = "bidi"
        configSet["gradient_checkpointing"] = "false"
        configSet["hidden_act"] = "gelu"
        configSet["hidden_dropout_prob"] = 0.1
        configSet["hidden_size"] = 768
        configSet["initializer_range"] = 0.02
        configSet["intermediate_size"] = 3072
        configSet["layer_norm_eps"] = 1e-12
        configSet["max_position_embeddings"] = 512
        configSet["model_type"] = "bert"
        configSet["num_attention_heads"] = 12
        configSet["num_hidden_layers"] = 12
        configSet["pad_token_id"] = 0
        configSet["pooler_fc_size"] = 768
        configSet["pooler_num_attention_heads"] = 12
        configSet["pooler_num_fc_layers"] = 3
        configSet["pooler_size_per_head"] = 128
        configSet["pooler_type"] = "first_token_transform"
        configSet["type_vocab_size"] = 2
        configSet["vocab_size"] = len(vocab)

        configFileName = str(dname) + "/" + "config.json"
        #print(configFileName)
        with open(configFileName, 'w+') as f:
            json.dump(configSet, f)
        print("==============================================================================")
        print("Tokenizer extractor buildt files for " + tok +":")
        print("\t"+ str(dname) + "/vocab.txt")
        print("\t"+ str(outputfile))
        print("\t"+ str(tokenizerConfigFileName))
        print("\t"+ str(configFileName))
        print("==============================================================================")     