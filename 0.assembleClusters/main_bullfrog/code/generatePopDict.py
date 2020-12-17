#!/usr/bin/env python

import sys

inFile=sys.argv[1]

def makeDict(inFile):
    file=open(inFile,"r")
    outDict={}
    for line in file:
        atts=line.split()
        if atts[1] in outDict:
            outDict[atts[1]].append(atts[0]+"001.trim")
        else:
            outDict[atts[1]]=[atts[0]+"001.trim",]
    return outDict
