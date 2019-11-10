from Statisticss.computation.extended.Variance_of_population_proportion import Variance_of_population_proportion
from Statisticss.computation.extended.split_list  import split_list

def Variance_of_sample_proportion(list):



    listx = split_list(list)

    c = Variance_of_population_proportion(listx)

    return c