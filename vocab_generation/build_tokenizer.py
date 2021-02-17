from tokenizers import Tokenizer
from tokenizers import normalizers
from tokenizers.trainers import WordPieceTrainer
from tokenizers.models import WordPiece
from tokenizers.normalizers import Lowercase
from tokenizers.pre_tokenizers import Whitespace
import glob

tokenizer = Tokenizer(WordPiece())
tokenizer.pre_tokenizer = Whitespace()

#tokenizer.normalizer = normalizers.Sequence([Lowercase()])

trainer = WordPieceTrainer(
        vocab_size=49500,
        min_frequency=2,
        show_progress=True,
        special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
        limit_alphabet=1500
)

files = glob.glob('/var/ml/tmp/*0.txt')
for _ in range(0,100):
    files.append('emoji/emoji.txt')


tokenizer.train(trainer,files)

tokenizer.save('tokenizers/tokenizer_wordpiece_49500_cased_alphabet1500_emoji_large.json', pretty=True)
