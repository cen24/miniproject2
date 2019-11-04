import statistics

def stdev_(list):
    c = statistics.stdev(list)
    return c

class stddev:
    result = 0
    def stddev(self,list):
        self.result = stdev_(list)
        return self.result