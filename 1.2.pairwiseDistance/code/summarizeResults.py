#!/usr/bin/env python

#takes output from popgenWindows.py and outputs relevant data
#in this case, all Fst values, in the following format:
# <pond 1>,<pond2>,<value>,<label>

import sys

inFile=sys.argv[1]
label=sys.argv[2]
outFile=sys.argv[3]

def summarizeData(inFile,label,outFile):
    i=open(inFile, "r")
    o=open(outFile, "w")
    infoDict={}
    for line in i:
        atts=line.split(",")
        for colNum,att in enumerate(atts):
            if colNum in infoDict.keys():
                infoDict[colNum].append(att.strip())
            else:
                infoDict[colNum]=[att,]
    for k in infoDict.keys():
        if "Fst" in infoDict[k][0]:
            nameParts=infoDict[k][0].split("_")
            pond1=nameParts[2]
            pond2=nameParts[4]
            o.write('''%s,%s,%f,%s\n''' % (pond1, pond2,float(infoDict[k][2]),label))
    o.close()

summarizeData(inFile,label,outFile)
