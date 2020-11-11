#!/bin/bash
if test $# -ne 1
then
echo "Usage:$0 <dir with paper>"
exit
fi


echo ${line}
#AVIS=`echo ${line} | cut -d"/" -f 8`
#DATO=`echo ${line} | cut -d"/" -f 10| cut -d"_" -f 4`

AVIS="NN"
DATO="DD"

echo ${AVIS}:${DATO}
LDIR="./tmp2"
if [ ! -d ${LDIR} ] 
then
mkdir -p ${LDIR}
fi
RELFILENAME="NN"

python3 metsParser.py ./tmp ${LDIR}
#rm /home/tensor/extractAvisArtikler/tmp/*
#exit
