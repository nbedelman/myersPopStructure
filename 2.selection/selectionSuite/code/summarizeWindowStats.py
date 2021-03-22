#!/usr/bin/env python

import numpy as np
import sys

statsConcat=sys.argv[1]
summaryOut=sys.argv[2]

def computeSummaryStats(statsConcat, summaryOut):
    i=open(statsConcat,"r")
    o=open(summaryOut, "w")
    for line in i:
        atts = line.strip().split()
        try:
            chrom=atts[0]
            pos=atts[1]
            values=[]
            for val in atts[2:]:
                try:
                    values.append(float(val))
                except ValueError:
                    pass
            npVals=np.array(values)
            validVals=np.count_nonzero(~np.isnan(values))
            o.write('''%s\t%s\t%f\t%f\t%i\n''' % (chrom,pos,np.nanmean(npVals),np.nanstd(npVals),validVals))
        except IndexError:
            pass
    o.close()
    i.close()

computeSummaryStats(statsConcat,summaryOut)
