from Statisticss.computation.mean import mean
from Statisticss.computation.median import median
from Statisticss.computation.mode import mode
from Statisticss.computation.stdev import stdev

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




