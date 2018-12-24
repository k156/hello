#!/bin/bash


if [ $# -lt 2 ]; then
    echo "Input the filename, please.."
    echo "usage) ./s5.sh <to-change-file>"
    exit 0
fi

DATE=`date +%Y%m%d--date=yesterday`

FN="${DATE}.log"
#echo "mv $1 $FN"

cat $1>File
cat $2>>File

mv File $FN
