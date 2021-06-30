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
        
    def test_divide(self):
        self.assertEqual(self.calculator.evaluate("8 / 4"), 2)

    def test_evaluate_simple(self):
        self.assertEqual(self.calculator.evaluate("1 + 1"), 2)

    def test_evaluate_chain(self):
        self.assertEqual(self.calculator.evaluate("2*-5-1/3.5+9"),
                         -1.2857142857142865)
