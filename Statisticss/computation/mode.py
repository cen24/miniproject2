import statistics

def mode(list):
    try:
        c = statistics.mode(list)
    except statistics.StatisticsError as e:
         print("There was an error with the statistics module")
        c = N.A
    return c