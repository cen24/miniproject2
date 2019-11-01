import math



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



class cal2:
    res2 = 0

    def addition(self, a, b):
        self.res2 = add(a, b)
        return self.res2

    def subtraction(self, a, b):
        self.res2 = sub(a, b)
        return self.res2

    def multiply(self, a, b):
        self.res2 = times(a, b)
        return self.res2

    def division(self, a, b):
        self.res2 = div(a, b)
        return self.res2

    def square_(self, a):
        self.res2 = square(a)
        return self.res2

    def sqrt_(self, a):
        self.res2 = sqrt(a)
        return self.res2