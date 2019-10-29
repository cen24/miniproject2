import unittest
import csv
from calculator import calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_add(self):
        self.calculator.addition(3, 3)
        self.assertEqual(self.calculator.result, 6)

    def test_sub(self):
        self.calculator.subtraction(3, 3)
        self.assertEqual(self.calculator.result, 0)

    def test_times(self):
        self.calculator.multiply(3, 3)
        self.assertEqual(self.calculator.result, 9)

    def test_div(self):
        self.calculator.division(3, 3)
        self.assertEqual(self.calculator.result, 1)

    def test_square(self):
        self.calculator.square_(9)
        self.assertEqual(self.calculator.result, 81)

    def test_sqrt(self):
        self.calculator.sqrt_(81)
        self.assertEqual(self.calculator.result, 9)

    def test_median(self):
        self.calculator.median_(self.calculator.list)
        self.assertEqual(self.calculator.result, 3)

    def test_mode(self):
        self.calculator.mode_(self.calculator.list_mode)
        self.assertEqual(self.calculator.result, 2)

    def test_mean(self):
        self.calculator.mean_(self.calculator.list)
        self.assertEqual(self.calculator.result, 3)

    def test_stdev(self):
        self.calculator.stdev_(self.calculator.list)
        self.assertEqual(self.calculator.result, 1.5811388300841898)

    def test_zscore(self):
        self.calculator.zscore_(5, self.calculator.list)
        self.assertEqual(self.calculator.result, 1.2649110640673518)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


   #def test_read_csv(self):

        #print(self.calculator.listy)
        #x = []
        #x = self.calculator.listy()
        #print(x)
        #self.assertEqual(self.calculator.result, 0)


    def test_read_csv_add(self):
        with open('uadd.csv', 'r') as f:
            next(f)
            reader = csv.reader(f)
            your_list = list(reader)

            for var in range(len(your_list)):
                a = int(your_list[var][0])
                b = int(your_list[var][1])
                c = int(your_list[var][2])

                self.calculator.addition(a, b)
                self.assertEqual(self.calculator.result, c)

    def test_sample_mean(self):
        listx = [170.5, 161, 160, 170, 150.5]
        self.calculator.sample_mean_(listx)
        self.assertEqual(self.calculator.result, 3.692560087527351)

    def test_sample_popvariance(self):
        self.calculator.popvariance_(list([1, 2, 3, 4, 5]))
        self.assertEqual(self.calculator.result, 2)





if __name__ == '__main__':
    unittest.main()
