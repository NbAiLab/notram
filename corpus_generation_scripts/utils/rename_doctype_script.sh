for f in *cc100*; do python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file $f --existing_doctype_value cc100_no --new_doctype_value cc100;done&
for f in open_books*; do python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file $f --existing_doctype_value book --new_doctype_value books;done&
for f in restricted_books*; do python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file $f --existing_doctype_value book --new_doctype_value books;done&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_parliamentary_collections_no.jsonl --existing_doctype_value Digistorting --new_doctype_value parliament&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_public_reports_no.jsonl --existing_doctype_value publicreport --new_doctype_value publicreports&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_subtitles_no.jsonl --existing_doctype_value opensubtitles --new_doctype_value subtitles&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_wikipedia_nb.jsonl --existing_doctype_value wikipedia_download_nb --new_doctype_value wikipedia_nb&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_wikipedia_nn.jsonl --existing_doctype_value wikipedia_download_nn --new_doctype_value wikipedia_nn&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_newspapers_online_nb.jsonl --existing_doctype_value newspapers_online --new_doctype_value newspapers_online_nb&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_newspapers_online_nn.jsonl --existing_doctype_value newspapers_online --new_doctype_value newspapers_online_nn&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_government_nb.jsonl --existing_doctype_value government --new_doctype_value government_nb&
python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py --corpus_input_file open_government_nn.jsonl --existing_doctype_value government --new_doctype_value government_nn&

