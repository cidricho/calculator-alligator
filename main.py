import tkinter as tk


class App(tk.Tk):
    """Main class of this application."""
    def __init__(self):
        super().__init__()

        # Sets the title of the window.
        self.title("Calculator Alligator")

        # Disallow window resizing.
        self.resizable(False, False)

        # Variables for the display and ans string
        self.display_string = tk.StringVar()
        self.display_ans = tk.StringVar()

        ans = tk.Label(self,
                       textvariable=self.display_ans,
                       font=('Courier', 10),
                       anchor="w")
        ans.grid(row=0, column=0, columnspan=4)

        display = tk.Entry(self,
                           textvariable=self.display_string,
                           relief="ridge",
                           justify='right',
                           state='disabled',
                           disabledbackground="black",
                           disabledforeground="white",
                           font=('Courier', 20))
        display.grid(row=1,
                     column=0,
                     columnspan=4,
                     padx=10,
                     ipadx=20,
                     ipady=20)

        # Button widgets

        # Buttons in Row 2 (Row 0 is for the Ans and Row 1 is for the Display widgets).

        b_sign = tk.Button(self,
                           text='-',
                           command=lambda: self.action_operation('-'))
        b_del = tk.Button(self,
                          text='Del',
                          command=lambda: self.delete_screen())
        b_ac = tk.Button(self, text='Clear', command=lambda: self.clear_screen())
        b_div = tk.Button(self,
                          text='÷',
                          command=lambda: self.action_operation('÷'))

        b_sign.grid(row=2, column=0)
        b_del.grid(row=2, column=1)
        b_ac.grid(row=2, column=2)
        b_div.grid(row=2, column=3)

        # Buttons in Row 3

        b_7 = tk.Button(self, text='7', command=lambda: self.action_number(7))
        b_8 = tk.Button(self, text='8', command=lambda: self.action_number(8))
        b_9 = tk.Button(self, text='9', command=lambda: self.action_number(9))
        b_mul = tk.Button(self,
                          text='×',
                          command=lambda: self.action_operation('×'))

        b_7.grid(row=3, column=0)
        b_8.grid(row=3, column=1)
        b_9.grid(row=3, column=2)
        b_mul.grid(row=3, column=3)

        # Buttons in Row 4

        b_4 = tk.Button(self, text='4', command=lambda: self.action_number(4))
        b_5 = tk.Button(self, text='5', command=lambda: self.action_number(5))
        b_6 = tk.Button(self, text='6', command=lambda: self.action_number(6))
        b_min = tk.Button(self,
                          text='−',
                          command=lambda: self.action_operation('-'))

        b_4.grid(row=4, column=0)
        b_5.grid(row=4, column=1)
        b_6.grid(row=4, column=2)
        b_min.grid(row=4, column=3)

        # Buttons in Row 5

        b_1 = tk.Button(self, text='1', command=lambda: self.action_number(1))
        b_2 = tk.Button(self, text='2', command=lambda: self.action_number(2))
        b_3 = tk.Button(self, text='3', command=lambda: self.action_number(3))
        b_add = tk.Button(self,
                          text='+',
                          command=lambda: self.action_operation('+'))

        b_1.grid(row=5, column=0)
        b_2.grid(row=5, column=1)
        b_3.grid(row=5, column=2)
        b_add.grid(row=5, column=3)

        # Buttons in Row 6

        b_dec = tk.Button(self,
                          text='.',
                          command=lambda: self.action_number('.'))
        b_0 = tk.Button(self, text='0', command=lambda: self.action_number(0))
        b_ans = tk.Button(self, text='Ans', command=lambda: self.action_ans())
        b_eq = tk.Button(self, text='=', command=lambda: self.action_equal())

        b_dec.grid(row=6, column=0)
        b_0.grid(row=6, column=1)
        b_ans.grid(row=6, column=2)
        b_eq.grid(row=6, column=3)

        # Sets the style of the widgets (buttons)
        for i in range(2, 7):
            for btn in self.grid_slaves(row=i):
                btn.grid(sticky="n" + "s" + "e" + "w", ipadx=20, ipady=20)
                if i > 0:
                    btn.config(font=('Courier'))

    def clean_expression(self, expr) -> str:
        """Gets the expression from the screen and replaces the signs to be used as python expression."""
        expr = expr.replace("×", "*")
        expr = expr.replace("÷", "/")
        return expr

    def delete_screen(self) -> None:
        """Deletes single character from the right."""
        self.display_string.set(self.display_string.get()[:-1])

    def clear_screen(self) -> None:
        """Clears the screen."""
        self.display_string.set("")

    def insert_screen(self, string) -> None:
        self.display_string.set(self.display_string.get() + string)

    def clear_ans(self) -> None:
        """Resets the ans indicator."""
        self.display_ans.set("")

    def set_ans(self, string: str = None) -> None:
        """Sets value for the Ans indicator if string argument is given."""
        if string:
            ans = "Ans: " + str(string)
            self.display_ans.set(ans)
        else:
            self.clear_ans()

    def get_ans(self) -> str:
        """Gets the ans value."""
        ans = self.display_ans.get()
        if ans:
            ans = ans.split(": ")[1]
        return ans

    def action_operation(self, operation: str) -> None:
        """
        Operation buttons handler. If there is evaluation answer in the screen it gets
        the answer and bring it to new string along with the operation pressed.
        Otherwise, it just add the operation in the screen.
        """
        new_str = operation
        screen_val = self.display_string.get()
        if "=" in screen_val:
            self.display_string.set("")
            new_str = screen_val.split("=")[1] + operation
        self.insert_screen(new_str)

    def action_ans(self) -> None:
        """Gets the Ans value from the indicator and pass it to the display."""
        if "=" in self.display_string.get():
            self.display_string.set("")
        self.insert_screen(self.get_ans())

    def action_number(self, number) -> None:
        """Inserts number in the screen."""
        self.insert_screen(str(number))

    def action_equal(self) -> None:
        """
        Equal button, commands evaluation of the current expression in the screen.
        Prohibits evaluation if there is answer from previous evaluation.
        Sets error message in the screen if there is one.
        """
        screen_val = self.clean_expression(self.display_string.get())
        if not "=" in screen_val:
            ans = Calculator.evaluate(self, screen_val)
            ans = str(ans).strip()
            if "Error" in ans:
                self.display_string.set(ans.split(": ")[1])
            else:
                self.set_ans(ans)
                self.insert_screen("=" + ans)


class Calculator:
    """Main class for the logic of this application"""
    def evaluate(self, exp: str):
        """Evaluate expression from the string value in the display."""
        try:
            ans = eval(exp)
        except SyntaxError:
            ans = "Error: Syntax Error"
        except ZeroDivisionError:
            ans = "Error: Math Error"
        return ans


if __name__ == "__main__":
    app = App()
    app.mainloop()
