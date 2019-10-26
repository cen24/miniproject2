import unittest
from calculator import calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_addition(self):
        self.calculator.add(3, 3)
        self.assertEqual(self.calculator.result, 6)

    def test_subtraction(self):
        self.calculator.sub(3, 3)
        self.assertEqual(self.calculator.result, 0)

    def test_multiplication(self):
        self.calculator.times(3, 3)
        self.assertEqual(self.calculator.result, 9)

    def test_division(self):
        self.calculator.div(3, 3)
        self.assertEqual(self.calculator.result, 1)

    def test_square(self):
        self.calculator.square(9)
        self.assertEqual(self.calculator.result, 81)

    def test_squareRoot(self):
        self.calculator.sqrt(81)
        self.assertEqual(self.calculator.result, 9)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()