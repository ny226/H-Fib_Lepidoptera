#!/bin/bash

#the environment hfibroin should contain bioconda blast. Once you create the environment, run this code "conda install -c bioconda blast"

while read f; do
	perl ./augustus/scripts/getAnnoFasta.pl $f 
done <"all.txt"
