from Statisticss.computation.extended.samplestdev import samplestdev
import statistics

#0.989743318610787

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,7]


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


z = population_correlation_coefficient(a,b)
print(z)