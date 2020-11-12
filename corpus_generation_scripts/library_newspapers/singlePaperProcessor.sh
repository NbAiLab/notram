#!/bin/bash
localfile=`echo $1 |tr -d "'"`
#echo "${localfile}">>aa.txt
outputmaster="/disk4/folder1/nancy/content/text/newspaper/nonpdf/text"
python /home/tensor/notram/corpus_generation_scripts/library_newspapers/metsParser.py ${localfile} ${outputmaster}

