# Balanced Norweigan Bokmål amd Norwegian Nynorsk Corpus
This is a balanced Nynorsk-Bokmål corpus created specifically for doing machine translations or other NLP tasks requiring balancing between the two language variants. The corpus has the same amount of data from both languages

The balancing is done both across the language variants. In addition we have tried to make sure that we have gotten about the same amount of data from each source. The corpus is randomized. 

Fasttext 0.9.2 is used for language detection including anything with a probability above 0.5 for each of the variants. 

Since the Bokmål corpus is significantly larger, a shuffled sub corpora for Bokmål is trimmed to approximately match the Nynorsk sub corpora. The final corpus is shuffled. All the text is collected from the Collossal Norwegian Corpus v2. The goal has been to extract as much Nynorsk text as possible from this collection.


## Corpus in GB
| Sub Corpus   |   Bokmål  | Nynorsk   | 
| -------- |   :-----|  :-----| 
| Library Books | 3.9| 3.9 |
| Library Newspapers | 3.5| 3.5 |
| Web Crawl| 0.4| 0.4 |
| Administration | 0.4| 0.4 |
| Social | 0.3| 0.3 |
| Wikipedia | 0.2| 0.2 |
| **Total**| **?GB**| **?**| 

