#with this code, I will assess selection through a variety of approaches.
#1. Fst in windows
#2. allele frequency difference
#3. bayescan
#4. phylogeny
#I will use 4 individuals per pond. I'm not sure if I should use all ponds or only the most extreme in terms of variable of interest.

###SETUP ENVIRONMENT###

mkdir -p data
mkdir -p errs
mkdir -p outs

module load miniconda
conda activate selection
module load VCFtools
module load PLINK/2.00-alpha2.3

#link original vcf file
ln -s /home/nbe4/scratch60/0.assembleClusters/RASY_ragTag/RASY_ragtag_outfiles/RASY_ragtag.vcf data

###DEFINE VARIABLES###
genomeDir=/home/nbe4/project/software/genomics_general/

trait=canopy
permutations=100
bootstraps=100
quantile=4
windowSize=1000000
maxMissing=0.5
breakpoint=50
prefix=RASY_ragtag_bootstrap_$trait\_bp$breakpoint\_w$windowSize
#prefix=RASY_ragtag_bootstrap_$trait\_bp$breakpoint\_w$windowSize

homeDir=$PWD
sampleFile=$homeDir/data/sampleData.allPonds.combined.noDup.noLow.tsv
vcfFile=$homeDir/data/RASY_ragtag.vcf
###RUN CODE###
#first, generate directory, enter, set up
mkdir $prefix
cd $prefix
mkdir data
mkdir results
mkdir geno
mkdir results/permutations
mkdir results/bootstraps
mkdir permGeno
mkdir bootGeno
mkdir errs
mkdir outs
mkdir trees
permutationPopFiles=data/$prefix\_permutations
permutationPrefix=data/$prefix\_permutations/$prefix\_permutation
permutationGenoDir=./permGeno
bootstrapPopFiles=data/$prefix\_bootstraps
bootstrapPrefix=data/$prefix\_bootstraps/$prefix\_bootstrap
bootstrapGenoDir=./bootGeno
indList=data/$prefix.inds.txt
filterVCF=data/$prefix.filter.VCF
genoFile=geno/$prefix.filter.geno
traitPopFile=data/$prefix.category.pop.txt
traitPlinkFile=data/$prefix.category.plink.pop.txt
bayescanPopFile=data/$prefix.bayescan.pop.txt
bayescanSNPfile=data/$prefix.bayescan.snp.txt
permutationResultPrefix=results/permutations/$prefix.filter
bootstrapResultPrefix=results/bootstraps/$prefix.filter
permutationSummary=results/$prefix.permutation.summary
boostrapSummary=results/$prefix.bootstrap.summary
treeOut=trees/$prefix


#generate experiment files
python $homeDir/code/generateBootstrapExperiment.py $sampleFile $trait data/$prefix $permutations $quantile $bootstraps $breakpoint

#filter VCF
$homeDir/code/subsetAndFilterVCF.sh $vcfFile $indList $maxMissing $filterVCF

#convert to geno file
python $genomeDir/VCF_processing/parseVCF.py -i $filterVCF -o $genoFile

#run popgen windows
sbatch $homeDir/code/computePopStats.boot.slurm $homeDir $genomeDir $genoFile $bootstrapGenoDir $bootstrapPrefix $bootstrapResultPrefix $bootstraps $windowSize $boostrapSummary

sbatch $homeDir/code/computePopStats.boot.slurm $homeDir $genomeDir $genoFile $permutationGenoDir $permutationPrefix $permutationResultPrefix $permutations $windowSize $permutationSummary

plink2 --vcf $filterVCF --freq --pheno $traitPlinkFile --loop-cats population --allow-extra-chr --out results/$prefix

sbatch $homeDir/code/runBayescan.slurm $homeDir $bayescanPopFile $filterVCF $bayescanSNPfile

sbatch $homeDir/code/computeWindowTrees.slurm $homeDir $genomeDir $genoFile $traitPopFile $treeOut $indList
