
from Statisticss.computation.extended.populationvar import populationvar
from Statisticss.computation.extended.proportion import proportion
from Statisticss.computation.extended.samplemean import samplemean
from Statisticss.computation.extended.samplestdev import samplestdev
from Statisticss.computation.extended.samplevar import samplevar
from Statisticss.computation.extended.zscore import zscore

def count(list):
    list = [1, 1, 1, 2, 3, 4, 5]
    c = len(list)


    return c

class extendedstat:
    result = 0

    list = [1, 2, 3, 4, 5]
    list_mode = [1, 2, 3, 4, 2]

    def __init__(self):
        pass

    def populationvar(self, list):
        self.result = populationvar(list)
        return self.result

    def samplevar(self, list):
        self.result = samplevar(list)
        return self.result

    def zscore_(self, z, list):
        self.result = zscore(z, list)
        return self.result

    def proportion_(self, a, b):
        self.result = proportion(a, b)
        return self.result

    def samplestdev(self, list):
        self.result = samplestdev(list)
        return self.result

    def samplemean(self, list):
        self.result = samplemean(list)
        return self.result

        # Variance of population proportion
        # Population Correlation Coefficient
        # Confidence Interval - done Chinedu
        # Population Variance
        # P Value(Rutvik)-done
        # Proportion(Rutvik) - done chinedu
        # Sample Mean(Rutvik)-done
        # Sample Standard Deviation(Rutvik)
        # Variance of sample proportion



#Variance of population proportion
#Population Correlation Coefficient
#Confidence Interval
#P Value
#Proportion
#Sample Mean
#Sample Standard Deviation
#Variance of sample proportion