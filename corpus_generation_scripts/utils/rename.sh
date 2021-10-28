change="python /home/perk/notram/corpus_generation_scripts/utils/change_doctype_value.py"

for f in *cc100*; do $change --corpus_input_file $f --existing_doctype_value cc100_no --new_doctype_value cc100;done
for f in open_books*; do $change --corpus_input_file $f --existing_doctype_value book --new_doctype_value books;done
for f in restricted_books*; do $change --corpus_input_file $f --existing_doctype_value book --new_doctype_value books;done
for f in open_newspapers*; do $change --corpus_input_file $f --existing_doctype_value newspapers_ocr --new_doctype_value newspapers_ocr;done
for f in open_newspapers*; do $change --corpus_input_file $f --existing_doctype_value newspapers_pdf --new_doctype_value newspapers_pdf;done
for f in restricted_newspapers*; do $change --corpus_input_file $f --existing_doctype_value newspapers_ocr --new_doctype_value newspapers_restricted_ocr;done
for f in restricted_newspapers*; do $change --corpus_input_file $f --existing_doctype_value newspapers_pdf --new_doctype_value newspapers_restricted_pdf;done


$change --corpus_input_file open_parliamentary_collections_no.jsonl --existing_doctype_value Digistorting --new_doctype_value parliament
$change --corpus_input_file open_public_reports_no.jsonl --existing_doctype_value publicreport --new_doctype_value publicreports
$change --corpus_input_file open_subtitles_no.jsonl --existing_doctype_value opensubtitles --new_doctype_value subtitles
$change --corpus_input_file open_wikipedia_nb.jsonl --existing_doctype_value open_wikipedia_download_nb --new_doctype_value open_wikipedia_nb
$change --corpus_input_file open_wikipedia_nn.jsonl --existing_doctype_value open_wikipedia_download_nn --new_doctype_value open_wikipedia_nn
$change --corpus_input_file open_newspapers_online_nb.jsonl --existing_doctype_value newspapers_online --new_doctype_value newspapers_online_nb
$change --corpus_input_file open_newspapers_online_nn.jsonl --existing_doctype_value newspapers_online --new_doctype_value newspapers_online_nn
$change --corpus_input_file open_government_nb.jsonl --existing_doctype_value government --new_doctype_value government_nb
$change --corpus_input_file open_government_nn.jsonl --existing_doctype_value government --new_doctype_value government_nn

