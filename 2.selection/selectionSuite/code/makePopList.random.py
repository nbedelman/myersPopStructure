#!/usr/bin/env python

#take a pop file; make a list.

import sys
import random

inFile=sys.argv[1]
includeList=sys.argv[2]
outFile=sys.argv[3]


def makeRandomPopString(popFile, includeList, outFile):
    '''takes a file with 2 columns - fist a smple and second the population.
    Returns a string of -p popName1 ind1,ind2... -p popname2 ind3,ind4...
    the number of pops, their names, and the number of individuals for each pop will be the same, but their
    members will be randomly drawn'''
    popDict={}
    f=open(inFile, "r")
    o=open(outFile,"w")
    popList=[]
    for line in f:
        atts=line.split()
        if atts[0] in includeList:
            popList.append(atts[0])
            if atts[1] in popDict.keys():
                popDict[atts[1]].append(atts[0])
            else:
                popDict[atts[1]]=[atts[0],]
    outString=''

    random.shuffle(popList)

    firstIndex=0
    for k in popDict.keys():
        numInds=len(popDict[k])
        thisPop=popList[firstIndex:firstIndex+numInds]
        firstIndex=firstIndex+numInds
        outString=outString+'''-p %s %s ''' % (k, ",".join(thisPop))
        for pop in thisPop:
            o.write('''%s\t%s\n''' % (pop,k))
    o.close()
    return outString

includeList=includeList.split()
print(makeRandomPopString(inFile, includeList, outFile))
