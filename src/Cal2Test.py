import unittest
from CALCULATOR.Cal2 import cal2
from CALCULATOR.readcsv import read_csv

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cal2 = cal2()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.cal2, cal2)


    def test_add_from_csv(self):

        y = read_csv("uadd.csv")

        for var in range(len(y)):
            self.cal2.addition(y[0][var], y[1][var])
            self.assertEqual(self.cal2.res2, y[2][var])




    if __name__ == '__main__':
        unittest.main()