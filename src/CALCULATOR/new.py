import statistics

def mean_(list):
    c = statistics.mean(list)
    return c

def median_(list):
    c = statistics.median(list)
    return c

def mode_(list):
    c = statistics.mode(list)
    return c

def stdev_(list):
    c = statistics.stdev(list)
    return c

class xyz:
    result = 0


    def mean_(self, list):
        self.result = mean_(list)
        return self.result

    def median_(self, list):
        self.result = median_(list)
        return self.result

    def mode_(self, list):
        self.result = mode_(list)
        return self.result

    def stdev_(self, list):
        self.result = stdev_(list)
        return self.result