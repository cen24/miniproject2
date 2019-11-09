import statistics

def stdev(list):
    c = statistics.pstdev(list, mu = None)
    return c