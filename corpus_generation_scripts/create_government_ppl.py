from bs4 import BeautifulSoup
import requests
import ftfy, glob, argparse

def main(args):
    #Create the new file. Overwrite if it exits
    f = open(args.output_file, "w+") 
    f.close()

    #Get a list of documents in the folder
    filelist = glob.glob(args.input_folder+'*.xhtml')
    n = 0
    for f in filelist:
        html_content = open(f, "r")

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")

        
        written = 0
        for p in soup.find_all("p"):
            text = p.text.strip()
            text = ftfy.fix_text(text)
            if len(text):
                if text[-1] != '.' and text[-1] != ":":
                    ...
                    # print(f'Heading or bulleted list: {text}')
                else:
                    if p.parent:
                        thisclasses = p.get('class')
                        parentclasses = p.parent.get('class')
                        if not parentclasses:
                            parentclasses = []
                        if not thisclasses:
                            thisclasses = []

                        if 'K-REFLISTE' in thisclasses:
                            ...
                            #print(f"Removed {p.get('class')} - {text}\n")

                        elif 'TOP' in parentclasses:
                            ...
                            #print(f"Removed {p.parent.get('class')} - {text}\n") 

                        elif 'K-NOTE-TBLNOTER' in parentclasses:
                            ...
                            #print(f"Removed {p.parent.get('class')} - {text}\n") 
                            
                        
                        elif 'K-NOTETEXT' in parentclasses:
                            ...
                            #print(f"Removed {p.parent.get('class')} - {text}\n") 
                        
                        else:
                            if len(text.split()) >= 10 and not text.startswith("Det har oppstått en teknisk feil.") and not text.startswith("A technical error has occurred. You can try to locate relevant documents"):
                                f=open(args.output_file, 'a+')
                                f.write(text+'\n')
                                f.close()
                                written = 1
                                n+=1
        
        if written:
            #Add an extra lineshift to separate documents
            f=open(args.output_file, 'a+')
            f.write('\n')
            f.close()
    
    print(f'{n} paragraphs from {len(filelist)} files are written to {args.output_file}')


def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', required=True, help='Output file name. Will overwrite it exists')
    parser.add_argument('-i', '--input_folder', required=True, help='Input folder. Will read all files in folder')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    main(args)
#print(soup.prettify()) # print the parsed data of html