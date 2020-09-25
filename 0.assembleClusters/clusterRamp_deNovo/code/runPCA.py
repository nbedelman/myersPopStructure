#!/usr/bin/env python

import sys
import ipyrad.analysis as ipa
import pandas as pd
import toyplot

snpFile=sys.argv[1]
popFile=sys.argv[2]

def makeDict(inFile):
    file=open(inFile,"r")
    outDict={}
    for line in file:
        atts=line.split()
        if atts[1] in outDict:
            outDict[atts[1]].append(atts[0])
        else:
            outDict[atts[1]]=[atts[0],]
    return outDict

data=snpFile

imap=makeDict(popFile)

pca = ipa.pca(
    data=data,
    imap=imap,
    mincov=0.75,
    impute_method="sample",
)
