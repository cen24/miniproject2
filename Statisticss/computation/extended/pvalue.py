from Statisticss.computation import mean
from Statisticss.computation import stdev
from Statisticss.computation.extended.populationvar import populationvar
from Calculator.computation import squareroot as sqrt


def pvalue(list):

    meanx = mean(list)
    stdevx = stdev(list)

    meanx2 = (meanx - stdevx)

    popx = populationvar
    popx2 = sqrt(popx)
    n = sqrt(len(list))

    #opx3 = popx / n

    c = meanx2 / popx2
    print(c)

    return c

# NEEDS FIXING
