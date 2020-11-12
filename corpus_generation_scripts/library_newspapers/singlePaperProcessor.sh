#!/bin/bash
localfile=`echo $1 |tr -d "'"`
#echo "${localfile}">>aa.txt
outputmaster="/disk4/folder1/nancy/content/text/newspaper/nonpdf/text"
python /home/tensor/notram/toolsForNewspapers/metsParser.py ${localfile} ${outputmaster}

