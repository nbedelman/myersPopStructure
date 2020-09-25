#!/bin/bash

#going to compute some of the stats that were done for McCartney-Melstad et al 2017

mkdir stats


#first, make a file with all vcf files

for i in *.json
do run=$(basename $i .json);
echo $run
#get the vcf file and add to list
vcfFile=$PWD/$run\_outfiles/*.vcf ;
echo $vcfFile >> stats/allVCFs.txt;
#then, get number of paralagous clusters, loci,heteozygous sites, heterozygosity
#paralagous clusters filtered by maxH (?)
awk -v run=$run 'BEGIN{OFS="\t";} {print $1,$2,$3,$4,$5,$6,$7,$8,$9,run}' $run\_consens/s5_consens_stats.txt |tail -n +2 >> stats/locusStats.txt;
done

#correlate pairwise divergence with missingness
vcfMissingness.pl --vcfList=stats/allVCFs.txt


while read line
do
  inPrefix=${line%.*}_missHM012
  genotypes=$inPrefix.012
  individuals=$inPrefix.012.indv
  out=$inPrefix.missingness
  perl ~/project/software/clustOpt/resources/pairwiseMissingnessFrom012.pl --genotypes $genotypes --individuals $individuals --out $out
done < stats/allVCFs.txt
