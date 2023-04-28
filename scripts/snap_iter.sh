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


file=$1 # file with all the genome names I want to run against the reference

while read f; do
	echo $f;
	input="${f}_gene.fa"
	./SNAP/snap ./SNAP/HMM/B.mori.hmm ../genes/$input > ../snap_anno/"${f}_snap.gff";
done <$file

