# controller.py

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
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
