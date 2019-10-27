import math
import statistics
import _statistics

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
    math.sqrt(a)
    return c

def mean(list):
    list([a, b, d, e, f])
    c = statistics.mean(list)
    return c

def median(list):
    list([a, b, d, e, f])
    c = statistics.median(list)
    return c

def mode(list):
    list([a, b, d, e, f])
    c = statistics.mode(list)
    return c

def stdev(list):
    list([a, b, d, e, f])
    c = statistics.stdev(list)
    return c

# Variance of population proportion
# Z-Score
# Standardized score
# Population Correlation Coefficient
# Confidence Interval
# Population Variance
# P Value
# Proportion
# Sample Mean
# Sample Standard Deviation
# Variance of sample proportion

class calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = add(a, b)
        return  self.result

    def sub(self, a, b):
        self.result = sub(a, b)
        return  self.result

    def times(self, a, b):
        self.result = times(a, b)
        return  self.result

    def div(self, a, b):
        self.result = div(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)

    def sqrt(self, a):
        self.result = math.sqrt(a)

    def mean(self, list):
        self.result = statistics.mean(list)
        return self.result

    def median(self, list):
        self.result = statistics.median(list)
        return self.result

    def mode(self, list):
        self.result = statistics.mode(list)
        return self.result

    def stdev(self, list):
        self.result = statistics.stdev(list)
        return self.result