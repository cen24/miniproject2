#σ = sqrt[ Σ ( Xi – μ )2 / N ]
from CALCULATOR.SEPRATE.sqrt import sqrt
from CALCULATOR.Statistical.mean import mean
from CALCULATOR.SEPRATE.square import square

def Pop_Std_Dev(self, list):
    meanx = mean.mean(self,list)

    list_dev = list
    list_sq = list

    sq_total = 0

    for var in range(len(list)):
        list_dev[var] = list[var] - meanx
        list_sq[var] = square.square_(self, list_dev[var])
        sq_total = list_sq[var] + sq_total

    c = sq_total / len(list)
    c = sqrt.sqrt(self, c)
    return c

class PopulationStandardDeviation:
    c = 0
    def pop_std_dev(self,list):
        c = Pop_Std_Dev(self, list)
        return c



