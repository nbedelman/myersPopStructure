# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import statistics
import random
import os

class Individual:
    # at the moment, each individual can only have a sample name, pond,  coverage, Age, accession
    def __init__(self, attList):
        self.sampleName = attList[0]
        self.sampleID = attList[1]
        self.pond = attList[2]
        self.coverage = int(attList[3])
        self.age = attList[4]
        self.accession = attList[5]

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

    def lowCov(self):
        return self.getCoverage() < 20000

class Population:
    # populations have individuals, canopy, depth, temp, area, population size, extinction probability, 2017_count
    def __init__(self, pondName, indList, attsList):
        self.pond = pondName
        self.individuals = [Individual(ind) for ind in indList]
        self.pondAttributes={
            "canopy" : attsList[0],
            "depth" : attsList[1],
            "temp" : attsList[2],
            "area" : attsList[3],
            "popSize" : attsList[4],
            "extinction" : attsList[5].strip()
        }

    def getPondName(self):
        return self.pond

    def getIndividuals(self):
        return self.individuals

    def getPondStat(self, stat):
        pondStat = self.pondAttributes[stat]
        return pondStat

    def getHighestCov(self, n=0):
        '''return the n highest coverage individuals
        if no n is specified, return all individuals'''
        sortedList = sorted(self.getIndividuals(), key=lambda x: x.getCoverage())
        if n == 0:
            return sortedList
        else:
            return sortedList[:n]

class Metapopulation():
    def __init__(self, popList):
        self.popList=popList

    def getPopulationList(self):
        return self.popList

    def generateBootstrapExperiment(self,variable,prefix,permutations=100, quantiles=2, bootstraps=100, breakpoint=None):
        ''' print bootstrap and permutation population files to test for selection based on variable.
        also generates a file with maximum, minimum, and variance of the variable by pond.
        values for variable must be "canopy", "depth", "temp", "area", or "extinction" '''
        viablePonds=self.getViablePonds(variable)

        pondDict = self.makePondDict(variable, viablePonds, quantiles, breakpoint=breakpoint)

        self.generateIndListFile(pondDict, prefix)
        self.generatePondPopFile(pondDict, prefix + ".ponds.plink", header="#IID\tpopulation\n")
        self.generateTraitPopFile(pondDict, prefix + ".category.plink", header="#IID\tpopulation\n")
        self.generateTraitPopFile(pondDict, prefix + ".category", header="")
        self.generateBayescanPopFile(pondDict, prefix)
        self.generateTraitStats(pondDict, variable, quantiles, prefix, 0)
        self.makeBootstraps(bootstraps, pondDict, prefix)
        self.makeBootstrapPermutations(permutations, pondDict, prefix)

    def makeBootstrapPermutations(self,permutations,pondDict,prefix):
        for perm in range(permutations):
            try:
                os.makedirs('''%s_permutations/''' % (prefix))
            except FileExistsError:
                pass
            filePrefix='''%s_permutations/%s_permutation_%i''' % (prefix,os.path.basename(prefix),perm)
            self.generateRandomBootstrapPopFile(pondDict, filePrefix)

    def makeBootstraps(self, bootstraps, pondDict, prefix):
        for boot in range(bootstraps):
            try:
                os.makedirs('''%s_bootstraps/''' % (prefix))
            except FileExistsError:
                pass
            filePrefix='''%s_bootstraps/%s_bootstrap_%i''' % (prefix,os.path.basename(prefix),boot)
            self.generateBootstrapPopFile(pondDict, filePrefix)

    def generateBootstrapPopFile(self, pondDict, filePrefix):
        lowPonds=[p for p in pondDict.keys() if pondDict[p][1] == "low"]
        highPonds=[p for p in pondDict.keys() if pondDict[p][1] == "high"]
        lowPondInds = 0
        highPondInds = 0
        for pond in lowPonds:
            lowPondInds+=len(pondDict[pond][0])
        for pond in highPonds:
            highPondInds+=len(pondDict[pond][0])

        lowInds = []
        highInds = []
        for k in pondDict.keys():
            if pondDict[k][1] == 'low':
                lowInds += random.choices(pondDict[k][0],k=int(lowPondInds/len(lowPonds)))
            elif pondDict[k][1] == 'high':
                highInds += random.choices(pondDict[k][0],k=int(highPondInds/len(highPonds)))

        o = open(filePrefix+".pop.txt", "w")
        for l in lowInds:
            o.write('''%s\t%s\n''' % (l.getSampleID(), "low"))
        for h in highInds:
            o.write('''%s\t%s\n''' % (h.getSampleID(), "high"))
        o.close()

    def generateRandomBootstrapPopFile(self, pondDict, filePrefix):
        lowPonds=[p for p in pondDict.keys() if pondDict[p][1] == "low"]
        highPonds=[p for p in pondDict.keys() if pondDict[p][1] == "high"]
        lowPondInds = 0
        highPondInds = 0
        for pond in lowPonds:
            lowPondInds+=len(pondDict[pond][0])
        for pond in highPonds:
            highPondInds+=len(pondDict[pond][0])

        pondOrder=random.sample(["low",]*len(lowPonds) + ["high",]*len(highPonds), len(pondDict.keys()))

        lowInds = []
        highInds = []
        for j,k in enumerate(pondDict.keys()):
            if pondOrder[j] == 'low':
                lowInds += random.choices(pondDict[k][0],k=int(lowPondInds/len(lowPonds)))
            elif pondOrder[j] == 'high':
                highInds += random.choices(pondDict[k][0],k=int(highPondInds/len(highPonds)))

        o = open(filePrefix+".pop.txt", "w")
        for l in lowInds:
            o.write('''%s\t%s\n''' % (l.getSampleID(), "low"))
        for h in highInds:
            o.write('''%s\t%s\n''' % (h.getSampleID(), "high"))
        o.close()


    def getViablePonds(self, variable, minInds=0):
        '''returns a list of ponds that have a value for varible, and a list of the variable values'''
        viablePonds = []
        for i in self.getPopulationList():
            numPassed = len(["pass" for j in i.getIndividuals() if j.lowCov()==False])
            if (numPassed >= minInds) and (i.getPondStat(variable) != 'NA'):
                viablePonds.append(i)
        return viablePonds

    def generateExperiment(self, n, variable, prefix, permutations=100, quantiles=2, breakpoint=None):
        ''' print a population file to test for selection based on variable.
        experiment will include n individuals per population. If a population has fewer individuals, it will not be included.
        Individuals are selected based on coverage.
        also generates a file with maximum, minimum, and variance of the variable by pond.
        values for variable must be "canopy", "depth", "temp", "area", or "extinctionProbability" '''
        viablePonds=self.getViablePonds(variable, n)

        pondDict=self.makePondDict(variable, viablePonds, quantiles, n, breakpoint)

        self.generateIndListFile(pondDict, prefix)
        self.generatePondPopFile(pondDict, prefix + ".ponds.plink",  header="#IID\tpopulation\n")
        self.generateTraitPopFile(pondDict, prefix + ".category.plink", header="#IID\tpopulation\n")
        self.generateTraitPopFile(pondDict, prefix + ".category", header="")
        self.generateBayescanPopFile(pondDict, prefix)
        self.generateTraitStats(pondDict,variable, quantiles, prefix, n)
        self.makePermutations(permutations, pondDict, prefix)

    def makePondDict(self, variable, viablePonds, quantiles=2, n=0, breakpoint=None):
        pondDict = {}
        variableValues=[float(p.getPondStat(variable)) for p in viablePonds]
        if breakpoint:
            breakpoints=[breakpoint,]
        else:
            breakpoints = statistics.quantiles(variableValues, n=quantiles)
        print(breakpoints)
        for i in viablePonds:
            if float(i.getPondStat(variable)) <= breakpoints[0]:
                pondDict[i.getPondName()] = [i.getHighestCov(n), "low", float(i.getPondStat(variable))]
            elif float(i.getPondStat(variable)) >= breakpoints[-1]:
                pondDict[i.getPondName()] = [i.getHighestCov(n), "high", float(i.getPondStat(variable))]
        return(pondDict)

    def generateBayescanPopFile(self,pondDict,prefix):
        '''generate a pop file with one column individuals and the other column trait (1 or 2)
        pop 1 is low, 2 is high. Ends with .pop.txt'''
        #print(len(individuals), len(descriptor))
        o=open(prefix+".bayescan.pop.txt", "w")
        for k in pondDict.keys():
            if pondDict[k][1]=="low":
                cat=1
            elif pondDict[k][1]=="high":
                cat=2
            for i in pondDict[k][0]: #individuals
                o.write('''%s\t%s\n''' % (i.getSampleID(), cat))
        o.close()

    def generateIndListFile(self,pondDict,prefix):
        o=open(prefix+".inds.txt","w")
        for k in pondDict.keys():
            for i in pondDict[k][0]:
                o.write(i.getSampleID()+"\n")
        o.close()

    def makePermutations(self,permutations,pondDict,prefix):
        for perm in range(permutations):
            try:
                os.makedirs('''%s_permutations/''' % (prefix))
            except FileExistsError:
                pass
            filePrefix='''%s_permutations/%s_%i''' % (prefix,os.path.basename(prefix),perm)
            self.generateRandomTraitPopFile(pondDict, filePrefix)

    def generatePondPopFile(self, pondDict, prefix, header=""):
        '''generate a pop file with one column individuals and the other column pond
        optionally has a header. Ends with .pop.txt'''
        #print(len(individuals), len(descriptor))
        o=open(prefix+".pop.txt", "w")
        o.write(header)
        for k in pondDict.keys():
            for i in pondDict[k][0]: #individuals
                o.write('''%s\t%s\n''' % (i.getSampleID(), k))
        o.close()

    def generateTraitPopFile(self, pondDict, prefix, header=""):
        '''generate a pop file with one column individuals and the other column trait (high or low)
        optionally has a header. Ends with .pop.txt'''
        #print(len(individuals), len(descriptor))
        o=open(prefix+".pop.txt", "w")
        o.write(header)
        for k in pondDict.keys():
            for i in pondDict[k][0]: #individuals
                o.write('''%s\t%s\n''' % (i.getSampleID(), pondDict[k][1]))
        o.close()

    def generateRandomTraitPopFile(self,pondDict, prefix, header=""):
        '''generate a pop file with one column individuals and the other column trait (high or low)
        ponds randomly assigned to each group. optionally has a header. Ends with .pop.txt'''
        #print(len(individuals), len(descriptor))
        o=open(prefix+".pop.txt", "w")
        o.write(header)
        numPonds=len(pondDict.keys())
        stateList=["low",]* int((numPonds/2)) + ["high",] * int((numPonds/2))
        randomList=random.sample(stateList, len(stateList))
        for n,k in enumerate(pondDict.keys()):
            for i in pondDict[k][0]: #individuals
                o.write('''%s\t%s\n''' % (i.getSampleID(), randomList[n]))


    def generateTraitStats(self, pondDict, variable, quantile, prefix, n):
        '''generate general description of trait and test'''
        o=open(prefix + ".experimentStats.txt","w")
        if n == 0:
            n="All (bootstrapped)"
        allPonds=sorted(list(pondDict.keys()), key=lambda x: pondDict[x][2])
        #print(allPonds)
        o.write('''The trait being tested is: %s\n''' % (variable))
        o.write('''The top (high) and bottom (low) %i percent of ponds were included, which were %s\n''' % (100/quantile, ",".join(allPonds)))
        o.write('''%s individuals per pond were included \n''' % str(n))
        pondValue=[]
        for k in allPonds:
            o.write('''%s:%f %s\n''' % (k,pondDict[k][2], pondDict[k][1]))
        for k in allPonds:
            o.write('''%s: %s\n''' % (k,",".join([i.getSampleName() for i in pondDict[k][0]])))
