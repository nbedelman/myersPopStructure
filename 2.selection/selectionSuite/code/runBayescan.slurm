#!/bin/bash

#SBATCH -J runBayescan
#SBATCH -p week
#SBATCH -t 3-00:00
#SBATCH --mem=10000
#SBATCH -c 30
#SBATCH -o outs/runBayescan.%j.out
#SBATCH -e errs/runBayescan.%j.err

homeDir=$1
popFile=$2
vcfFile=$3
bayescanFile=$4

mkdir -p results

grep -v "#" $vcfFile |awk '{print $1"\t"$2}' > results/$(basename $bayescanFile).positions.txt

perl $homeDir/code/vcf2bayescan.pl -p $popFile -v $vcfFile

mv bayescan.txt $bayescanFile

bayescan_2.1 $bayescanFile -o results/$(basename $bayescanFile).out
