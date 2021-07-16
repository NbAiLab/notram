# Corpus v2 Summary and NoTram Large
This page summarizes the Norwegian Collossal Corpus v2. All sizes in GB. 1GB of uncompressed text is roughly 160M words. Not all numbers are ready yet.

## Norwegian
| General   |   GB | Web   |   GB | Social Media  |   GB | Administrative  |   GB | 
| -------- |   :-----|  -------- |   :-----| -------- |   :-----|  -------- |   :-----|  
| Library Books | 60.0| CC-100 | 24.0| Facebook | 3.9| Government Docs | 0.1|
| Library Newspapers | 50.0| OSCAR | 0.5|Reddit | 0.2|Parliament Docs | 8.1|
| Wikipedia | 1.6| MC4 | 68.0| Twitter News | 0.3|Public Reports | 0.5|
| Open Subtitles | 0.2| | | Twitter Top | 5.9|Lovdata CD | 0.3|
| Norart | 0.2| | | VG Debatt| 15.0|Lovdata Transfer | 1.6|
| Online Newspapers|5.0| || | |Målfrid | 11.0|
| **Total Unique General**| **117GB**| **Total Unique Web**| **93GB**| **Total Unique Social**| **25GB**|**Total Unique Admin**| **22GB**|
| **Total Unique Norwegian** | **256GB**| | | | | |

 
## Other Languages
| Sources  |  Swedish GB | Danish GB | English  GB | 
| -------- |   :-----|   :-----|:-----| 
| Library books/newspapers | 0.5|  1.0|  5.0| 
| Reddit | 1.6|  1.1| 520.0|
| Wikipedia | 3.9|  0.8| 23.0|
| CC-100 | 98.0| 58.0| 376.0|
| MC4 | 150.0| 60.0| >1TB|
| **Total Unique Estimate**| **150GB**| **60Gb**|**>1TB**|


# Composition of Training Corpus for NoTraM Large
NoTraM Large is primarily a Norwegian model but with added high quality Swedish, Danish and English text. For these languages we have added the entire Wikipedia, then added 1 GB of social media text (Reddit) and in the end added web crawled data until the target (15GB for Swedish/Danish and 40GB for English). The total training corpus is 300GB.

Swedish and Danish is added mainly for support since the languages are very similar, and it is expexted that this will strenghten the Norwegian capabilities. English is also a simililar language, however there are some additional reasons for adding English text to the training corpus:
* Most Norwegians speak English. There are also a lot of English in use, especially in social media, and it is likely that new words in the future will come from Nowegian. A good understanding of English is therefore necessary for a model used to understand the Norwegian language.
* This amount of English will also make it a decent English model. It will make evaluating the model easier. We can for instance evaluate the model directly of Glue/SuperGlue. We can also train it directly on large non-translated dataset, like SQuAD and MNLI, and then expect it to have decent Norwegian capabilities in solving similar tasks.

| Sources  |   % available | Gb | 
| -------- |   :-----| :-----| 
| Norwegian General | 100% | 117| 
| Norwegian Web | 70% | 77| 
| Norwegian Social Media | 100% | 25| 
| Norwegian Admin | 100% | 22|
| **Norwegian Total** |  | **230GB**|
| Swedish | - | 15|
| Danish | - | 15|
| English | - | 40|
| **Total Corpus**| | **300GB**|

