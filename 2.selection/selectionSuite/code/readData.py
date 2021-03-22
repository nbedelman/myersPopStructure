#take a tsv with sample infor, and sort them into population classes
import sys

class Individual:
    #at the moment, each individual can only have a sample name, pond,  coverage, Age, accession
    def __init__(self,attList):
        self.sampleName=attList[0]
        self.sampleID=attList[1]
        self.pond=attList[2]
        self.coverage=attList[3]
        self.age=attList[4]
        self.accession=attList[5]
    def getSampleName(self):
        return self.sampleName
    def getSampleID(self):
        return self.sampleID
    def getPond(self):
        return self.pond
    def getCoverage(self):
        return self.coverage
    def getAge(self):
        return self.getAge
    def getAccession(self):
        return self.getAccession


class Population:
    #populations have individuals, canopy, depth, temp, area, population size, extinction probability, 2017_count
    def __init__(self,pondName,indList,attsList):
        self.pond=pondName
        self.individuals=[Individual(ind) for ind in indList]
        self.canopy=attsList[0]
        self.depth=attsList[1]
        self.temp=attsList[2]
        self.area=attsList[3]
        self.popSize=attsList[4]
        self.extinction=attsList[5]
    def getPondName:
        return self.pond
    def getIndividuals:
        return self.individuals
    def getCanopy:
        return self.canopy
    def getDepth:
        return self.depth
    def getTemp:
        return self.temp
    def getArea:
        return self.area
    def getPopSize:
        return self.popSize
    def getExtinctionProb:
        return self.extinction




sampleFile=sys.argv[1]
pondDict={}
s=open(sampleFile, "r")
s.readline()
for line in sampleFile:
    atts.split(line)
    pondName=atts[2]
    if pondName in pondDict.keys():
        pondDict[pondName][0].append(atts[0:6])
    else:
        pondDict[pondName]=[[atts[0:6]],atts[6:]]
