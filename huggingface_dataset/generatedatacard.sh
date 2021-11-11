#!/bin/bash
if test $# -ne 5
then
echo "Usage:$0 <templatefile> <corpusname><nosplits><languages><outputdir>"
exit
fi
templatefile=$1
corpusname=$2
nosplits=$3
languages=$4
outputdir=$5
cp ${templatefile} ${outputdir}/tmp.md
sed -i "s/<corpusname>/$corpusname/g"  ${outputdir}/tmp.md
sed -i "s/<nosplits>/$nosplits/g"  ${outputdir}/tmp.md
sed -i "s/<languages>/$languages/g"  ${outputdir}/tmp.md
mindato=`date +"%Y%m%d %H:%M"`
sed -i "s/<builddate>/$mindato/g"  ${outputdir}/tmp.md
mv  ${outputdir}/tmp.md  ${outputdir}/README.md