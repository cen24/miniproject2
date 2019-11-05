from Statisticss.computation import mean
from Statisticss.computation import stdev
from Statisticss.computation import popvariance
from Calculator.computation import squareroot as sqrt


def pvalue(list):

    meanx = mean
    stdevx = stdev

    meanx2 = (meanx - stdevx)

    popx = popvariance
    popx2 = sqrt(popx)
    n = sqrt(len(list))

    popx3 = popx / n

    c = meanx2 / popx2

    return c

# NEEDS FIXING
