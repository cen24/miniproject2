from CALCULATOR.new import xyz
from CALCULATOR.SEPRATE.sqrt import sqrt


class s:


    def sample_mean(self, list):
        meanx = xyz.mean_(self,list)

        list_dev = list
        list_sq = list

        sq_total = 0

        for var in range(len(list)):
            list_dev[var] = list[var] - meanx
            list_sq[var] = sqrt.sqrt(self,list_dev[var])
            sq_total = list_sq[var] + sq_total

        n = len(list) - 1
        n1 = sq_total / n
        n2 = sqrt.sqrt(self,n1)

        c = n2 / sqrt.sqrt(self,len(list))

        return c

