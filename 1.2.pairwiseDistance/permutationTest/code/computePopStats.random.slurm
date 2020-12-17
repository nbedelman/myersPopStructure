#!/bin/bash

#SBATCH -J computePopStats
#SBATCH -p day
#SBATCH -t 0-01:00
#SBATCH --mem=5000
#SBATCH -c 20
#SBATCH -o outs/computePopStats.%j.out
#SBATCH -e errs/computePopStats.%j.err

genomeDir=$1
genofile=$2
popfile=$3
popgenStats=$4
label=$5
overallOut=$6

included="$(head -1 $genofile)"
popString=$(code/makePopList.random.py $popfile "$included" poplist.txt)

#code/makePseudoChrom.py $genofile $pseudoChromFile

python $genomeDir/popgenWindows.py -g $genofile -w 1000 -f phased -T 20 $popString -o $popgenStats
python code/summarizeResults.py $popgenStats $label $overallOut
