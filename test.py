from main import Calculator
import unittest
class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.evaluate("1 +2"), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 4), -1)
        self.assertEqual(self.calculator.evaluate("3 - 4"), -1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 6), 30)
        self.assertEqual(self.calculator.evaluate("5 * 6"), 30)