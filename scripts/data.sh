#!/bin/bash

#ref=$1
#termini="../termini/${ref}.fasta"
species=$1
genome="../genomes/${species}.fna"

#source ~/.bashrc
#the environment hfibroin should contain bioconda blast. Once you create the environment, run this code "conda install -c bioconda blast"
#conda activate hfibroin



makeblastdb -dbtype nucl -in $genome -title ../genomes/
#tblastn -db $genome -query $termini -out ../b_results/${species}.out -outfmt 7

#cat ../b_results/${species}.out

#python3 file_edit.py $species
#python3 gene_ext.py $ref $species

#[[ -f ../genes/${species}_gene.fa ]] || echo There is no gene file;  exit 1;

#conda deactivate

#sbatch annotation.sh $species
#squeue -u ny226
