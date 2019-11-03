from CALCULATOR.new import xyz

class z:
    def zscore(self,z,list):

        meanx = xyz.mean_(self,list)
        stdevx = xyz.stdev_(self,list)
        c = (z - meanx) / stdevx
        return c