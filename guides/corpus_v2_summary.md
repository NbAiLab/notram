# Corpus v2 Summary and NoTram Large
This page summarizes the Norwegian Collossal Corpus v2. All sizes in GB. 1GB of uncompressed text is roughly 160M words. Not all numbers are ready yet.

## Norwegian
| General   |   GB | Web   |   GB | Social Media  |   GB | Administrative  |   GB | 
| -------- |   :-----|  -------- |   :-----| -------- |   :-----|  -------- |   :-----|  
| Library Books | 83.0| CC-100 | 52.0| Facebook | 6.5| Government Docs | 0.2|
| Library Newspapers | 63.0| OSCAR | 6.8|Reddit | 0.3|Parliament Docs | 8.4|
| Wikipedia | 2.0| MC4 | 100.0| Twitter News | 0.8|Public Reports | 0.6|
| Open Subtitles | 0.6| | | Twitter Top | 14.0|Lovdata CD | 0.5|
| Norart | 0.4| | | VG Debatt| 15.0|Lovdata Transfer | 2.8|
| Online Newspapers|5.0| || | |Målfrid | 13.0|
| **Total Unique General**| **150GB**| **Total Unique Web**| **100GB**| **Total Unique Social**| **25GB**|**Total Unique Admin**| **20GB**|
| **Total Unique Norwegian Estimate** | **289GB??**| | | | | |

 
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
NoTraM Large is primarily a Norwegian model but with added Swedish, Danish and English text. Swedish and Danish is added mainly for support since the languages are very similar, and it is expexted that this will strenghten the Norwegian capabilities. English is also a simililar language, however there are mainly two reasons for adding a significant amountof English text to the training corpus:
* Most Norwegians speak English. There are also a lot of English in use, especially in social media, and it is likely that new words in the future will come from Nowegian. A good understanding of English is therefore necessary for a model used to understand the Norwegian language.
* This amount of English will also make it a decent English model. It will make evaluating the model easier. We can for instance evaluate the model directly of Glue/SuperGlue. We can also train it directly on large non-translated dataset, like SQuAD and MNLI, and then expect it to have decent Norwegian capabilities in solving similar tasks.

| Sources  |   % available | Gb | 
| -------- |   :-----| :-----| 
| Norwegian General | 100% | 150| 
| Norwegian Web | 70% | 70| 
| Norwegian Social Media | 100% | 40| 
| Norwegian Admin | 100% | 20|
| **Norwegian Total** |  | **250GB**|
| Swedish | 30% | 50|
| Danish | 80% | 50|
| English | <10% | 150|
| **Total Corpus**| | **500GB**|

