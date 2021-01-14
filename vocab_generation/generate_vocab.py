from tokenizers import BertWordPieceTokenizer

# Initialize an empty BERT tokenizer
tokenizer = BertWordPieceTokenizer(
  clean_text=False,
  handle_chinese_chars=False,
  strip_accents=False,
  lowercase=False,
)

# prepare text files to train vocab on them
files = ['/var/ml/vocab_generation/sentences_colossal_norwegian_corpus_271120_42.txt']
#files = ['/var/ml/vocab_generation/test100000.txt']

# train BERT tokenizer
tokenizer.train(
  files,
  vocab_size=30000,
  min_frequency=2,
  show_progress=True,
  special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
  limit_alphabet=1000,
  wordpieces_prefix="##"
)

# save the vocab
tokenizer.save('tokenizer.json')
