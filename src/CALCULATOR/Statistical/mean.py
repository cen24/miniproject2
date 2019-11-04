import statistics

def mean_(list):
    c = statistics.mean(list)
    return c

class mean:
    result = 0
    def mean(self,list):
        self.result = mean_(list)
        return self.result