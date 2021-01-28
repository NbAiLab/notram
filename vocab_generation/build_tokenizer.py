from tokenizers import Tokenizer
from tokenizers import normalizers
from tokenizers.trainers import WordPieceTrainer
from tokenizers.models import WordPiece
from tokenizers.normalizers import Lowercase
from tokenizers.pre_tokenizers import Whitespace
import glob

tokenizer = Tokenizer(WordPiece())
tokenizer.pre_tokenizer = Whitespace()

tokenizer.normalizer = normalizers.Sequence([Lowercase()])

trainer = WordPieceTrainer(
        vocab_size=29000,
        min_frequency=2,
        show_progress=True,
        special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
        limit_alphabet=500
)

files = glob.glob('/var/ml/tmp/*00.txt')

tokenizer.train(trainer,files)

tokenizer.save('tokenizers/tokenizer_wordpiece_29000_lowercased.json', pretty=True)
