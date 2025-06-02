# main.py
import tkinter as tk
from controller import CalculatorController

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorController(root)
    root.mainloop()
