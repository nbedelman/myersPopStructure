import Bio
from Bio import Phylo
from io import StringIO
import sys


treeFile=sys.argv[1]
popFile=sys.argv[2]
percent=sys.argv[3]
outFile=sys.argv[4]


def evaluateMonophyly(treeFile,popFile, percent, outFile):
    p=open(popFile, "r")
    t=open(treeFile, "r")
    o=open(outFile, "w")
    highList=[]
    lowList=[]
    o.write('''chrom\tstart\tmaxLow\tmaxHigh\n''')
    for line in p:
        atts=line.split()
        if atts[1] == "low":
            lowList += [atts[0]+"_A", atts[0]+"_B"]
        elif atts[1] == "high":
            highList += [atts[0]+"_A", atts[0]+"_B"]
    for num, line in enumerate(t):
        if num % 1000 == 0:
            print(num)
        atts=line.split()
        chrom=atts[0]
        start=atts[1]
        newickString=atts[6]
        maxMono=findMaxMono(newickString,lowList,highList,percent)
        maxLow=maxMono[0]
        maxHigh=maxMono[1]
        o.write('''%s\t%s\t%f\t%f\n''' % (chrom, start, maxLow,maxHigh))
    p.close()
    t.close()
    o.close()



def findMaxMono(newickString, lowList, highList, percent):
    tree=Phylo.read(StringIO(newickString), "newick")
    lowCladeSizes=[]
    highCladeSizes=[]
    for clade in tree.get_nonterminals():
        subTree = tree.from_clade(clade)
        terminals = subTree.get_terminals()
        taxNames = [t.name for t in terminals]
        if sum([tax in lowList for tax in taxNames])/len(taxNames) > percent:
            lowCladeSizes.append(len(taxNames))
        if sum([tax in highList for tax in taxNames])/len(taxNames) > percent:
            highCladeSizes.append(len(taxNames))
    try:
        return(max(lowCladeSizes), max(highCladeSizes))
    except ValueError:
        return(0,0)

evaluateMonophyly(treeFile,popFile, percent, outFile)
