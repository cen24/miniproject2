from Statisticss.computation.extended.samplestdev import samplestdev
import statistics

def cov(a, b):

    if len(a) != len(b):
        return

    a_mean = statistics.mean(a)
    b_mean = statistics.mean(b)

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/(len(a)-1)

def population_correlation_coefficient(a,b):

    x = cov(a,b)
    y = samplestdev(a) * samplestdev(b)
    c = x/y
    return c