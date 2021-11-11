#!/bin/bash
if test $# -ne 4
then
echo "Usage:$0 <templatefile> <corpusname><nosplits><outputdir>"
exit
fi
templatefile=$1
corpusname=$2
nosplits=$3
outputdir=$4
cp ${templatefile} ${outputdir}/tmp.py
sed -i "s/<corpusname>/$corpusname/g" ${outputdir}/tmp.py
sed -i "s/<nosplits>/$nosplits/g" ${outputdir}/tmp.py
mv ${outputdir}/tmp.py ${outputdir}/${corpusname}.py