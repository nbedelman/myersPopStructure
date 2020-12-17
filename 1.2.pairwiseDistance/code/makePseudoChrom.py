#!/usr/bin/env python

#pretend each rad is on the same chromosome so that we can calculate averages.
#**IMPORTANT: these will be in windows, but really its a RANDOM SUBSET of SNPs

import sys

genoFile=sys.argv[1]
outfile=sys.argv[2]

def makeOneChrom(genoFile, outfile):
    g=open(genoFile, "r")
    o=open(outfile, "w")
    for lineNum, line in enumerate(g):
        if "#" in line: #write the header
            o.write(line)
        else:
            atts=line.split()
            o.write('''%s\t%i\t%s\n''' % ("pseudochrom_1", lineNum, "\t".join(atts[2:])))

makeOneChrom(genoFile,outfile)
