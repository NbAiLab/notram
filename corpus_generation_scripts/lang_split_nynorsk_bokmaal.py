##################################################
### Splits jsonl-file in Bokmål and nynorsk ######
##################################################

import fasttext
from utils.misc import ArgParseDefault, add_bool_arg
import jsonlines
from tqdm import tqdm
import os

PRETRAINED_MODEL_PATH = '/usr/local/bin/fasttext/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)


def main(args):
    basename = os.path.basename(args.input_file).replace(".jsonl","")
    with jsonlines.open(os.path.join(args.output_folder, basename+'_nn.jsonl'), mode='a') as nnowriter:
        with jsonlines.open(os.path.join(args.output_folder, basename+'_nb.jsonl'), mode='a') as nobwriter:
            with jsonlines.open(args.input_file) as reader:
                for line in tqdm(reader):
                    t = line['text']
                    predictions = model.predict([t]) 
                    lang = str(predictions[0][0][0]).replace("__label__","")
                    conf = float(predictions[1][0][0])
                    
                    if lang=="no" and conf>0.5:
                        nobwriter.write(line)
                    if lang=="nn" and conf>0.5:
                        nnowriter.write(line)
                        #print(f'{t} -  {lang} - {conf}')



def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_folder', required=True, help='Path to output folder.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
