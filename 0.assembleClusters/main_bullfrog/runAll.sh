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
mkdir -p errs
mkdir -p outs
mkdir -p data
ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/processed/trimmed/YMF_main/ data/
ln -s /gpfs/loomis/project/skelly/aa2258/2019_RASY_YMF_PopGen/Analysis/ipyrad/YMF_main/popfile.txt data/

chmod u+x code/*

########################
### define variables ###
########################

assemblyName=myersPopGen_bullfrog

#steps 1 and 2
fastqDir=data/YMF_main/*.fastq
reference_sequence=data/GCA_002284835.2_RCv2.1_genomic.fna
#downloaded 9/23/20 from https://ftp.ncbi.nlm.nih.gov/genomes/genbank/vertebrate_other/Lithobates_catesbeianus/latest_assembly_versions/GCA_002284835.2_RCv2.1/
assembly_method=reference
#popFile=data/popfile.txt #this requires more info! figure it out, then include for step 7.
datatype=ddrad
restriction_overhang=GATC,TGCA
filter_min_trim_len=50
max_indels_locus=5
output_formats='*'


################
### Run Code ###
################

#first, generate ipyrad project

ipyrad -n $assemblyName #this generates parameter file called params-$assemblyName.txt

#then, change the lines for steps 1 and 2
sed -i "s:^.*sorted_fastq:$fastqDir\t## :" params-$assemblyName.txt
sed -i "s:^.*reference_sequence:$reference_sequence\t## :" params-$assemblyName.txt
sed -i "s:^.*assembly_method:$assembly_method\t## :" params-$assemblyName.txt
sed -i "s:^.*datatype:$datatype\t## :" params-$assemblyName.txt
sed -i "s:^.*restriction_overhang:$restriction_overhang\t## :" params-$assemblyName.txt
sed -i "s:^.*filter_min_trim_len:$filter_min_trim_len\t## :" params-$assemblyName.txt
sed -i "s:^.*max_indels_locus:$max_indels_locus\t## :" params-$assemblyName.txt
sed -i "s:^.*output_formats:"$output_formats"\t## :" params-$assemblyName.txt

#the, run steps 1 and 2.
sbatch code/runipyrad.slurm params-$assemblyName.txt 1234567
