
from Statisticss.computation.zscore import zscore

# new formulas added
from Statisticss.computation.proportion import prop


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

    def zscore_(self, z, list):
        self.result = zscore(z, list)
        return self.result

    def proportion(self, a, b):
        self.result = prop(a, b)
        return self.result

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