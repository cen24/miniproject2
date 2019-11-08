from Statisticss.computation.mean import mean
from Statisticss.computation.stdev import stdev




def zscore(z, list):
    c = (z * stdev(list)) + mean(list)
    return c

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#print(zscore(1.2, list))
#print (stdev(list))
#print (mean(list))




# z = (X - μ) / σ
#where z is the z-score, X is the value of the element,
#μ is the mean of the population,
#and σ is the standard deviation. ( Z  and List wouold be a pulled from CSV)
#https://github.com/hl533/IS601-CalculatorProject/blob/master/References/Standardized_Zscore.md

##from scipy import stats
#Or we can use the below formula by importing scipy
##def zscore2(list):
    ##list = [20, 2, 7, 1, 34]
    ##c = stats.zscore(list)
    ##return c

##print (zscore2(list))

