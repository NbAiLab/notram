import csv
import pandas as pd
import glob
import os
from urllib.parse import urlparse

files = glob.glob('/mnt/lv_ai_1_ficino/sprakbanken_test_output/*.*')
input_file = "/mnt/lv_ai_1_ficino/pdf_warcinfo.csv"
df = pd.read_csv(input_file, encoding='utf-8', dtype='string')


for f in files:
    hash = os.path.basename(f).replace(".txt","")
    item = df[df.content_hash == hash].iloc[0]
    domain = urlparse(item['target_uri']).netloc
    name, ext = domain.split('.')[-2:]
    doc_type = "maalfrid_"+name
    print(doc_type)


