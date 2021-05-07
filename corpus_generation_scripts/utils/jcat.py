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

def print_header(mydict):
    hl = "---------"
    for k in mydict.keys():
        if k != "paragraphs":
            hl += k+"="+str(mydict.get(k,"N/A"))+"---"
    print(hl+"------")


def main(args):
    with jsonlines.open(args.input_file) as f:
        count = 0
        for i,line in enumerate(f.iter()):
            if (args.number_of_articles==-1 or count<= int(args.number_of_articles)) and i >= int(args.start):
                count+=1

                if args.key:
                    value = line.get(args.key, "Not set")
                    print(value)

                else:
                    if int(args.verbose) != 3:
                        print_header(line)

                    paragraphs = line['paragraphs']
                    for p in paragraphs:
                        if int(args.verbose) != 2:
                            if int(args.verbose) == 5:
                                print_header(p)

                            print(f'{p.get("text","[EMPTY]")}\n')
            
            elif count>int(args.number_of_articles):
                break

def parse_args():
    parser = ArgParseDefault()
    parser.add_argument('-n', '--number_of_articles', default=-1, required=False, help='Number of articles')
    parser.add_argument('-s', '--start', default=0, required=False, help='Start at article')
    parser.add_argument('-v', '--verbose', default=3, required=False, help='Choose between headers_only(2), text_only (3=default), text_and_headers(4), paragraph_headers(5)')
    parser.add_argument('-k', '--key', default=None, required=False, help='List only the value from this specific field')
    
    parser.add_argument('input_file', help='Path to input file')
    args = parser.parse_args()  
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)


