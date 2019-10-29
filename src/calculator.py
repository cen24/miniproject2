import math
import statistics
import stat

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



# Variance of population proportion

# Standardized score
# Population Correlation Coefficient
# Confidence Interval
# Population Variance
# P Value(Rutvik)
# Proportion(Rutvik)
# Sample Mean(Rutvik)
# Sample Standard Deviation(Rutvik)
# Variance of sample proportion

class calculator:
    result = 0

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
