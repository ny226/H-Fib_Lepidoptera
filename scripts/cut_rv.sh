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

first=$1
genome="../genomes/${first}.fna"

coors=$2
inter="${first}_cut.out"
out="${first}_rv.out"


./seqtk/seqtk subseq $genome $coors > $inter;
./seqtk/seqtk seq -r $inter > $out;
