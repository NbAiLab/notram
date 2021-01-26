from tokenizers import BertWordPieceTokenizer, SentencePieceBPETokenizer
import glob

# Initialize an empty BERT tokenizer
#tokenizer = BertWordPieceTokenizer(
#  clean_text=True,
#  handle_chinese_chars=False,
#  strip_accents=False,
#  lowercase=False,
#)

tokenizer = SentencePieceBPETokenizer()




# prepare to train vocab on them
#files = ['/var/ml/vocab_generation/sentences_colossal_norwegian_corpus_271120_42.txt']
#files = ['/var/ml/vocab_generation/test100000.txt']
files = glob.glob('/var/ml/tmp/*.txt')
#files = glob.glob('/nfsmounts/meta2/disk4/folder1/nancy/content/text/v3/sentence_segm_5/*.txt')

#print(files)
#print(len(files))
#exit()

# train BERT tokenizer
tokenizer.train(
  files,
  vocab_size=50000,
  min_frequency=2,
  show_progress=True,
  special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
  limit_alphabet=1000,
  #wordpieces_prefix="##"
)

# save the vocab
tokenizer.save('generated_tokenizers/tokenizer_sentencepiecetokenizer_clean_true.json')
