import statistics

def popstdev(list):
    c = statistics.pstdev(list, mu = None)
    return c

def popvar(list):
    c = statistics.pvariance(list, mu = None)
    return c

def sampvar(list):
    c = statistics.variance(list, xbar=None)
    return c

