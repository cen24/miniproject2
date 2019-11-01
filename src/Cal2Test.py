import unittest
from CALCULATOR.Cal2 import cal2
from CALCULATOR.readcsv import read
from CALCULATOR.Stat import xyz
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cal2 = cal2()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.cal2, cal2)


    def test_add_from_csv(self):

        y = read.read_csv("../src/CSV FILES/uadd.csv")

        for var in range(len(y)):
            self.cal2.addition(y[0][var], y[1][var])
            self.assertEqual(self.cal2.res2, y[2][var])

    def test_sub_from_csv(self):

        y = read.read_csv("../src/CSV FILES/Unit Test Subtraction.csv")

        for var in range(len(y)):
            self.cal2.subtraction(y[0][var], y[1][var])
            self.assertEqual(self.cal2.res2, y[2][var]*-1)

    def test_mul_from_csv(self):

        y = read.read_csv("../src/CSV FILES/Unit Test Multiplication.csv")

        for var in range(len(y)):
            self.cal2.multiply(y[0][var], y[1][var])
            self.assertEqual(self.cal2.res2, y[2][var])

    def test_div_from_csv(self):

        y = read.read_csv("../src/CSV FILES/Unit Test Division.csv")

        for var in range(len(y)):
            self.cal2.division(y[1][var], y[0][var])
            self.assertEqual(int(self.cal2.res2), int(y[2][var]))

    def test_square_from_csv(self):

        y = read.read_csv("../src/CSV FILES/Unit Test Square.csv")

        for var in range(len(y)):
            self.cal2.square_(y[0][var])
            self.assertEqual(int(self.cal2.res2), int(y[1][var]))

    def test_sqrt_from_csv(self):

        y = read.read_csv("../src/CSV FILES/Unit Test Square Root.csv")

        for var in range(len(y)):
            self.cal2.sqrt_(y[0][var])
            self.assertEqual(int(self.cal2.res2), int(y[1][var]))

    def test_array(self):
        y = read.read_array("../src/CSV FILES/array2.csv")

        for var in range(len(y)):
            list = y[var]
            x = self.xyz.mean(list)
            print(x)







        self.assertEqual(0,0)





    if __name__ == '__main__':
        unittest.main()