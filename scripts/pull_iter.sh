#!/bin/bash

#SBATCH --time=4:00:00   # walltime
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
file=$2
#source ~/.bashrc
#conda activate hfibroin
#pip install pyfaidx

while read f; do
	echo $f;
	python3 gene_ext.py $ref $f;
done <$file
