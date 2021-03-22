#!/usr/bin/env python

import sys

genoFile=sys.argv[1]
popFile=sys.argv[2]
genoOut=sys.argv[3]


def makePopString(popFile):
    p=open(popFile,"r")
    numHigh=0
    numLow=0
    for line in p:
        atts=line.strip().split()
        if atts[1] == "low":
            numLow += 1
        elif atts[1] == "high":
            numHigh += 1
    popString='''-p high %s -p low %s''' % (",".join(["high"+str(num) for num in range(numHigh)]),
    ",".join(["low"+str(num) for num in range(numLow)]))
    print(popString)
    p.close()

def makeGenoFile(genoFile,popFile,genoOut):
    i=open(genoFile,"r")
    p=open(popFile, "r")
    o=open(genoOut, "w")
    highInds = []
    lowInds = []
    for line in p:
        atts=line.strip().split()
        if atts[1]=="high":
            highInds.append(atts[0])
        elif atts[1]=="low":
            lowInds.append(atts[0])

    originalHead=i.readline().strip().split()
    highIndices=[originalHead.index(h) for h in highInds]
    lowIndices=[originalHead.index(l) for l in lowInds]

    header = '''#CHROM\tPOS\t%s\t%s\n''' % ("\t".join(["high"+str(num) for num in range(len(highInds))]),
    "\t".join(["low"+str(num) for num in range(len(lowInds))]))
    o.write(header)
    for line in i:
        atts=line.strip().split()
        o.write('''%s\t%s\t%s\t%s\n''' % (atts[0],atts[1],"\t".join([atts[highInd] for highInd in highIndices]),"\t".join([atts[lowInd] for lowInd in lowIndices])))
    o.close()


makeGenoFile(genoFile,popFile,genoOut)
makePopString(popFile)
