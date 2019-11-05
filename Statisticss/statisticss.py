from Statisticss.computation.statistics import mean
from Statisticss.computation.statistics import median
from Statisticss.computation.statistics import mode
from Statisticss.computation.statistics import stdev
#from Statisticss.computation.zscore import zscore
#from Statisticss.computation.proportion import prop


class statisticss:
    result = 0

    list = [1, 2, 3, 4, 5]
    list_mode = [1, 2, 3, 4, 2]

    def __init__(self):
        pass

    def mean_(self, list):
        self.result = mean(list)
        return self.result

    def median_(self, list):
        self.result = median(list)
        return self.result

    def mode_(self, list):
        self.result = mode(list)
        return self.result

    def stdev_(self, list):
        self.result = stdev(list)
        return self.result

    # def zscore_(self, z, list):
    #     self.result = zscore(z, list)
    #     return self.result
    #
    # def proportion(self, a, b):
    #     self.result = prop(a, b)
    #     return self.result

        # Variance of population proportion
        # Standardized score
        # Population Correlation Coefficient
        # Confidence Interval - done Chinedu
        # Population Variance
        # P Value(Rutvik)-done
        # Proportion(Rutvik) - done chinedu
        # Sample Mean(Rutvik)-done
        # Sample Standard Deviation(Rutvik)
        # Variance of sample proportion





