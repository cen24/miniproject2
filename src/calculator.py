import math
import statistics

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