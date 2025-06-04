# model.py
import math

class CalculatorModel:
    """Model for a simple calculator supporting basic arithmetic operations."""
    def __init__(self):
        self.memory = 0
        self.reset_all()

    def reset_all(self):
        self.stored_value = None
        self.operator = None
        self.just_calculated = False

    def operate(self, left, right, op):
        try:
            left, right = float(left), float(right)
            ops = {
                '+': lambda a, b: a + b,
                '−': lambda a, b: a - b,
                '×': lambda a, b: a * b,
                '÷': lambda a, b: a / b,
            }
            return ops[op](left, right)
        except Exception:
            return 'Error'

    def reciprocal(self, val):
        try:
            return 1 / float(val)
        except Exception:
            return 'Error'
    def square(self, val):
        try:
            return float(val) ** 2
        except Exception:
            return 'Error'
    def sqrt(self, val):
        try:
            val = float(val)
            return math.sqrt(val) if val >= 0 else 'Error'
        except Exception:
            return 'Error'
    def percent(self, val):
        try:
            return float(val) / 100
        except Exception:
            return 'Error'
    def plus_minus(self, val):
        try:
            return -float(val)
        except Exception:
            return 'Error'
