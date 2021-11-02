#!/usr/bin/env python3

######################################################################
### Creates a sub-corpus  - In this example: sami
#####################################################################

from tqdm import tqdm
from utils.misc import ArgParseDefault, add_bool_arg
import jsonlines, json

def main(args):
    with open(args.json_file_list) as file:
        json_file_list = file.readlines()
        json_file_list = [line.rstrip() for line in json_file_list]

    with open(args.docid_list) as file:
        docid_list = file.readlines()
        docid_list = [line.rstrip() for line in docid_list]

    tot = 0    
    hits = 0
    docid_notfound_list = docid_list.copy()

    with jsonlines.open(args.output_file, mode='w') as writer:
        for myfile in tqdm(json_file_list): 
            with jsonlines.open(myfile) as reader:
                for n,obj in enumerate(reader):
                    tot += 1
                    if obj['id'] in docid_list:
                        hits += 1                        
                        try:
                            docid_notfound_list.remove(obj['id'])
                        except:
                            print("Seems like there are multiple versions with this docid in the corpus. This should not happen.")

                        #Prints the json-line to file
                        writer.write(obj)
                        
                        # Prints the docid to screen
                        print(obj['id'])

    
    print(f'*** Finished processing {len(json_file_list)} json-files. Result has {hits} documents of a total {tot} documents evaluated. Result is written to {args.output_file}.')
    print(f'*** A total of {len(docid_notfound_list)} was not found. Listing here for reference:')
    print(docid_notfound_list)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Fill in! Output is an UTF-8 JSON lines")
    parser.add_argument('--json_file_list', required=True, help='List of json-files that should be processed')
    parser.add_argument('--output_file', required=True, help='Path to output file. Will replace existing file.')
    parser.add_argument('--docid_list',required=True, default="config.json", help='List of docids that should be included')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)



