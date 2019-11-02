import math
from CALCULATOR.SEPRATE.addition import addition2
from CALCULATOR.SEPRATE.subtraction import subtraction
from CALCULATOR.SEPRATE.multiply import multiply
from CALCULATOR.SEPRATE.division import division







def div(a, b):
    c = a / b
    return c

def square(a):
    c = a * a
    return c

def sqrt(a):
    c = math.sqrt(a)
    return c


class cal2():
    res2 = 0

    def __init__(self):
        pass

    def setUp(self) -> None:
        self.addition2 = addition2()
        self.subtraction = subtraction()
        self.multiply = multiply()
        self.division = division()


    def addition(self, a, b):
        self.res2 = addition2.addition3(self,a,b)
        return self.res2

    def subtraction(self, a, b):
        self.res2 = subtraction.subtraction(self,a, b)
        return self.res2

    def multiply(self, a, b):
        self.res2 = multiply.multiply(self,a, b)
        return self.res2

    def division(self, a, b):
        self.res2 = division.division(self,a,b)
        return self.res2

    def square_(self, a):
        self.res2 = square(a)
        return self.res2

    def sqrt_(self, a):
        self.res2 = sqrt(a)
        return self.res2

