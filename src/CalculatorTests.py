import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        self.assertEqual(self.calculator.add(3, 3), 6)
        self.assertEqual(self.calculator.result, 6)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(3, 3), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_division(self):
        self.assertEqual(self.calculator.division(3, 3), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_division(self):
        self.assertEqual(self.calculator.division(3, 3), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square(self):
        self.assertEqual(self.calculator.square(9), 81)
        self.assertEqual(self.calculator.result, 81)

    def test_squareroot(self):
        self.assertEqual(self.calculator.squareroot(81), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
