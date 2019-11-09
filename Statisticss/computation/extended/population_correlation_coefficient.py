from Statisticss.statisticss import statisticss
import numpy as np
import statistics



a = [1,2,3,4,5,6]
b = [1,2,3,4,5,7]


def cov(a, b):

    if len(a) != len(b):
        return

    a_mean = np.mean(a)
    b_mean = np.mean(b)

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/(len(a)-1)

def population_correlation_coefficient(list):

    x = cov(a,b)
    y = statistics.stdev(a) * statistics.stdev(b)
    c = x/y
    return c


z = population_correlation_coefficient(list)
print(z)