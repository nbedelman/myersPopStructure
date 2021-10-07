#!/bin/bash

mkdir -p data
mkdir -p errs
mkdir -p outs
mkdir -p geno
mkdir -p results

ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/Analysis/old_ipy_analysis/YMF_main/popfile.txt data
ln -s /home/nbe4/scratch60/1.3.pca/plink/RASY_ragtag/autosomes/data/RASY_ragtag.myers.autosome.filter.vcf data
ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/filtered_vcfs/filter_SNPs/YMFmain.subset.0.50_0.50.vcf data

module load miniconda

conda activate ipyrad
###DEFINE VARIABLES###
genomeDir=/home/nbe4/project/software/genomics_general/
popfile=data/popfile.txt
vcfFile=data/RASY_ragtag.myers.autosome.filter.vcf
genofile=geno/RASY_ragtag.myers.autosome.filter.geno
popgenStats=results/RASY_ragtag.myers.autosome.filter.vcf.stats

###RUN CODE###
#first, convert vcf to geno
python $genomeDir/VCF_processing/parseVCF.py -i $vcfFile -o $genofile
genomeDir=/home/nbe4//project/software/genomics_general/
popfile=data/popfile.txt
vcfFile=data/YMFmain.subset.0.50_0.50.vcf
genofile=geno/YMFmain.subset.0.50_0.50.geno
popgenStats=results/YMFmain.subset.0.50_0.50.stats

###RUN CODE###
#first, convert vcf to geno
python $genomeDir/VCF_processing/parseVCF.py -i $vcfFile -o $genofile

#then, get popgen stats
sbatch code/computePopStats.slurm $genomeDir $genofile $popfile $popgenStats
