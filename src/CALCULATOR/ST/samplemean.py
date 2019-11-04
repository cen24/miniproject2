from CALCULATOR.Statistical.mean import mean
from CALCULATOR.SEPRATE.sqrt import sqrt


def sample_mean_(self, list):
    meanx = mean.mean(self, list)

    list_dev = list
    list_sq = list

    sq_total = 0

    for var in range(len(list)):
        list_dev[var] = list[var] - meanx
        list_sq[var] = sqrt.sqrt(self, list_dev[var])
        sq_total = list_sq[var] + sq_total

    n = len(list) - 1
    n1 = sq_total / n
    n2 = sqrt.sqrt(self, n1)

    c = n2 / sqrt.sqrt(self, len(list))

    return c


class s:
    c = 0
    def sample_mean(self, list):
        c = sample_mean_(self, list)
        return c



