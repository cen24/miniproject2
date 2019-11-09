from Statisticss.computation.mean import mean
from Calculator.calculator import calculator


class stattest(calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean_(self, list):
        self.data = mean(list)
        return self.data

