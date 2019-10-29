import math
import statistics
import csv


def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def times(a, b):
    c = a * b
    return c

def div(a, b):
    c = a / b
    return c

def square(a):
    c = a * a
    return c

def sqrt(a):
    c = math.sqrt(a)
    return c

def mean(list):
    c = statistics.mean(list)
    return c

def median(list):
    c = statistics.median(list)
    return c

def mode(list):
    c = statistics.mode(list)
    return c

def stdev(list):
    c = statistics.stdev(list)
    return c

def zscore(z, list):
    meanx = mean(list)
    stdevx = stdev(list)
    c = (z - meanx) / stdevx
    return c

def sample_mean(list):

    meanx = mean(list)

    list_dev = list
    list_sq = list

    sq_total=0

    for var in range(len(list)):

        list_dev[var] = list[var] - meanx
        list_sq[var] = square(list_dev[var])
        sq_total=list_sq[var]+sq_total


    n = len(list) - 1
    n1 = sq_total / n
    n2 = sqrt(n1)

    c = n2 / sqrt(len(list))
    return c

def popvariance(list):

    meanx = mean(list)

    list_dev = list
    list_sq = list

    sq_total = 0

    for var in range(len(list)):
        list_dev[var] = list[var] - meanx
        list_sq[var] = square(list_dev[var])
        sq_total = list_sq[var] + sq_total

    n = len(list)
    c = sq_total / n

    return c

def pvalue(list):

    meanx = mean(list)
    stdevx = stdev(list)

    meanx = meanx - stdevx

    popx = popvariance(list)
    popx = sqrt(popx)
    n = sqrt(len(list))

    popx = popx / n

    c = meanx / popx

    return c
















# Variance of population proportion

# Standardized score
# Population Correlation Coefficient
# Confidence Interval
# Population Variance
# P Value(Rutvik)-done
# Proportion(Rutvik)
# Sample Mean(Rutvik)
# Sample Standard Deviation(Rutvik)
# Variance of sample proportion

class calculator:
    result = 0
    list = [1, 2, 3, 4, 5]
    list_mode =[1, 2, 3, 4, 2]

  #  def listy(self):
   #  with open('uadd.csv', 'r') as f:
    #        next(f)
     #       reader = csv.reader(f)
      #      your_list = list(reader)
       # for var in range(len(your_list)):
        #    a[var] = int(your_list[var][0])
         #   b[var] = int(your_list[var][1])
          #  c[var] = int(your_list[var][2])
#
 #           self.list2 = a
  #      return self.list2
        



    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = add(a, b)
        return self.result

    def subtraction(self, a, b):
        self.result = sub(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = times(a, b)
        return self.result

    def division(self, a, b):
        self.result = div(a, b)
        return self.result

    def square_(self, a):
        self.result = square(a)

    def sqrt_(self, a):
        self.result = sqrt(a)
        return self.result

    def mean_(self, list):
        self.result = mean(list)
        return self.result

    def median_(self, list):
        self.result = median(list)
        return self.result

    def mode_(self, list):
        self.result = mode(list)
        return self.result

    def stdev_(self, list):
        self.result = stdev(list)
        return self.result

    def zscore_(self, z, list):
        self.result = zscore(z, list)
        return self.result

    def sample_mean_(self, list):
        self.result = sample_mean(list)
        return self.result

    def popvariance_(self, list):
        self.result = popvariance(list)
        return self.result
    def pvalue_(self, list):
        self.result = pvalue(list)
        return self.result



    def read_csv_add(self):
        with open('uadd.csv', 'r') as f:
            next(f)
            reader = csv.reader(f)
            your_list = list(reader)

            #n = len(list)-1
            #new_list = [range(1, 6), range(15, 20)]
            #a = [range(0,n)]
            #b = [range(0,n)]
            #c = [range(0,n)]

            for var in range(len(your_list)):
                a = int(your_list[var][0])
                b = int(your_list[var][1])
                c = int(your_list[var][2])
                print(a, b, c)


