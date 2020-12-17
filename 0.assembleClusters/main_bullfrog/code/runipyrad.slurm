#!/bin/bash

#SBATCH -J assembleRadSeq
#SBATCH -p day
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --mem-per-cpu=10G
##SBATCH --exclusive
#SBATCH --time=10:00:00
#SBATCH -e errs/assembleRadSeq.%j.err
#SBATCH -o outs/assembleRadSeq.%j.out

module load miniconda/4.8.3
conda activate ipyrad

paramFile=$1
steps=$2

ipyrad -p $paramFile -d -s $steps
