#!/usr/bin/env python3
import argparse
import os
import jsonlines
from tqdm import tqdm
import json
import pprint
import pandas as pd
#pd.options.display.float_format = '{:,}'.format
#pd.options.display.float_format = '${:,.2f}'.format

def main(args):

    with jsonlines.open(args.input_file) as reader:
        doc_type = {}
        doc_type_lines = {}
        lang_fasttext = {}
        lang_fasttext_lines = {}
        publish_year = {}
        publish_year_lines = {}


        for n, line in tqdm(enumerate(reader)):
            num_words = len(line['text'].split())
            doc_type[line['doc_type']] = doc_type.get(line['doc_type'], 0) + num_words
            doc_type_lines[line['doc_type']] = doc_type_lines.get(line['doc_type'], 0) + 1
            lang_fasttext[line['lang_fasttext']] = lang_fasttext.get(line['lang_fasttext'], 0) + num_words
            lang_fasttext_lines[line['lang_fasttext']] = lang_fasttext_lines.get(line['lang_fasttext'], 0) + 1
            year = line['publish_year']
            if year == 2099:
                year = 2021
            publish_year[year] = publish_year.get(year, 0) + num_words
            publish_year_lines[year] = publish_year_lines.get(year, 0) + 1
    
    #Do sone reasonable sorting
    publish_year = list(publish_year.items())
    publish_year_lines= list(publish_year_lines.items())
    doc_type = sorted(doc_type.items(), key=lambda x: x[1], reverse=True)
    doc_type_lines = sorted(doc_type_lines.items(), key=lambda x: x[1], reverse=True)
    lang_fasttext = sorted(lang_fasttext.items(), key=lambda x: x[1], reverse=True)
    lang_fasttext_lines = sorted(lang_fasttext_lines.items(), key=lambda x: x[1], reverse=True)
    
    all_json=[doc_type,doc_type_lines,lang_fasttext,lang_fasttext_lines,publish_year,publish_year_lines]
   
    # Report Document Types
    df_doc = pd.DataFrame.from_dict(doc_type)
    df_doc.columns = ['Source','Words']
    df_doc_length = pd.DataFrame.from_dict(doc_type_lines)
    df_doc_length.columns = ['Source','Documents']
    df_doc_all  = pd.merge(df_doc, df_doc_length, on='Source')
    df_doc_all['Words/Document'] = (df_doc_all['Words']/df_doc_all['Documents']).astype(int)
    
    # Report Language
    df_lang_fasttext = pd.DataFrame.from_dict(lang_fasttext)
    df_lang_fasttext.columns = ['Language','Words']
    df_lang_fasttext_length = pd.DataFrame.from_dict(lang_fasttext_lines)
    df_lang_fasttext_length.columns = ['Language','Documents']
    df_lang_all  = pd.merge(df_lang_fasttext, df_lang_fasttext_length, on='Language')
    df_lang_all['Words/Document'] = (df_lang_all['Words']/df_lang_all['Documents']).astype(int)

    
    # Report Publish Year
    df_publish_year = pd.DataFrame.from_dict(publish_year)
    df_publish_year.columns = ['Year','Words']
    df_publish_year_length = pd.DataFrame.from_dict(publish_year_lines)
    df_publish_year_length.columns = ['Year','Documents']
    df_year_all  = pd.merge(df_publish_year, df_publish_year_length, on='Year')
    df_year_all['Words/Document'] = (df_year_all['Words']/df_year_all['Documents']).astype(int)
    #sort
    df_year_all = df_year_all.sort_values(by=['Year'], ascending=False).reset_index(drop=True)

    #group by decade
    df_decade_all = df_year_all.groupby((df_year_all['Year']//10)*10).sum()
    df_decade_all = df_decade_all.drop(['Year'], axis=1)
    df_decade_all['Decade'] = df_decade_all.index
    df_decade_all = df_decade_all.sort_values(by=['Decade'], ascending=False).reset_index(drop=True)
    df_decade_all = df_decade_all[['Decade', 'Words', 'Documents', 'Words/Document']]
   
    #Format all columns correctly
    df_doc_all['Words'] = df_doc_all['Words'].apply(lambda x:'{:,}'.format(x))    
    df_doc_all['Documents'] = df_doc_all['Documents'].apply(lambda x:'{:,}'.format(x))    
    df_doc_all['Words/Document'] = df_doc_all['Words/Document'].apply(lambda x:'{:,}'.format(x))    
    df_lang_all['Words'] = df_lang_all['Words'].apply(lambda x:'{:,}'.format(x))    
    df_lang_all['Documents'] = df_lang_all['Documents'].apply(lambda x:'{:,}'.format(x))    
    df_lang_all['Words/Document'] = df_lang_all['Words/Document'].apply(lambda x:'{:,}'.format(x))    
    df_decade_all['Words'] = df_decade_all['Words'].apply(lambda x:'{:,}'.format(x))    
    df_decade_all['Documents'] = df_decade_all['Documents'].apply(lambda x:'{:,}'.format(x))    
    df_decade_all['Words/Document'] = df_decade_all['Words/Document'].apply(lambda x:'{:,}'.format(x))    

    

    output = "## Statistics\n"
    output += "### Document Types\n"+df_doc_all.to_markdown(index=False).replace("|:--","|---").replace("---|","--:|")+"\n\n"
    output += "### Languages\n"+df_lang_all.to_markdown(index=False).replace("|:--","|---").replace("---|","--:|")+"\n\n"
    output += "### Publish Periode\n"+df_decade_all.to_markdown(index=False).replace("|:--","|---").replace("---|","--:|")+"\n\n"
    
    file = open(args.output_file, 'w')
    file.write(output)
    file.close()
    
    print(f"Markdown file is written to {args.output_file}")

def parse_args():
    # Parse commandline
    parser = argparse.ArgumentParser(
        description="Convert the WEB64 Facebook corpus to jsonl. This corpus is in json format. Output is a jsonl  UTF-8 file with one post per line")
    parser.add_argument('--output_file', required=True,
                        help='Output file name. Will overwrite it exists')
    parser.add_argument('--input_file', required=True,
                        help='Input file. Will read all files in folder')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
