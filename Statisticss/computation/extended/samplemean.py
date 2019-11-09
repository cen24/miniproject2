from Statisticss.computation.populationmean import mean



def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half]



def samplemean(list):

    r = split_list(list)
    c = mean(r)
    return c




#Sample mean = x = ( Σ xi ) / n
# http://www.differencebetween.net/science/difference-between-sample-mean-and-population-mean/
