#!/bin/bash

#SBATCH -J computeWindowTrees
#SBATCH -p day
#SBATCH -t 1-00:00
#SBATCH --mem=10000
#SBATCH -N 2
#SBATCH -c 25
#SBATCH -o outs/computeWindowTrees.%j.out
#SBATCH -e errs/computeWindowTrees.%j.err


homeDir=$1
genomeDir=$2
genoFile=$3
popFile=$4
resultPrefix=$5
indList=$6

export PYTHONPATH=$PYTHONPATH:$genomeDir

stepSize=$(echo "$windowSize / 4" | bc)

#first, calculate trees in windows
python $genomeDir/phylo/phyml_sliding_windows.py -w 5000000 -S 1000000 -g $genoFile -p $resultPrefix --bootstraps 1000 -T 50 --indFile $indList -M 30

gunzip $resultPrefix.trees.gz > results/$(basename $resultPrefix).trees

python $homeDir/code/evaluateMonophyly.py results/$(basename $resultPrefix).trees $popFile .9 results/$(basename $resultPrefix).monophyly.txt
