#!/bin/bash


PRE_IFS=$IFS
IFS=


a={for i in `ls -al /bin`; do
    echo $i | awk '{print $5,$9}'
done}

vi file.sh

$a>>{file}.sh

IFS=$PRE_IFS
