
vcfIn=$1
popList=$2
maxMissingLocus=$3
vcfOut=$4



vcftools --vcf $vcfIn --keep $popList --min-alleles 2 --max-alleles 2 --mac 3 --max-missing 0.1 --recode --out ./$(basename $vcfIn .vcf).tmp

mv ./$(basename $vcfIn .vcf).tmp.recode.vcf $vcfOut
