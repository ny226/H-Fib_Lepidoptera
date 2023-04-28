#!/bin/bash

ref=$1
termini="../termini/${ref}.fasta"

#the environment hfibroin should contain bioconda blast. Once you create the environment, run this code "conda install -c bioconda blast"

while read f; do
	sbatch annotation.sh $f 
done <"found_alt_phegnom.txt"

