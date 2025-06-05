# view.py
import tkinter as tk

class CalculatorView:
    def __init__(self, parent, controller=None):
        BG_COLOR = "#22252A"
        BTN_COLOR = "#2A2D36"
        BTN_HL_COLOR = "#393e4d"
        FONT = ("Segoe UI", 20)
        DISPLAY_FONT = ("Segoe UI", 36, "bold")

        self.parent = parent
        self.controller = controller
        self.parent.title("Calculator")
        self.parent.configure(bg=BG_COLOR)
        self.parent.geometry("390x530")
        self.parent.resizable(False, False)
        self.parent.bind("<Key>", self.on_key)

        self.display = tk.Entry(parent, font=DISPLAY_FONT, bd=0, bg=BTN_COLOR, fg='white', justify='right', state='readonly', readonlybackground=BG_COLOR)
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
                    parent,
                    text=label,
                    font=FONT,
                    bg=color,
                    fg="white",
                    bd=0,
                    relief="flat",
                    activebackground="#313745",
                    activeforeground="white",
                    command=lambda l=label: self.on_button(l)
                )
                btn.grid(row=r+1, column=c, sticky="nsew", padx=6, pady=6, ipadx=2, ipady=2)
        for i in range(4):
            parent.grid_columnconfigure(i, weight=1)
        for i in range(len(buttons)+1):
            parent.grid_rowconfigure(i, weight=1)

    def on_key(self, event):
        key = event.keysym
        if key in [str(i) for i in range(10)]:
            self.on_button(key)
        elif key == "period" or event.char == '.':
            self.on_button(".")
        elif key == "plus":
            self.on_button("+")
        elif key == "minus":
            self.on_button("−")
        elif key == "asterisk":
            self.on_button("×")
        elif key == "slash":
            self.on_button("÷")
        elif key == "Return":
            self.on_button("=")
        elif key == "BackSpace":
            self.on_button("⌫")
        elif key == "Escape":
            self.on_button("C")

    def on_button(self, label):
        if self.controller:
            self.controller.on_button(label)

    def set_display(self, value):
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(0, str(value))
        self.display.config(state='readonly')

    def get_display(self):
        try:
            return float(self.display.get().replace('−', '-'))
        except ValueError:
            raise ValueError("Invalid input in display")
