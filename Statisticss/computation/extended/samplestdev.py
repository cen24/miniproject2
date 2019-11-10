import statistics
from Statisticss.computation.extended.split_list  import split_list

def samplestdev(list):
    r = split_list(list)
    c = statistics.stdev(r, xbar = None)
    return c