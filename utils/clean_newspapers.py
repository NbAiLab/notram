####################################################################################
# Cleaning up newspaper corpuis
# These are the unpacked files in the 2/ directory
# Output is an UTF-8 file with one article per line
####################################################################################

import sys, glob, os, re, argparse
import pandas as pd

def main(args):
    minimum_number_of_words_in_an_article = 1
    all_articles = ""
    valid_segment_count = 0
    total_article_count = 0

    for file in glob.glob(os.path.join(args.input_path,'2/*/*/*.html4')):
        content=""
        total_article_count += 1
        #Specify the encoding while opening it
        with open(file, encoding="ISO-8859-1") as f:
            for n in f.readlines():
                if n.startswith('##U'):
                    content = content + '##U'
                elif not (n.startswith('##B') or n.startswith('##A') or n.startswith('##M') or n.startswith('##D') or n.startswith('Publisert: ') or n.startswith('Oppdatert: ')):
                    content = content + n
        
        #Linebreaks are non funcitonal here and should just be removed in the start
        content = content.replace("\n"," ")
        content = content.replace("(© NTB)","")
        content = content.replace("   ¶","\n")
        content = content.replace("  ¶","\n")
        content = content.replace("¶","\n")
       
        content = content.replace('##U','\n')
       
        #All 
        articles = content.split('\n')

        for article in articles:
            if len(str(article).split()) >= minimum_number_of_words_in_an_article:
                valid_segment_count += 1
                all_articles += str(article).strip() + '\n'
   

    print("Finished parsing the articles. Cleaning up")

    #Get rid of all double linespaces and doublewhitespace
    for _ in [0,5]:
        all_articles = all_articles.replace("\n\n","\n")
        all_articles = all_articles.replace("  "," ")
         
    #Clear some variables because of memory issues
    del content, article, articles

    print("Starting to save file")

    with open(args.output_file, 'w+', encoding="utf-8") as f:
        f.write(all_articles)

    
    #Print some statistics
    print(f'Saved file: {args.output_file}')
    print(f'Total number of articles: {total_article_count}')
    print(f'Number of valid segments: {valid_segment_count}')
    
    #Split the file into lines - else we often run into memory issues
    all_articles_lines = all_articles.split("\n")
    del all_articles

    word_num = 0
    for l in all_articles_lines:
        word_line_num = len(l.split())
        word_num += word_line_num

    print(f'Number of words: {word_num}')

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_path', required=True, type=str, help='Input path')
    parser.add_argument('-o', '--output_file', required=True, type=str, help='Output file')
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
    args = parse_args()
    main(args)


