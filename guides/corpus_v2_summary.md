# Corpus v2
This page tracks summarizes the Norwegian Collossal Corpus v2. All sizes in GB. 1GB of uncompressed text is roughly 160M words. 

## Norwegian
| General Sources  |   Gb | | Web Harvested  |   Gb | 
| -------- |   :-----|  | | -------- |   :-----| 
| Library Books | 83.0| | | CC-100 | 52.0| 
| Library Newspapers | 63.0| | | OSCAR | 6.8|
| Wikipedia | 1.6|| | MC4 | ?80?|
| Open Subtitles | 0.6| | | |
| Norart | 0.4| | | |
| **Total Unique General**| **149**| | **Total Unique Web**| **80**|



 





| Sosial Media  |   Gb | 
| -------- |   :-----|  
| Facebook | ?| 
| Reddit | 0.3|
| Twitter News | ?|
| Twitter Top | ?|
| **Total Unique Web**| **40**??|

| Administrative sources  |   Gb | 
| -------- |   :-----|  
| Government Collection | 0.2|
| Parliament Collection | 8.4|
| Public Reports | 0.6|
| Lovdata CD | 0.5|
| Lovdata Transfer | 2.8|
| Målfrid | 13.0|
| **Total Unique Admin**| **20**|

**Total Norwegian text: 289Gb??**


## Swedish
| Sources  |   Gb | 
| -------- |   :-----|  
| Library books/newspapers | 0.5| 
| Reddit | 1.6| 
| MC4 | 150|
| **Total Swedish**| **150Gb**|

## Danish
| Sources  |   Gb | 
| -------- |   :-----|
| Library books/newspapers | 1.0| 
| Reddit | 1.1| 
| MC4 | 60|
| **Total Danish**| **60Gb**|

## Icelandic
| Sources  |   Gb | 
| -------- |   :-----|  
| Reddit | 0.1| 
| MC4 | 8|
| **Total Icelandic**| **8Gb**|

## English
| Sources  |   Gb | 
| -------- |   :-----| 
| Library books/newspapers | 5.0| 
| Wikipedia | 23|
| Reddit | 520| 
| CC-100 | 376|
| MC4 | Lots|
| **Total English**| **>1Tb**|



# Composition of Training Corpus for NoTraM Large
Norwegian model but with added Swedish/Danish and English text. Swedish and Danish is added mainly for support since the languages are very similar, and it is expexted that this will strenghten the Norwegian capabilities. English is also a simililar language, however there are mainly two reasons for adding quite a lot of English text here:
* Most Norwegians speak English, and it is expected that English should be understood. There are also a lot of English words in use and it is likely that new words in the future will come from Nowegian. We expect this to strengthen the Norwegian model.
* This amount of English will also make it a decent English model. It will make evaluating the model easier. We can for instance evaluate the model directly of Glue/SuperGlue. We can also train it directly on large non-translated dataset, like SQuAD and MNLI, and then expect it to have decent Norwegian capabilities in solving similar tasks.

| Sources  |   % available | Gb | 
| -------- |   :-----| :-----| 
| Norwegian General | 100% | 149| 
| Norwegian Web | 70% | 100| 
| Norwegian Social Media | 100% | 40| 
| Norwegian Admin | 100% | 20|
| **Norwegian Total** |  | **250GB**|
| Swedish | 30% | 50|
| Danish | 80% | 50|
| English | <10% | 150|
| **Total Corpus**| **500GB**|

