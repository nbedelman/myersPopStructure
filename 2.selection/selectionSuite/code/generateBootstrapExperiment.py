import sys
import classDefinitions as cd

sampleFile=sys.argv[1]
trait=sys.argv[2]
prefix=sys.argv[3]
permutations=int(sys.argv[4])
quantiles=int(sys.argv[5])
bootstraps=int(sys.argv[6])
try:
    breakpoint=float(sys.argv[7])
except IndexError:
    breakpoint=None
# sampleFile="/Users/nbedelman/Desktop/sampleData.allPonds.combined.tsv"
# trait="canopy"
# prefix="trialBootstrap"
# permutations= 10
# quantiles= 4
# bootstraps= 1


pondDict={}
s=open(sampleFile, "r")
s.readline()
for line in s:
    atts=line.split("\t")
    pondName = atts[2]
    if pondName in pondDict.keys():
        pondDict[pondName][0].append(atts[0:6])
    else:
        pondDict[pondName] = [[atts[0:6]], atts[6:]]

pondList = []
for pond in pondDict.keys():
    pondList.append(cd.Population(pond, pondDict[pond][0], pondDict[pond][1]))

myers=cd.Metapopulation(pondList)

myers.generateBootstrapExperiment(trait,prefix,permutations,quantiles=quantiles, bootstraps=bootstraps,breakpoint=breakpoint)
