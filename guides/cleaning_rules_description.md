[<img align="right" width="150px" src="../images/nblogo.png">](https://ai.nb.no)
# Cleaning Rules
The **clean.py**-script is using configuration files to do the actual cleaning. We adjust these scrpts according to the sources. 


| Key  | Default | Description |
| :-------- |  :-----| :-----| 
|min_alphawords_paragraph |0 | Set a minimum number of words in a paragraph with only letters [a-Å]. Typically used in OCR text|
|min_length_article | 20 | Minimum number of characters in an article.|
|min_words_paragraph | 20 | Minimum number words in a paragraph.|
|max_word_length_paragraph | 1000 | Maximum word length in a paragraph. Typically used in OCR text where you somethimes get extremely long words. Might also be triggered by urls.|
|remove_control_characters | true | |
| standardize_punctuation| true | |
| replace_usernames_tweets| false | |
| replace_urls| false | |
|replace_email_addresses | false | |
| fix_unicode| true | |
|normalise_unicode | true | |
|min_ocr_date | 20090101 | |
|min_publish_date | 18140517 | |
|min_document_word_confidence | 0.9 | |
|min_confidence_paragraph | 0.9 | |
|remove_non_terminated_paragraphs | true | |
|truncate_last_valid_sentence |true | |
| minimise_jsonl|true | |
| assume_late_missing_dates| true| |
| drop_paragraphs_with_encoding_errors|true | |
| drop_paragraphs_with_curly_brackets|true | |
