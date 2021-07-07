import unittest
from main import Calculator, App

class Test(unittest.TestCase):

    def test_addition(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("1 + 2"), 3)

    def test_subtract(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("3 - 4"), -1)

    def test_multiply(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("5 * 6"), 30)

    def test_divide(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("8 / 4"), 2)

    def test_evaluate_simple(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("1 + 1"), 2)

    def test_evaluate_chain(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("2*-5-1/3.5+9"),
                         -1.2857142857142865)

    def test_syntax_error(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("1 +/ 1"),
                         "Error: Syntax Error")

    def test_math_error(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.evaluate("9/0"), "Error: Math Error")

    def setUp(self):
        self.app = App()
    
    def tearDown(self):
        self.app.destroy()

    def test_startup(self):
        self.assertEqual(self.app.winfo_toplevel().title(), "Calculator Alligator")

    def test_screen_set(self):
        self.app = App()
        self.app.display_string.set("string")
        self.assertTrue(len(self.app.display_string.get()) > 0)
     
    def test_action_operations_populated(self):
        self.app.display_string.set("2×5=10")
        self.app.action_operation(operation)
        self.assertEqual(self.app.display_string.get(), "10" + operation)

if __name__ == "__main__":
    unittest.main()
