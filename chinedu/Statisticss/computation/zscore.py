#from Statisticss.computation import mean
#from Statisticss.computation import stdev

# z = (X - μ) / σ
#formula used below is crossed multiplied where c is X

import statistics


def zscore(z, list):
    mean = statistics.mean(list)
    stdev = statistics.stdev(list)
    c = (z * stdev) + mean
    return c

##from scipy import stats

#Or we can use the below formula by importing scipy

##def zscore2(list):
    ##list = [20, 2, 7, 1, 34]
    ##c = stats.zscore(list)
    ##return c

##print (zscore2(list))

