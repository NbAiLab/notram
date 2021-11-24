[<img align="right" width="150px" src="../images/nblogo.png">](https://ai.nb.no)
# Cleaning Rules
The **clean.py**-script is using configuration files to do the actual cleaning. We adjust these scrpts according to the sources. 


| Key  | Default | Description |
| :-------- |  :-----| :-----| 
|min_alphawords_paragraph |0 | Set a minimum number of words in a paragraph with only letters [a-Å]. Typically used in OCR text|
|min_length_article | 20 | Minimum number of characters in an article.|
|min_words_paragraph | 20 | Minimum number words in a paragraph.|
|max_word_length_paragraph | 1000 | Maximum word length in a paragraph. Typically used in OCR text where you somethimes get extremely long words. Might also be triggered by urls.|
|remove_control_characters | true | Removed control characters.|
| standardize_punctuation| true | Standardises the punctation.|
| replace_usernames_tweets| false | Replaces usernames in tweets, ie @twitteruser.|
| replace_urls| false | Replaces urls.|
|replace_email_addresses | false | replaces email addresses with placeholder.|
| fix_unicode| true | Fixes unicode errors. |
|normalise_unicode | true | Normalises the unicode. |
|min_ocr_date | 20090101 | Minimum ocr date. No effect if "assume_late_missing_dates" is true, and the value is not explicitely set.|
|min_publish_date | 18140517 | Minimum publish date. No effect if "assume_late_missing_dates" is true, and the value is not explicitely set.|
|min_document_word_confidence | 0.9 | Minimum average word confidence in a document. If this is not from an OCR source, the default value is set to 1.0.|
|min_confidence_paragraph | 0.9 |Minimum average word confidence in a paragraph. If this is not from an OCR source, the default value is set to 1.0. |
|remove_non_terminated_paragraphs | true | Headings usually does not have puntation marks at the end. This removes paragraphs without punctation at the end. |
|truncate_last_valid_sentence |true |In many books it is hard to concatenate pages. This means some sentences is broken in half. This removes the last sentence. |
| minimise_jsonl|true | Minimises the size of the json-file, ie removes meta-data that is not necessary later. |
| assume_late_missing_dates| true| Assyme that any missing dates (for instance ocr_date) is late, meaning today.|
| drop_paragraphs_with_encoding_errors|true | Drop all paragraphs with encoding errors. |
| drop_paragraphs_with_curly_brackets|true | Drop paragraphs with curly {brackets}. This effectively removes javascript from a lot of web documents.|


## Overview of Config-files
The following config-files are used when training NCC. These files are located [here](../corpus_generation_scripts/config/).

<details>
  <summary>config.json</summary>
  
```json
  {
	"min_alphawords_paragraph": 0,
	"min_length_article": 20,
	"min_words_paragraph": 0,
	"max_word_length_paragraph":1000,
	"remove_control_characters": true,
	"standardize_punctuation": true,
	"replace_usernames_tweets": false,
	"replace_urls": false,
	"replace_email_addresses": false,
	"fix_unicode":true,
	"normalise_unicode": true,
	"min_ocr_date": "20090101",
	"min_publish_date": "18140517",
	"min_document_word_confidence": 0.9,
	"min_confidence_paragraph": 0.9,
	"remove_non_terminated_paragraphs": true,
	"truncate_last_valid_sentence": true,
	"minimise_jsonl": true,
	"assume_late_missing_dates": true,
	"drop_paragraphs_with_encoding_errors": true,
	"drop_paragraphs_with_curly_brackets": true
}	
 ```
  
  </details>
  
  
<details>
  <summary>config_ocr.json</summary>
  
```json   
{
	"min_alphawords_paragraph": 2,
	"min_length_article": 20,
	"min_words_paragraph": 2,
	"max_word_length_paragraph":25,
	"remove_control_characters": true,
	"standardize_punctuation": true,
	"replace_usernames_tweets": false,
	"replace_urls": false,
	"replace_email_addresses": false,
	"fix_unicode":true,
	"normalise_unicode": true,
	"min_ocr_date": "20090101",
	"min_publish_date": "18140517",
	"min_document_word_confidence": 0.9,
	"min_confidence_paragraph": 0.9,
	"remove_non_terminated_paragraphs": true,
	"truncate_last_valid_sentence": true,
	"minimise_jsonl": true,
	"assume_late_missing_dates": true,
	"drop_paragraphs_with_encoding_errors": false,
	"drop_paragraphs_with_curly_brackets": false

}	
 ```
  
  </details>
  
  
<details>
  <summary>config_twitter.json</summary>
  
```json
{
	"min_alphawords_paragraph": 0,
	"min_length_article": 10,
	"min_words_paragraph": 0,
	"max_word_length_paragraph":1000,
	"remove_control_characters": true,
	"standardize_punctuation": true,
	"replace_usernames_tweets": true,
	"replace_urls": true,
	"replace_email_addresses": true,
	"fix_unicode":true,
	"normalise_unicode": true,
	"min_ocr_date": "20090101",
	"min_publish_date": "18140517",
	"min_document_word_confidence": 0.9,
	"min_confidence_paragraph": 0.9,
	"remove_non_terminated_paragraphs": false,
	"truncate_last_valid_sentence": false,
	"minimise_jsonl": true,
	"assume_late_missing_dates": true,
	"drop_paragraphs_with_encoding_errors": false,
	"drop_paragraphs_with_curly_brackets": false
}	
 ```
  
  </details>
