from Statisticss.computation.extended.Variance_of_population_proportion import Variance_of_population_proportion

def Variance_of_sample_proportion(list):

    def split_list(list):
        half = len(list) // 2
        return list[:half]

    listx = split_list(list)

    c = Variance_of_population_proportion(listx)

    return c