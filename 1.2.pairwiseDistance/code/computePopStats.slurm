#!/bin/bash

#SBATCH -J computePopStats
#SBATCH -p day
#SBATCH -t 0-05:00
#SBATCH --mem=1000
#SBATCH -c 20
#SBATCH -o outs/computePopStats.%j.out
#SBATCH -e errs/computePopStats.%j.err

genomeDir=$1
genofile=$2
pseudoChromFile=$3
popfile=$4
popgenStats=$5


included="$(head -1 $genofile)"
popString=$(code/makePopList.py $popfile "$included")

#code/makePseudoChrom.py $genofile $pseudoChromFile

python $genomeDir/popgenWindows.py -g $pseudoChromFile $popString -o $popgenStats -f phased -w 500 -T 20
