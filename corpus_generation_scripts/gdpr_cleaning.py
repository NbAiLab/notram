import os, sys, jsonlines, json, re
from tqdm import tqdm
from utils.misc import ArgParseDefault, add_bool_arg
import pnr

def main(args):
    # compile regexes
    username_regex = re.compile(r'(^|[^@\w])@(\w{1,15})\b')
    url_regex = re.compile(r'((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))')
    
    pnr_regex1 = re.compile(r'((0[1-9]|[1-2][0-9]|31(?!(?:0[2469]|11))|30(?!02))(0[1-9]|1[0-2])(\d{2})([ \-])(\d{5}))') #240119 88020 with data validation
    pnr_regex2 = re.compile(r'((0[1-9]|[1-2][0-9]|31(?!(?:0[2469]|11))|30(?!02))(0[1-9]|1[0-2])\d{7})') #24011988020 with date validation
    pnr_filler = "111111-11111"
    pnr_list = []
    pnr_doc_type_list = []
    pnr_id_list = []
    pnr_log = {}
    pnr_count = 0

    email_regex = re.compile(r'[\w\.-]+@[\w\.-]+')
    email_filler='email@email.no'
    email_log = {}
    email_count = 0

    if not os.path.isdir(args.output_folder):
        print("Output folder does not exist. Create it and then retry.")
        exit()
    else:
        base = os.path.basename(args.input_file)
        output_file = os.path.join(args.output_folder,base)
        if os.path.exists(output_file):
            os.remove(output_file)

    if not os.path.isdir(os.path.join(args.output_folder,"log")):
        os.mkdir(os.path.join(args.output_folder,"log"))
    
    log_file = os.path.join(args.output_folder,"log",base)
    if os.path.exists(log_file):
            os.remove(log_file)

    if args.input_file == output_file or args.input_file == log_file or output_file == log_file:
        print("Input, ouput and log file needs to be uniqu.")
        exit()

    with jsonlines.open(output_file, 'a') as writer:    
        with jsonlines.open(log_file, 'a') as log_writer:    
            with jsonlines.open(args.input_file) as reader:
                for n,line in enumerate(reader):
                    output_line = line
                    #Pnr removal
                    match = re.findall(pnr_regex1, line['text'])
                    if match:
                        for p in match:
                            if pnr.IsValidNorwegianPersonalIdentificationNumber(p[0].replace(" ","").replace("-","")):
                                pnr_count += 1
                                pnr_log = {"id":line['id'],"doc_type": line['doc_type'], "pnr":p[0], "filler":pnr_filler}
                                log_writer.write(pnr_log)
                                output_line['text'] = re.sub(pnr_regex1, pnr_filler, output_line['text'])

                    match = re.findall(pnr_regex2, line['text'])
                    if match:
                        for p in match:
                            if pnr.IsValidNorwegianPersonalIdentificationNumber(p[0].replace(" ","").replace("-","")):
                                pnr_count += 1
                                pnr_log = {"id":line['id'],"doc_type": line['doc_type'], "pnr":p[0], "filler":pnr_filler}
                                log_writer.write(pnr_log)
                                output_line['text'] = re.sub(pnr_regex2, pnr_filler, output_line['text'])

                    #Email removal
                    match = re.findall(email_regex, line['text'])
                    if match:
                        for e in match:
                            email_count += 1
                            email_log = {"id":line['id'],"doc_type": line['doc_type'], "email":e, "filler":email_filler}
                            log_writer.write(email_log)

                        output_line['text'] = re.sub(email_regex, email_filler, output_line['text'])

                    #if not n%10000:
                    #    print(".", end = '', flush=True)
                    
        
                    writer.write(output_line)
            
    print(f'\n{args.input_file} - found {email_count} emails and {pnr_count} pnr.')
    

def parse_args():
    parser = ArgParseDefault(description="Makes the corpus more GDPR compliant by removing all email addresses and Norwegian personal identification numbers.")
    parser.add_argument('--input_file', required=True, help='Path to input file.')
    parser.add_argument('--output_folder', required=True, help='Path to output folder.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)



