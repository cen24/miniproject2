import math
from CALCULATOR.SEPRATE.addition import addition
from CALCULATOR.SEPRATE.subtraction import subtraction
from CALCULATOR.SEPRATE.multiply import multiply
from CALCULATOR.SEPRATE.division import division
from CALCULATOR.SEPRATE.square import square
from CALCULATOR.SEPRATE.sqrt import sqrt



class cal2():
    res2 = 0

    def __init__(self):
        pass

    def setUp(self) -> None:
        self.addition = addition()
        self.subtraction = subtraction()
        self.multiply = multiply()
        self.division = division()
        self.square = square()
        self.sqrt = sqrt()

    def addition(self, a, b):
        self.res2 = addition.addition(self, a, b)
        return self.res2

    def subtraction(self, a, b):
        self.res2 = subtraction.subtraction(self, a, b)
        return self.res2

    def multiply(self, a, b):
        self.res2 = multiply.multiply(self, a, b)
        return self.res2

    def division(self, a, b):
        self.res2 = division.division(self, a, b)
        return self.res2

    def square_(self, a):
        self.res2 = square.square_(self, a)
        return self.res2

    def sqrt_(self, a):
        self.res2 = sqrt.sqrt(self, a)
        return self.res2

