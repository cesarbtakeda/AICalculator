import tkinter as tk
from tkinter import messagebox
import sympy as sp

class CalculadoraCientificaIA:
    def __init__(self, root):  
        self.root = root
        self.root.title("Calculadora Científica com IA")
        self.root.geometry("500x600")

        self.equation = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.equation, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
        entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^', 5, 2), ('ln', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('π', 6, 3),
            ('exp', 7, 0), ('lim', 7, 1), ('∫', 7, 2), ('d/dx', 7, 3),
            ('solve', 8, 0), ('simplify', 8, 1), ('factor', 8, 2), ('expand', 8, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 15), height=2, width=6, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == "=":
            self.calculate()
        elif button_text == "C":
            self.equation.set("")
        elif button_text == "√":
            self.equation.set(f"sqrt({self.equation.get()})")
        elif button_text == "^":
            self.equation.set(self.equation.get() + "**")  
        elif button_text == "ln":
            self.equation.set(f"log({self.equation.get()})")
        elif button_text == "π":
            self.equation.set(self.equation.get() + "3.1415926535")
        elif button_text == "exp":
            self.equation.set(f"exp({self.equation.get()})")
        elif button_text == "lim":
            self.equation.set("lim(f(x), x→a)")
        elif button_text == "∫":
            self.equation.set("∫ f(x) dx")
        elif button_text == "d/dx":
            self.equation.set("d/dx f(x)")
        elif button_text == "sin":
            self.equation.set(f"sin({self.equation.get()})")
        elif button_text == "cos":
            self.equation.set(f"cos({self.equation.get()})")
        elif button_text == "tan":
            self.equation.set(f"tan({self.equation.get()})")
        elif button_text in ["solve", "simplify", "factor", "expand"]:
            self.equation.set(button_text + "(" + self.equation.get() + ")")
        else:
            self.equation.set(self.equation.get() + button_text)

    def calculate(self):
        try:
            expression = self.equation.get()

            if "lim" in expression:
                result = self.calculate_limit(expression)
            elif "∫" in expression:
                result = self.calculate_integral(expression)
            elif "d/dx" in expression:
                result = self.calculate_derivative(expression)
            elif "solve" in expression:
                result = self.solve_equation(expression)
            elif "simplify" in expression:
                result = self.simplify_expression(expression)
            elif "factor" in expression:
                result = self.factor_expression(expression)
            elif "expand" in expression:
                result = self.expand_expression(expression)
            else:
                result = sp.sympify(expression)

            self.equation.set(result)
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida")

    def calculate_derivative(self, expr):
        try:
            var = sp.Symbol('x')
            expr = sp.sympify(expr.replace("d/dx ", ""))
            return sp.diff(expr, var)
        except:
            return "Erro"

    def calculate_integral(self, expr):
        try:
            var = sp.Symbol('x')
            expr = sp.sympify(expr.replace("∫ ", "").replace(" dx", ""))
            return sp.integrate(expr, var)
        except:
            return "Erro"

    def calculate_limit(self, expr):
        try:
            var = sp.Symbol('x')
            parts = expr.replace("lim(", "").replace(")", "").split(",")
            func = sp.sympify(parts[0])
            point = sp.sympify(parts[1].split("→")[1])
            return sp.limit(func, var, point)
        except:
            return "Erro"

    def solve_equation(self, expr):
        try:
            expr = expr.replace("solve(", "").replace(")", "")
            eq = sp.sympify(expr)
            var = list(eq.free_symbols)[0]
            return sp.solve(eq, var)
        except:
            return "Erro"

    def simplify_expression(self, expr):
        try:
            expr = expr.replace("simplify(", "").replace(")", "")
            return sp.simplify(sp.sympify(expr))
        except:
            return "Erro"

    def factor_expression(self, expr):
        try:
            expr = expr.replace("factor(", "").replace(")", "")
            return sp.factor(sp.sympify(expr))
        except:
            return "Erro"

    def expand_expression(self, expr):
        try:
            expr = expr.replace("expand(", "").replace(")", "")
            return sp.expand(sp.sympify(expr))
        except:
            return "Erro"

if __name__ == "__main__":  
    root = tk.Tk()
    app = CalculadoraCientificaIA(root)
    root.mainloop()
