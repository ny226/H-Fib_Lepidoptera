#!/bin/bash

#SBATCH --time=24:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4G   # memory per CPU core
#SBATCH -J "augustus"   # job name
#SBATCH --mail-user=naomi.j.young@gmail.com   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE




ref=$1
termini="../termini/${ref}.fasta"
file=$2 #gene names
#the environment hfibroin should contain bioconda blast. Once you create the environment, run this code "conda install -c bioconda blast"

source ~/.bashrc
conda activate hfibroin
while read f; do
	genome="../genomes/${f}.fna"
	tblastn -db $genome -query $termini -out ../b_results/${f}.out -outfmt 7
	cat ../b_results/${f}.out
done <$file
