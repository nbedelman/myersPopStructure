#!/bin/bash

#SBATCH -J computePopStats
#SBATCH -p day
#SBATCH -t 0-01:00
#SBATCH --mem=5000
#SBATCH -c 20
#SBATCH -o outs/computePopStats.%j.out
#SBATCH -e errs/computePopStats.%j.err

homeDir=$1
genomeDir=$2
genofile=$3
popfile=$4
popgenStats=$5
windowSize=$6

included="$(head -1 $genofile)"
popString=$($homeDir/code/makePopList.py $popfile "$included")

#code/makePseudoChrom.py $genofile $pseudoChromFile

python $genomeDir/popgenWindows.py -g $genofile -w $windowSize -f phased -T 20 $popString -o $popgenStats
