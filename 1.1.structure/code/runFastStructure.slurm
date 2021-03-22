#!/bin/bash
#SBATCH -J fastStructure
#SBATCH -p day
#SBATCH -N 1 -n 1
#SBATCH  --mem=10000
#SBATCH -t 0-05:00
#SBATCH -o outs/fastStructure_%j.out
#SBATCH -e errs//fastStructure_%j.err

input=$1
output=$2
k=$3


python /home/nbe4/project/software/fastStructure/structure.py --format=str -K $k --input $input --output $output

python /home/nbe4/project/software/fastStructure/distruct.py -K $k --input=$output --output=$output.$k.plot
