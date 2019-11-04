#from Statisticss.computation import mean
#from Statisticss.computation import stdev
import statistics



def zscore(z, list):
    mean = statistics.mean(list)
    stdev = statistics.stdev(list)
    c = (z - mean) / stdev
    return c

