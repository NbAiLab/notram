import sys, os, glob
from tqdm import tqdm

sys.path.append(r'../utils')
sys.path.append(r'../')

from utils.textCleaner import cleanTextBlock, cleanTextBlock_notram


text = "My email is per@capia.no\n"
print(text)

cleaned = cleanTextBlock_notram(text,do_lower_case=True) 
print(cleaned)

