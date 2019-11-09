import statistics

list  = [2.74, 1.23, 2.63, 2.22, 3, 1.98]

def split_list(a_list):
        half = len(a_list) // 2
        return a_list[:half]


def varianceofsampprop(list):
        c = %statistics.variance(list, xbar = None)
        return c



print("Variance of sample set is % s"%varianceofsampprop(list))
