#!/usr/bin/env python

#get total number of reads from each locus of vcf. not surei f there's a better way

import sys
import pandas as pd

vcfIn=sys.argv[1]
tableOut=sys.argv[2]

class Site:
    def __init__(self,line, sampleNames):
        atts=line.split()
        self.locus=atts[0]
        self.site=int(atts[1])
        self.name=atts[2]
        self.ref=atts[3]
        self.alt=atts[4]
        self.score=atts[5]
        self.p=(atts[6]=="PASS")
        self.numInds=atts[7].split("=")[1].split(";")[0]
        self.depth=atts[7].split("=")[2].strip()
        self.sampleDict={}
        for record in range(9,len(atts)):
            GT=atts[record].split(":")[0]
            DP=int(atts[record].split(":")[1])
            C=int(atts[record].split(":")[2].split(",")[0])
            A=int(atts[record].split(":")[2].split(",")[1])
            T=int(atts[record].split(":")[2].split(",")[2])
            G=int(atts[record].split(":")[2].split(",")[3].strip())
            self.sampleDict[sampleNames[record-9]]=[GT,DP,C,A,T,G]

    def getSiteDepth(self):
        depthList=[self.locus,]+[self.sampleDict[k][1] for k in self.sampleDict.keys()]
        return (depthList)

def perSiteDepth(vcfFile):
    inVCF=open(vcfFile,"r")
    output=[]
    for num,line in enumerate(inVCF):
        if line.startswith("##"):
            pass
        elif line.startswith("#CHROM"):
            sampleNames=[i for i in line.split()[9:]]
        else:
            thisSite=Site(line,sampleNames)
            output.append(thisSite.getSiteDepth())
        if num%10000==0:
            print(num)
    return(output,sampleNames)

depthLists=perSiteDepth(vcfIn)
my_df=pd.DataFrame(depthLists)
my_df.to_csv(tableOut, index=False, header=["locus",]+sampleNames)
