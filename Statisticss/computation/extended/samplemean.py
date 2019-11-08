from Statisticss.computation.mean import mean
import random






def samplemean(list):
    r = random.sample(list, 5)
    c = mean(r)
    return c


list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
k = random.sample(list, k=5)


print("Below is a test")
print ("Population mean is:", mean(list))
print("Sample mean is:", samplemean(list))
print ("Generated Sample is:", k)
# formula; X = E x i / n
# http://www.differencebetween.net/science/difference-between-sample-mean-and-population-mean/
