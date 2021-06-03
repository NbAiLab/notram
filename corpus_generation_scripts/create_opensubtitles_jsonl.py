####################################################################################
# Convert the OpenSubtitles corpus to jsonl.
# This corpus is in xml format
# Output is an UTF-8 file with one article per line
####################################################################################

from bs4 import BeautifulSoup
import requests
import ftfy, glob, argparse, os
import jsonlines
from tqdm import tqdm

def main(args):
    #Create the new file. Overwrite if it exits
    f = open(args.output_file, "w+") 
    f.close()

    #Get a list of documents in the folder
    filelist = glob.glob(args.input_folder+'**/*.xml', recursive=True)
    
    n = 0
    with jsonlines.open(args.output_file, 'w') as writer:
        for f in tqdm(filelist):
            html_content = open(f, "r")
            basename = os.path.basename(f).replace(".xml","")
            year = f.split('/')[-3]
            # Parse the html content
            soup = BeautifulSoup(html_content, "lxml")
            
            print(year)
            if(len(year) != 4):
                print(f'{year} - wrong year. Fix')
                exit()

            written = 0
            myarticle = {}
            myarticle['doc_type'] = args.doc_type
            myarticle['id'] = args.doc_type+"_"+basename
            myarticle['publish_date'] = str(year)+"0101"
            myarticle['language_reported'] = args.language_reported
            myarticle['paragraphs'] = [] 
            myarticle['publish_date'] = year+"0101"

            try:
                myarticle['original_language'] = soup.original.text.strip()
            except:
                myarticle['original_language'] = "Unknown"

            try:
                myarticle['genre'] = soup.genre.text.strip()
            except:
                myarticle['genre'] = "Unknown"

            pid = 0

            for s in soup.find_all("s"):
                paragraph = {}
                text = ""
                for w in s.find_all("w"):
                    text += w.text.strip() + " "
                
                text = " ".join(text.split())
                text = ftfy.fix_text(text)

                paragraph['paragraph_id'] = pid
                paragraph['text'] = text
                paragraph['s_id'] = str(s.get('id'))
                 
                try:
                    paragraph['time_id'] = str(s.time.get('id'))
                    paragraph['time_value'] = str(s.time.get('value'))
                except:
                    paragraph['time_id'] = ""
                    paragraph['time_value'] = "0"
                    
                
                myarticle['paragraphs'].append(paragraph)
                pid += 1
               
            #print(myarticle)
            #breakpoint()
            writer.write(myarticle)
            n += 1
            
    print(f'{n} documents from {len(filelist)} files are written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()    
    parser.add_argument('--language_reported', required=False, default="N/A", type=str, help='Language reported. Can be nob, nno, no or N/A')
    parser.add_argument('--doc_type', required=True, type=str, help='For instance government')
    parser.add_argument('-o', '--output_file', required=True, help='Output file name. Will overwrite it exists')
    parser.add_argument('-i', '--input_folder', required=True, help='Input folder. Will read all files in folder')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
#print(soup.prettify()) # print the parsed data of html
