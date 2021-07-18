# Balanced Norwegian Bokmål and Norwegian Nynorsk Corpus
This is a balanced Nynorsk-Bokmål corpus created as part of the JAX/Flax + 🤗 Community Week for doing machine translations between the two language variants. The corpus has the same amount of data from both languages, and could also be used for other NLP tasks.

The balancing is done both across the language variants and across media types. 

Fasttext 0.9.2 is used for language detection including anything with a probability above 0.5 for each of the variants. 

Since the Bokmål corpus is significantly larger, a shuffled sub corpora for Bokmål is trimmed to approximately match the Nynorsk sub corpora. The final corpus is shuffled. All the text is collected from the Collossal Norwegian Corpus v2. Virtually all Nynorsk text in this collection is used.


## Composition of the 19GB Balanced Corpus
| Sub Corpus   |   Bokmål  | Nynorsk   | 
| -------- |   :-----|  :-----| 
| Library Books | 3.9| 3.9 |
| Library Newspapers | 3.5| 3.5 |
| Web Crawl| 1.3| 1.3 |
| Administration | 0.4| 0.4 |
| Social | 0.3| 0.3 |
| Wikipedia | 0.2| 0.2 |
| **Total**| **9.5**| **9.5**| 

