from Statisticss.computation.populationmean import mean
from Statisticss.computation.extended.split_list  import split_list





def samplemean(list):
    r = split_list(list)
    c = mean(r)
    return c




#Sample mean = x = ( Σ xi ) / n
# http://www.differencebetween.net/science/difference-between-sample-mean-and-population-mean/
