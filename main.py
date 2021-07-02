class Calculator:
    """Main class for the logic of this application"""
    def evaluate(self, exp: str) :
        """Evaluate expresssion from the string value in the display."""
        try:
            ans = eval(exp)
        except SyntaxError:
            ans = "Error: Syntax Error"
        except ZeroDivisionError:
            ans = "Error : Math Error"
        return ans 