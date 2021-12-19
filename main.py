from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Basic Pyhon Calculator")
        master.iconbitmap("calculator_icon.ico")
        self.equation = Entry(master, width=36, border=5, justify=RIGHT)
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.createButton()

    def createButton(self):
        b0 = self.addButton("0")
        b1 = self.addButton("1")
        b2 = self.addButton("2")
        b3 = self.addButton("3")
        b4 = self.addButton("4")
        b5 = self.addButton("5")
        b6 = self.addButton("6")
        b7 = self.addButton("7")
        b8 = self.addButton("8")
        b9 = self.addButton("9")
        b_decimal = self.addButton(".")
        b_plus = self.addButton("+")
        b_minus = self.addButton("-")
        b_mult = self.addButton("*")
        b_div = self.addButton("/")
        b_equal = self.addButton("=")
        b_clear = self.addButton("Clear")
        b_del = self.addButton("Delete")

        rows = [[b7, b8, b9, b_plus],
                [b4, b5, b6, b_minus],
                [b1, b2, b3, b_mult],
                [b_decimal, b0, b_del, b_div]]
        
        r = 1
        for row in rows:
            c = 0
            for btn in row:
                btn.grid(row=r, column=c)
                c += 1
            r +=1
        b_equal.grid(row=r, column=3, columnspan=1)
        b_clear.grid(row=r, column=2, columnspan=1)

    def addButton(self, value):
        return Button(self.master, text=value, width=9, border=3, command = lambda: self.clickButton(value))

    def clickButton(self, value):
        current_equation = self.equation.get()

        if value == "Clear":
            self.equation.delete(0, END)

        elif value == "=":
            try:
                answer = str(eval(current_equation))
                self.equation.delete(0, END)
                self.equation.insert(0, answer)

            except ZeroDivisionError:
                self.equation.delete(0, END)
                self.equation.insert(0, "Cannot divide by zero. Stoooopid!")

            except SyntaxError:
                self.equation.delete(0, END)
                self.equation.insert(0, "Syntax error")

            except Exception as e:
                self.equation.delete(0, END)
                self.equation.insert(0, e)

        elif value == "Delete":
            self.equation.delete(0,END)
            self.equation.insert(0, current_equation[:-1])

        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation+value)

def main():
    root = Tk()
    Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
