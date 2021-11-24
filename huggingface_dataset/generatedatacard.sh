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
nosplitszeropadded=`printf %04d $3`
cp ${templatefile} ${outputdir}/tmp.md
sed -i "s/<corpusname>/$corpusname/g"  ${outputdir}/tmp.md
sed -i "s/<nosplits>/$nosplits/g"  ${outputdir}/tmp.md
sed -i "s/<nosplitszeropadded>/$nosplitszeropadded/g"  ${outputdir}/tmp.md
sed -i "s/<languages>/$languages/g"  ${outputdir}/tmp.md
mindato=`date +"%d%m%Y"`
sed -i "s/<builddate>/$mindato/g"  ${outputdir}/tmp.md

foo=$(< ${outputdir}/stats.md)
desc=$(< ${outputdir}/description.md)
license=$(< ${outputdir}/license.md)
>${outputdir}/tmp2.md
while read line
do
if [[ ${line} == "<stats>" ]]
then
printf '%s\n' "$foo" >>  ${outputdir}/tmp2.md

elif [[ ${line} == "<filelist>" ]]
then
for f in `ls -1 ${outputdir}/data`
do
fibasename=`echo $f |rev|cut -d "/" -f 1 | rev | cut -d "." -f 1`
echo "* [${fibasename}](https://huggingface.co/datasets/NbAiLab/${corpusname}/resolve/main/data/${fibasename}.json.gz)" >>  ${outputdir}/tmp2.md
done
elif [[ ${line} == "<description>" ]]
then
  printf '%s\n' "$desc" >>  ${outputdir}/tmp2.md
elif [[ ${line} == "<license>" ]]
then
  printf '%s\n' "$license" >>  ${outputdir}/tmp2.md
else
  printf '%s\n' "$line" >>   ${outputdir}/tmp2.md
fi


done<${outputdir}/tmp.md
mv  ${outputdir}/tmp2.md  ${outputdir}/README.md
rm ${outputdir}/tmp.md