#!/bin/bash

#trying a permutation test to see if pattern of Fst could be explained by sorting a panmictic population into groups.

#######################
###SETUP ENVIRONMENT###
#######################

mkdir -p data
mkdir -p errs
mkdir -p outs
mkdir -p results

ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/Analysis/old_ipy_analysis/YMF_main/popfile.txt data/
ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/filtered_vcfs/filter_SNPs/YMFmain.subset.0.50_0.50.vcf data/
ln -s /gpfs/loomis/project/skelly/nbe4/myersPopStructure/1.2.pairwiseDistance/geno/YMFmain.subset.0.50_0.50.pseudoChrom.geno data/

module load miniconda
conda activate ipyrad

######################
###DEFINE VARIABLES###
######################

genomeDir=/home/nbe4/project/software/genomics_general/
popfile=data/popfile.txt
genofile=data/YMFmain.subset.0.50_0.50.pseudoChrom.geno

homeDir=$PWD

overallOut=results/permutationResults.csv

numPermutations=100
###RUN CODE###

#analyze the true dataset
mkdir realData
cd realData
mkdir errs
mkdir outs
mkdir code
cp $homeDir/code/* code/
label=realData
popgenOutput=$label.stats

sbatch code/computePopStats.slurm $genomeDir $homeDir/$genofile $homeDir/$popfile $popgenOutput $label $homeDir/$overallOut

cd ..
#then, make permutations
for i in  $(seq $numPermutations)
do
  mkdir perm_$i
  cd perm_$i
  mkdir errs
  mkdir outs
  mkdir code
  cp $homeDir/code/* code
  label=perm_$i
  popgenOutput=$label.stats

  sbatch code/computePopStats.random.slurm $genomeDir $homeDir/$genofile $homeDir/$popfile $popgenOutput $label $homeDir/$overallOut
  cd ..
done
