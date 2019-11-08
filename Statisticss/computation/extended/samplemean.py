from Statisticss.computation.mean import mean



def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half]



def samplemean(list):

    r = split_list(list)
    c = mean(r)
    return c


# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# k = random.sample(list, k=5)


# print("Below is a test")
# print ("Population mean is:", mean(list))
# print("Sample mean is:", samplemean(list))
# print ("Generated Sample is:", k)
# formula; X = E x i / n
# http://www.differencebetween.net/science/difference-between-sample-mean-and-population-mean/
