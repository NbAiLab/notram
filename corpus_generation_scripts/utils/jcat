#!/opt/anaconda3/bin/python
import os
import jsonlines
import argparse

class ArgParseDefault(argparse.ArgumentParser):
    """Simple wrapper which shows defaults in help"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

def add_bool_arg(parser, name, default=False, help=''):
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--' + name, dest=name, action='store_true', help=help)
    group.add_argument('--do_not_' + name, dest=name, action='store_false')
    parser.set_defaults(**{name: default})

def main(args):
    with jsonlines.open(args.input_file) as f:
        count = 0
        for i,line in enumerate(f.iter()):
            if (args.n==-1 or count<= int(args.n)) and i >= int(args.start):
                count+=1
                doctype = line.get("doctype","No_doctype_defined")
                docid = line.get("id","No_id_defined")
                scan_date = line.get("scan_date","No_scandate_reported")
                publish_date = line.get("publish_date_date","No_publishdate_reported")
                language_reported = line.get("language_reported","No_language_reported")
                language_detected = line.get("language_detected","No_language_detected")
                confidence = line.get("document_word_confidence","No_page_confidence_defined")
                page = line.get("page","No_page_nr")

                if args.style != "noheader":
                    print(f'\n------(doctype){doctype}---(id){docid}---(scan){scan_date}---(publish){publish_date}---(confidence){confidence}---(lang_det){language_reported}---(lang_rep){language_detected}---(page){page}------\n')
                
                paragraphs = line['paragraphs']
                for p in paragraphs:
                    if args.style != "notext":
                        if args.style == "rich":
                            paragraph_id = p.get("paragraph_id","No_pid_defined")
                            p_page = p.get("page","No_parapgraph_page")
                            p_block = p.get("block","No_parapgraph_block")
                            p_confidence = p.get("confidence","No_parapgraph_confidence")
                            
                            print(f'\n------(pid){paragraph_id}---(page){p_page}---(block){p_block}---(conf){p_confidence}------\n')

                            print(f'{p.get("text","[EMPTY]")}\n')
                        else:
                            print(f'{p.get("text","[EMPTY]")}\n')


def parse_args():
    parser = ArgParseDefault()
    #parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--n', default=-1, required=False, help='Number of articles')
    parser.add_argument('--start', default=0, required=False, help='Start at article')
    parser.add_argument('--style', default="standard", required=False, help='Choose between standard,noheader,rich,notext')
    parser.add_argument("input_file", help='Path to input file')
    args = parser.parse_args()  
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)


