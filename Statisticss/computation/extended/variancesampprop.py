import statistics

list  = [2.74, 1.23, 2.63, 2.22, 3, 1.98]

def split_list(list):
        half = len(list) // 2
        return list[:half]


def variancesampprop(list):
        r = statistics.variance(list, xbar = None)
        c = r
        return c



print("Variance of sample set is % s"%varianceofsampprop(list1))
