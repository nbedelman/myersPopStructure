#!/usr/bin/env python

#take a pop file; make a list.

import sys

inFile=sys.argv[1]
includeList=sys.argv[2]


def makePopString(popFile, includeList):
    '''takes a file with 2 columns - fist a smple and second the population. Returns a string of -p popName1 ind1,ind2... -p popname2 ind3,ind4...'''
    popDict={}
    f=open(inFile, "r")
    for line in f:
        atts=line.split()
        if atts[0]+"001.trim" in includeList:
          if atts[1] in popDict.keys():
              popDict[atts[1]].append(atts[0]+"001.trim")
          else:
              popDict[atts[1]]=[atts[0]+"001.trim",]
    outString=''
    for k in popDict.keys():
        outString=outString+'''-p %s %s ''' % (k, ",".join(popDict[k]))
    return outString

includeList=includeList.split()
print(makePopString(inFile, includeList))
