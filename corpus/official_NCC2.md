## Composition of Norwegian Colossal Corpus v2
This corpus is the official corpus used for training the NB models. It consists of the majority of available text, but the amount from MC4 is decreased because it is slighly repetive and of lower quality.

The corpus has also a slight about of high quality Swedish, Danish and English text. For these languages we have added the entire Wikipedia for each of the languages, then added Reddit (1.0GB/0.5GB/1.5GB) and finally web text until we reached the target of 15GB for each of the languages. The total training corpus is 250GB.

Swedish and Danish is added mainly for support since the languages are very similar, and it is expexted that this will strenghten the Norwegian capabilities. English is also a simililar language, there are also a lot of English in use, especially in social media, and it is likely that new words in the future will come from Nowegian. A good understanding of English is therefore necessary for a model used to understand the Norwegian language.

| Sources  |   % available | Gb | 
| -------- |   :-----| :-----| 
| Norwegian General | 100% | 117| 
| Norwegian Web | 50% | 44| 
| Norwegian Social Media | 100% | 25| 
| Norwegian Beurocratic | 100% | 22|
| **Norwegian Total** |  | **205GB**|
| Swedish | - | 15|
| Danish | - | 15|
| English | - | 15|
| **Total Corpus**| | **250GB**|

