from CALCULATOR.new import xyz


def zscore_(self, z, list):
    meanx = xyz.mean_(self, list)
    stdevx = xyz.stdev_(self, list)
    c = (z - meanx) / stdevx
    return c

class z:
    c = 0;
    def zscore(self,z,list):
        c = zscore_(self,z , list)
        print(c)
        return c
