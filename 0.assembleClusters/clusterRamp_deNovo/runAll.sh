#! /bin/bash

#use Andis's trimmed rad-seq reads to generate and cluster RAD loci

#########################
### setup environment ###
#########################

#load modules
module load miniconda/4.8.3
conda activate ipyrad
module load OpenMPI
module load VCFtools/0.1.15-foss-2018a-Perl-5.26.1

#link data
mkdir -p data
ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/processed/trimmed/YMF_pilot/ data/
ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/Analysis/ipyrad/YMF_main/popfile.txt data/

chmod u+x code/*

########################
### define variables ###
########################

assemblyName=myersPopGen_clusterRamp_deNovo

#steps 1 and 2
fastqDir=data/YMF_pilot/*.fastq
#popFile=data/popfile.txt #this requires more info! figure it out, then include for step 7.
datatype=ddrad
restriction_overhang=GATC,TGCA
filter_min_trim_len=50
max_indels_locus=5
output_formats='*'
maxdepth=100

#steps 3-7
clust_threshold=$(echo 0.90 0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99)
max_shared_Hs_locus=$(echo .01 .02)

################
### Run Code ###
################

#first, generate ipyrad project

ipyrad -n $assemblyName #this generates parameter file called params-$assemblyName.txt

#then, change the lines for steps 1 and 2
sed -i "s:^.*sorted_fastq:$fastqDir\t## :" params-$assemblyName.txt
sed -i "s:^.*datatype:$datatype\t## :" params-$assemblyName.txt
sed -i "s:^.*restriction_overhang:$restriction_overhang\t## :" params-$assemblyName.txt
sed -i "s:^.*filter_min_trim_len:$filter_min_trim_len\t## :" params-$assemblyName.txt
sed -i "s:^.*max_indels_locus:$max_indels_locus\t## :" params-$assemblyName.txt
sed -i "s:^.*output_formats:"$output_formats"\t## :" params-$assemblyName.txt

#the, run steps 1 and 2.
sbatch code/runipyrad.slurm params-$assemblyName.txt 12

####################
### RESTART HERE ###
####################


for j in $clust_threshold
  do for k in $max_shared_Hs_locus
    do
    name=$assemblyName\_$j\_$k
    newBranch=${name//./}
    ipyrad -p params-$assemblyName.txt -b $newBranch
    sed -i "s:^.*clust_threshold:$j\t## :" params-$newBranch.txt
    sed -i "s:^.*max_shared_Hs_locus:$k\t## :" params-$newBranch.txt
    sed -i "s:^.*project_dir:$PWD\t## :" params-$newBranch.txt
    sed -i "s:^.*maxdepth:$maxdepth\t## :" params-$newBranch.txt
    sbatch code/runipyrad.slurm params-$newBranch.txt 34567
  done
done
