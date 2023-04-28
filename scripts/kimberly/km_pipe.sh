#!/bin/bash

ref=sys.argv[1]
termini="../termini/${ref}.fasta"
species=sys.argv[2]
genome="../genomes/${species}.fna"

source ~/.bashrc
conda activate hfibroin

#python3 file_edit.py $species

makeblastdb -in $genome -dbtype nucl -title "Title"
tblastn -db $genome -query $termini -out ../b_results/${species}.out -outfmt 7

#python3 gene_ext.py $ref $species

#[[ -f ../genes/${species}_gene.fa ]] || echo There is no gene file;  exit 1;

#conda deactivate

#sbatch annotation.sh $species
#squeue -u ny226
