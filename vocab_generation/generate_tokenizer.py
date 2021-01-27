from tokenizers import Tokenizer
from tokenizers.trainers import WordPieceTrainer
from tokenizers.models import WordPiece
from tokenizers.pre_tokenizers import Whitespace

import glob

tokenizer = Tokenizer(WordPiece())
tokenizer.pre_tokenizer = Whitespace()

trainer = WordPieceTrainer(
        vocab_size=50000,
        min_frequency=2,
        show_progress=True,
        special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
        limit_alphabet=1000
)

files = glob.glob('/var/ml/tmpsmall/*.txt')

tokenizer.train(trainer,files)

tokenizer.save('tokenizers/tokenizer_wordpiece_50000.json')
