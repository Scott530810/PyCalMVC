import tkinter as tk
import math

# ---------- Model ----------
class CalculatorModel:
    def __init__(self):
        self.memory = 0
        self.reset_all()

    def reset_all(self):
        self.stored_value = None
        self.operator = None
        self.just_calculated = False

    def operate(self, left, right, op):
        try:
            if op == '+':
                return left + right
            elif op == '−':
                return left - right
            elif op == '×':
                return left * right
            elif op == '÷':
                if right == 0:
                    raise ZeroDivisionError
                return left / right
        except ZeroDivisionError:
            return 'Error'
        except Exception:
            return 'Error'

    # 其它進階運算
    def reciprocal(self, val):
        try:
            return 1 / val
        except ZeroDivisionError:
            return 'Error'
    def square(self, val):
        return val ** 2
    def sqrt(self, val):
        return math.sqrt(val) if val >= 0 else 'Error'
    def percent(self, val):
        return val / 100
    def plus_minus(self, val):
        return -val

# ---------- View ----------
class CalculatorView:
    def __init__(self, root, controller):
        BG_COLOR = "#22252A"
        BTN_COLOR = "#2A2D36"
        BTN_HL_COLOR = "#393e4d"
        FONT = ("Segoe UI", 20)
        DISPLAY_FONT = ("Segoe UI", 36, "bold")

        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("390x530")
        self.root.resizable(False, False)

        self.display = tk.Entry(root, font=DISPLAY_FONT, bd=0, bg=BTN_COLOR, fg='white', justify='right')
        self.display.insert(0, '0')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=(16,10), ipady=14)

        buttons = [
            ['MC', 'MR', 'M+', 'M-'],
            ['%', 'CE', 'C', '⌫'],
            ['1/x', 'x²', '²√x', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['+/−', '0', '.', '=']
        ]
        hl_btns = {'CE', 'C', '='}
        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                color = BTN_HL_COLOR if label in hl_btns else BTN_COLOR
                btn = tk.Button(
                    root,
                    text=label,
                    font=FONT,
                    bg=color,
                    fg="white",
                    bd=0,
                    relief="flat",
                    activebackground="#313745",
                    activeforeground="white",
                    command=lambda l=label: controller.on_button(l)
                )
                btn.grid(row=r+1, column=c, sticky="nsew", padx=6, pady=6, ipadx=2, ipady=2)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(len(buttons)+1):
            root.grid_rowconfigure(i, weight=1)

    def set_display(self, value):
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        self.display.delete(0, tk.END)
        self.display.insert(0, str(value))

    def get_display(self):
        try:
            return float(self.display.get().replace('−', '-'))
        except ValueError:
            return 0

# ---------- Controller ----------
class CalculatorController:
    def __init__(self, root):
        self.model = CalculatorModel()
        self.view = CalculatorView(root, self)
        self.reset_next = False

    def on_button(self, label):
        if label in '0123456789':
            if self.view.display.get() == '0' or self.reset_next:
                self.view.set_display(label)
                self.reset_next = False
            else:
                self.view.set_display(self.view.display.get() + label)
            self.model.just_calculated = False

        elif label == '.':
            if '.' not in self.view.display.get():
                self.view.set_display(self.view.display.get() + '.')
            self.model.just_calculated = False

        elif label in ['+', '−', '×', '÷']:
            self.input_operator(label)

        elif label == '=':
            self.calculate()
            self.model.operator = None
            self.model.stored_value = None
            self.model.just_calculated = True

        elif label == 'C':
            self.view.set_display('0')
            self.model.reset_all()
            self.reset_next = False

        elif label == 'CE':
            self.view.set_display('0')

        elif label == '⌫':
            text = self.view.display.get()
            if len(text) > 1:
                self.view.set_display(text[:-1])
            else:
                self.view.set_display('0')

        elif label == '+/−':
            value = self.view.get_display()
            self.view.set_display(self.model.plus_minus(value))

        elif label == '%':
            value = self.view.get_display()
            self.view.set_display(self.model.percent(value))

        elif label == '1/x':
            value = self.view.get_display()
            self.view.set_display(self.model.reciprocal(value))

        elif label == 'x²':
            value = self.view.get_display()
            self.view.set_display(self.model.square(value))

        elif label == '²√x':
            value = self.view.get_display()
            self.view.set_display(self.model.sqrt(value))

        elif label == 'MC':
            self.model.memory = 0

        elif label == 'MR':
            self.view.set_display(self.model.memory)
            self.reset_next = True

        elif label == 'M+':
            self.model.memory += self.view.get_display()

        elif label == 'M-':
            self.model.memory -= self.view.get_display()

    def input_operator(self, op):
        curr_val = self.view.get_display()
        if self.model.operator and not self.reset_next:
            # 即時運算模式
            self.model.stored_value = self.model.operate(self.model.stored_value, curr_val, self.model.operator)
            self.view.set_display(self.model.stored_value)
        else:
            self.model.stored_value = curr_val
        self.model.operator = op
        self.reset_next = True
        self.model.just_calculated = False

    def calculate(self):
        if self.model.operator is not None and self.model.stored_value is not None:
            curr_val = self.view.get_display()
            result = self.model.operate(self.model.stored_value, curr_val, self.model.operator)
            self.view.set_display(result)
            self.model.stored_value = result
            self.reset_next = True
            self.model.just_calculated = True

# ---------- main ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorController(root)
    root.mainloop()
