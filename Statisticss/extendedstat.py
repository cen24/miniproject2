
from Statisticss.computation.extended.populationvar import populationvar
from Statisticss.computation.extended.proportion import proportion
from Statisticss.computation.extended.samplemean import samplemean
from Statisticss.computation.extended.samplestdev import samplestdev
from Statisticss.computation.extended.samplevar import samplevar
from Statisticss.computation.extended.zscore import zscore
from Statisticss.computation.extended.variancesampprop import variancesampprop
from Statisticss.computation.extended.variancesampprop import varianceofpopprop


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

    def variancesamprop_(self, list):
        self.result = variancesampprop(list)
        return self.result

    def variancesamprop_(self, list):
        self.result = variancepoppprop(list)
        return self.result




        # Population Correlation Coefficient
        # Confidence Interval - done Chinedu
        # P Value(Rutvik)-done
