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

species=$1
gene="${species}_gene.fa"
output="${species}.gff"

source ~/.bashrc
#conda activate augustus
conda activate maker

export AUGUSTUS_CONFIG_PATH=~/anaconda3/envs/augustus/config/
augustus --strand=both --singlestrand=true \
--extrinsicCfgFile=./extrinsic.cfg \
--alternatives-from-evidence=true \
--gff3=on \
--uniqueGeneId=true \
--UTR=off \
--species=fly \
../genes/$gene > \
../annotation/$output

