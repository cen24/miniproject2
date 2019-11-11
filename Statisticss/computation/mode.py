import statistics

def mode(list):
    c = 0
    try:
        c = statistics.mode(list)
        return c
    except statistics.StatisticsError as e:
         print("There was no Repeating number in The given list")
    return c