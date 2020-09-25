#!/bin/bash

#SBATCH -J assembleRadSeq
#SBATCH -p day
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 1
#SBATCH --cpus-per-task 32
#SBATCH --exclusive
#SBATCH --mem-per-cpu=4G
#SBATCH --time=12:00:00
#SBATCH -e errs/assembleRadSeq.%j.err
#SBATCH -o outs/assembleRadSeq.%j.out


paramFile=$1
steps=$2

ipyrad -p $paramFile -s $steps -c 20
