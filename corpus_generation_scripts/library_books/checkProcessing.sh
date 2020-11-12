#!/bin/bash
if test $# -ne 1 
then
echo "Usage:$0 "
exit
fi

for i in `find $1 -name '*.jpg'`
do






echo  "$i"
mogrify -set comment 'Image rewritten with ImageMagick' $i 
done
