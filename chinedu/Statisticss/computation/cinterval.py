from Statisticss.computation.stdev import stdev
from Statisticss.computation.mean import mean
from Statisticss.computation.sampmean import s

import math

def cinterval(s):
    # H, find the T-value (<30 sample size)
    # (Calculate your T-Value by taking the difference between the mean and population mean
    # (sample mean - pop mean)
    # and dividing it over the standard deviation divided by the degrees (stdev - n)
    # of freedom square root.

    n = 10
    stdev = 25
    mean = 240
    #b = (100 - a) / 100
    #d = b / 2
    #g = count(list)

    df = n - 1
    #1, above should be used  to calculate Tvalue
    #https://www.statisticshowto.datasciencecentral.com/
    # probability-and-statistics/confidence-interval/

    tval = 2.262
    h = (s - mean ) / (stdev / math.sqrt(n)) #h should equal Tval and tval should be removed
    se = stdev / math.sqrt(n)
    #2, above was used to calculate Standard of error
    e = tval * se

    # upper limit
    c = mean + e

    # lower limit
    f = mean - e
    return c, f, h


print (cinterval(95))

