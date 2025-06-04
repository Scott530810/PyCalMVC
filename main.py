# main.py
import tkinter as tk
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

if __name__ == "__main__":
    root = tk.Tk()
    model = CalculatorModel()
    controller = CalculatorController(model, None)
    view = CalculatorView(root, controller)
    controller.view = view
    root.mainloop()
