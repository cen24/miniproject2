from Statisticss.statisticss import statisticss



list = [1,2,3,4,5,6]


def cov(list):
    half = len(list)

    if len(list[:half]) != len(list[half:]):
        return


    a_mean = statisticss.mean_(list[:half])
    b_mean = statisticss.mean_(list[half:])

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/(len(a)-1)

def population_correlation_coefficient(list):
    half = len(list)


    x = cov(list)
    y = statisticss.stdev_(list[:half]) * statisticss.stdev_(list[half:])
    c = x / y
    return c


z = population_correlation_coefficient(list)
print(z)