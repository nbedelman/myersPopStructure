#!/bin/bash

#run structure analysis

#######################
###SETUP ENVIRONMENT###
#######################

module load miniconda
conda activate faststructure
module load GSL/2.5-iccifort-2018.3.222-GCC-7.3.0-2.30

mkdir -p errs
mkdir -p outs
mkdir -p data
ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/Analysis/YMF_main/PCA data

#######################
###DEFINE VARIABLES####
#######################

k=$(echo 3 4 5 6 7 8)
input=data/PCA/PCA_YMFmain_filt_minsamp026

###############
###RUN CODE####
###############

for i in $k
do echo $i
outDir=$(basename $input)_$i\_output
mkdir $outDir
output=$outDir/$(basename $input)_$i
sbatch code/runFastStructure.slurm $input $output $i
done
