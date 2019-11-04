import statistics


def median_(list):
    c = statistics.median(list)
    return c

class median:
    result = 0
    def median(self,list):
        self.result = median_(list)
        return self.result