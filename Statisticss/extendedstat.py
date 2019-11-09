from Statisticss.computation.extended.populationvar import populationvar
from Statisticss.computation.extended.proportion import proportion
from Statisticss.computation.extended.samplemean import samplemean
from Statisticss.computation.extended.samplestdev import samplestdev
from Statisticss.computation.extended.samplevar import samplevar
from Statisticss.computation.extended.zscore import zscore
from Statisticss.computation.extended.population_correlation_coefficient import population_correlation_coefficient
from Statisticss.computation.extended.pvalue import pvalue



class extendedstat:
    result = []

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

    def population_correlation_coefficient_(self,a,b):
        self.result = population_correlation_coefficient(a,b)
        return self.result

    def pvalue_(self, a, b, c, d):
        self.result = pvalue(a, b, c, d)
        return self.result


        # Variance of population proportion
        # Population Correlation Coefficient(rutvik)
        # Confidence Interval - done Chinedu
        # Population Variance
        # P Value(Rutvik)-done
        # Proportion(Rutvik) - done chinedu
        # Sample Mean(Rutvik)-done
        # Sample Standard Deviation(Rutvik)
        # Variance of sample proportion
