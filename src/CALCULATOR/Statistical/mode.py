import statistics

def mode_(list):
    c = statistics.mode(list)
    return c

class mode:
    result = 0
    def mode(self,list):
        self.result = mode_(list)
        return self.result
