from Statisticss.computation.extended.Variance_of_population_proportion import Variance_of_population_proportion
from Statisticss.computation.extended.split_list  import split_list
from Statisticss.computation.sample import Sample

def Variance_of_sample_proportion(list):


    s = 50
    listx = Sample(list,s)

    c = Variance_of_population_proportion(listx)

    return c