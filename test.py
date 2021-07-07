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
    
    def tearDown(self):
        self.app = App()
        self.app.destroy()

    def test_startup(self):
        self.app = App()
        self.assertEqual(self.app.winfo_toplevel().title(), "Calculator Alligator")

    def test_screen_set(self):
        self.app = App()
        self.app.display_string.set("string")
        self.assertTrue(len(self.app.display_string.get()) > 0)

    def test_screen_get(self):
        self.app = App()
        self.app.display_string.set("string")
        self.assertEqual(self.app.display_string.get(), "string")

    def test_screen_clear(self):
        self.app = App()
        self.app.display_string.set("string")
        self.app.clear_screen()
        self.assertEqual(len(self.app.display_string.get()), 0)

    def test_screen_delete(self):
        self.app = App()
        self.app.display_string.set("string")
        self.app.delete_screen()
        self.assertEqual(self.app.display_string.get(), "strin")

    def test_screen_insert(self):
        self.app = App()
        self.app.display_string.set("string")
        self.app.insert_screen("s")
        self.assertEqual(self.app.display_string.get(), "strings")

    def test_ans_set(self):
        self.app = App()
        self.app.set_ans("1234")
        self.assertTrue(len(self.app.display_ans.get()) > 0)

    def test_ans_get(self):
        self.app = App()
        self.app.display_ans.set("string")
        self.assertEqual(self.app.display_ans.get(), "string")

    def test_ans_clear(self):
        self.app = App()
        self.app.display_ans.set("string")
        self.app.clear_ans()
        self.assertEqual(len(self.app.display_ans.get()), 0)

    def test_clean_expr(self):
        self.app = App()
        expr = "2×-5-1÷3.5+9"
        self.assertEqual(self.app.clean_expression(expr), "2*-5-1/3.5+9")

    def test_action_equal(self):
        self.app = App()
        self.app.display_string.set("2×-5-1÷3.5+9")
        self.app.action_equal()
        display_string = "2×-5-1÷3.5+9=-1.2857142857142865"
        self.assertEqual(self.app.display_string.get(), display_string)

    def test_action_equal_populated(self):
        self.app = App()
        display_string = "2×5=10"
        self.app.display_string.set(display_string)
        self.app.action_equal()
        self.assertEqual(self.app.display_string.get(), display_string)

    def test_action_ans(self):
        self.app = App()
        self.app.display_ans.set("Ans: 1234")
        self.app.action_ans()
        self.assertEqual(self.app.display_string.get(), "1234")

    def test_action_ans_populated(self):
        self.app = App()
        self.app.display_string.set("2×5=10")
        self.app.action_ans()
        self.assertEqual(self.app.display_string.get(), "")

    def test_action_numbers(self):
        self.app = App()
        nums = "0123456789."
        for num in nums:
            self.app.action_number(num)
        self.assertEqual(self.app.display_string.get(), nums)

    def test_action_operations(self):
        self.app = App()
        operations = "×÷+-"
        for operation in operations:
            self.app.action_operation(operation)
        self.assertEqual(self.app.display_string.get(), operations)

    def test_action_operations_populated(self):
        self.app = App()
        operations = "×÷+-"
        for operation in operations:
            self.app.display_string.set("2×5=10")
            self.app.action_operation(operation)
            self.assertEqual(self.app.display_string.get(), "10" + operation)
            
if __name__ == "__main__":
    unittest.main()
