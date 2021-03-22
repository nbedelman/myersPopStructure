#!/bin/bash

#SBATCH -J computePopStats
#SBATCH -p day
#SBATCH -t 1-00:00
#SBATCH --mem=10000
#SBATCH -N 4
#SBATCH -c 25
#SBATCH -o outs/computePopStats.%j.out
#SBATCH -e errs/computePopStats.%j.err

homeDir=$1
genomeDir=$2
genofile=$3
genoOutDir=$4
popFilePrefix=$5
resultPrefix=$6
permutations=$7
windowSize=$8
summaryFile=$9

function pwait() {
    while [ $(jobs -p | wc -l) -ge $1 ]; do
        sleep 1
    done
}


echo running popgenWindows

stepSize=$(echo "$windowSize / 4" | bc)

popGenRun () {
    local i=$1
    echo iteration $i
  popString=$($homeDir/code/sampleGeno.py $genofile $popFilePrefix\_$i.pop.txt $genoOutDir/$(basename $popFilePrefix)\_$i.geno)
   python $genomeDir/popgenWindows.py -g $genoOutDir/$(basename $popFilePrefix)\_$i.geno -w $windowSize -s $stepSize -f phased -T 10 $popString -m 20 --writeFailedWindows -o $resultPrefix\_$i.stats

   if [ ! -f  $summaryFile.fst.raw ]
     then grep -v "scaffold" $resultPrefix\_$i.stats | awk 'BEGIN{FS=",";} {print $1"\t"$2"\t"$9}'  > $summaryFile.fst.raw
     grep -v "scaffold" $resultPrefix\_$i.stats | awk 'BEGIN{FS=",";} {print $1"\t"$2"\t"$8}'  > $summaryFile.dxy.raw
   else
     grep -v "scaffold" $resultPrefix\_$i.stats| awk 'BEGIN {FS=",";OFS="\t"} {print $9}' > $resultPrefix.thisFst.tmp
     paste $summaryFile.fst.raw $resultPrefix.thisFst.tmp > $resultPrefix.combinedFst.tmp && mv $resultPrefix.combinedFst.tmp $summaryFile.fst.raw
     grep -v "scaffold" $resultPrefix\_$i.stats| awk 'BEGIN {FS=",";OFS="\t"} {print $8}' > $resultPrefix.thisDxy.tmp
     paste $summaryFile.dxy.raw $resultPrefix.thisDxy.tmp > $resultPrefix.combinedDxy.tmp && mv $resultPrefix.combinedDxy.tmp $summaryFile.dxy.raw
   fi
 }

for i in $(seq 0 $permutations)
 do
 popGenRun $i &
 pwait 10
done

 wait

echo finished running all iterations

python $homeDir/code/summarizeWindowStats.py $summaryFile.fst.raw $summaryFile.fst.txt
python $homeDir/code/summarizeWindowStats.py $summaryFile.dxy.raw $summaryFile.dxy.txt
