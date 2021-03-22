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
popFilePrefix=$4
resultPrefix=$5
permutations=$6
windowSize=$7

for i in $(seq $permutations)
 do
 included="$(head -1 $genofile)"
 popString=$($homeDir/code/makePopList.py $popFilePrefix\_$i.pop.txt "$included")

#code/makePseudoChrom.py $genofile $pseudoChromFile

python $genomeDir/popgenWindows.py -g $genofile -w $windowSize -f phased -T 20 $popString -o $resultPrefix\_$i.stats

grep -v "#" $resultPrefix\_$i.stats >> results/$(basename $resultPrefix).allPermutations.stats
done
