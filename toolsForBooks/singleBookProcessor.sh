#!/bin/bash
localfile=`echo $1 |tr -d "'"`
#echo "${localfile}">>/home/freddy/tools/aa.txt 
/usr/bin/python3 /home/freddy/tools/singleBookProcessor.py ${localfile}

