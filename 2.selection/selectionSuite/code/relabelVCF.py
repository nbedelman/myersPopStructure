#!/usr/bin/env python

import sys

vcfIn=sys.argv[1]
vcfOut=sys.argv[2]

def relabelLine(line):
    atts=line.split()
    outString='''%s\t%s\t%s\t%s\n''' % (atts[0],atts[1],atts[1],"\t".join(atts[3:]))
    return(outString)

def relabelVCF(vcfIn,vcfOut):
    i=open(vcfIn, "r")
    o=open(vcfOut,"w")
    for line in i:
        if line.startswith("chr"):
            o.write(relabelLine(line))
        else:
            o.write(line)

relabelVCF(vcfIn,vcfOut)
