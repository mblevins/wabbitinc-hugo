#!/bin/bash
echo $1
b=`basename $1 .md`
d=`dirname $1`
cd $d
python3 /Users/mblevins/Documents/wabbitinc/wabbitinc-hugo/caption.py < ${b}.mdx > ${b}.md
