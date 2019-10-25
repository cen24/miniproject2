def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    c = a - b
    return c

def multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    c = a / b
    return c

def square(a):
    c = a**2
    return c

def squareroot(a):
    c = a**(1/2)
    return c


# The above lines of code are from the Calculator Assignment
# Below is the extension that performs statistical calculations


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result
    def division(self, a, b):
        self.result = division(a, b)
        return self.result
    def square(self, a):
        self.result = square(a)
        return self.result
    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result