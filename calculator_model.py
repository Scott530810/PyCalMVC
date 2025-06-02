# calculator_model.py
import math

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
