#!/bin/bash
if test $# -ne 2
then
echo "Usage:$0 <infile><outfile>"
exit
fi
> $2
while read line
do
out=`echo ${line} | sed -e "s/^/'/g" | sed -e "s/$/'/g"`
echo "Inp: ${line} Out: ${out}"
echo ${out} >> $2
done<$1