from Statisticss.computation import mean
from Statisticss.computation import stdev
from Statisticss.computation.extended.populationvar import populationvar
from Calculator.computation import squareroot as sqrt
from
import statistics
import math

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

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half]


def pval(a, list):
    p = split_list(list)
    pO = float(a)
    f = p - pO
    n = len(list)
    z = f / (math.sqrt(pO*(1-pO)/(n)))
    return z

    p =  80 /240
    pO = float(.27)
    f = p - pO
    n = len(list)
    z = f / (math.sqrt(pO*(1-pO)/(n)))





