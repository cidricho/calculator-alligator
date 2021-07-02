import tkinter as tk


class App(tk.Tk):
    """Main class of this application."""
    def __init__(self):
        super().__init__()

        # Sets the title of the window.
        self.title("Calculator")

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

        clear = tk.Button(self,
                          text="Clear",
                          relief='flat')
        clear.grid(row=0, column=3)

        display = tk.Entry(self,
                           textvariable=self.display_string,
                           relief="ridge",
                           justify='right',
                           state='disabled',
                           disabledbackground="white",
                           disabledforeground="black",
                           font=('Courier', 20))
        display.grid(row=1,
                     column=0,
                     columnspan=4,
                     padx=10,
                     ipadx=20,
                     ipady=20)

        # Button widgets

        # Buttons in Row 2 (Row 0 is for the Ans and Row 1 is for the Display widgets).

        b_sign = tk.Button(self, text='-')
        b_del = tk.Button(self, text='Del')
        b_ac = tk.Button(self, text='AC')
        b_div = tk.Button(self, text='÷')

        b_sign.grid(row=2, column=0)
        b_del.grid(row=2, column=1)
        b_ac.grid(row=2, column=2)
        b_div.grid(row=2, column=3)

        # Buttons in Row 3

        b_7 = tk.Button(self, text='7')
        b_8 = tk.Button(self, text='8')
        b_9 = tk.Button(self, text='9')
        b_mul = tk.Button(self, text='×')

        b_7.grid(row=3, column=0)
        b_8.grid(row=3, column=1)
        b_9.grid(row=3, column=2)
        b_mul.grid(row=3, column=3)

        # Buttons in Row 4

        b_4 = tk.Button(self, text='4')
        b_5 = tk.Button(self, text='5')
        b_6 = tk.Button(self, text='6')
        b_min = tk.Button(self, text='−')

        b_4.grid(row=4, column=0)
        b_5.grid(row=4, column=1)
        b_6.grid(row=4, column=2)
        b_min.grid(row=4, column=3)

        # Buttons in Row 5

        b_1 = tk.Button(self, text='1')
        b_2 = tk.Button(self, text='2')
        b_3 = tk.Button(self, text='3')
        b_add = tk.Button(self, text='+')

        b_1.grid(row=5, column=0)
        b_2.grid(row=5, column=1)
        b_3.grid(row=5, column=2)
        b_add.grid(row=5, column=3)

        # Buttons in Row 6

        b_dec = tk.Button(self, text='.')
        b_0 = tk.Button(self, text='0')
        b_ans = tk.Button(self, text='Ans')
        b_eq = tk.Button(self, text='=')

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
    
if __name__ == "__main__":
    app = App()
    app.mainloop()