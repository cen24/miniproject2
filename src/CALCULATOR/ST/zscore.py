from CALCULATOR.Statistical.mean import mean
from CALCULATOR.Statistical.stddev import stddev


def zscore_(self, z, list):
    meanx = mean.mean(self, list)
    stdevx = stddev.stddev(self, list)
    c = (z - meanx) / stdevx
    return c

class z:
    c = 0;
    def zscore(self,z,list):
        c = zscore_(self,z , list)
        #print(c)
        return c
