import math

class CalculatorModel:
    def __init__(self):
        pass

    def sin(self, value):
        return math.sin(math.radians(value))

    def cos(self, value):
        return math.cos(math.radians(value))

    def tg(self, value):
        return math.tan(math.radians(value))

    def ctg(self, value):
        return 1 / math.tan(math.radians(value))

    def arcsin(self, value):
        return math.degrees(math.asin(value))

    def arccos(self, value):
        return math.degrees(math.acos(value))

    def arctg(self, value):
        return math.degrees(math.atan(value))

    def arcctg(self, value):
        return math.degrees(math.atan(1 / value))

import tkinter as tk

class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.root.title("Тригонометричний калькулятор")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Відображення результату
        result_label = tk.Label(self.root, textvariable=self.result_var, height=2)
        result_label.grid(row=0, column=0, columnspan=4)

        # Поле для введення числа
        self.input_var = tk.StringVar()
        input_entry = tk.Entry(self.root, textvariable=self.input_var, width=20)
        input_entry.grid(row=1, column=0, columnspan=4)

        # Кнопки
        buttons = [
            ('sin', 2, 0), ('cos', 2, 1), ('tg', 2, 2), ('ctg', 2, 3),
            ('arcsin', 3, 0), ('arccos', 3, 1), ('arctg', 3, 2), ('arcctg', 3, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, operation):
        pass

    def set_result(self, result):
        self.result_var.set(result)

    def get_input_value(self):
        # Отримую значення з поля для введення
        try:
            return float(self.input_var.get())
        except ValueError:
            return None

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.on_button_click = self.on_button_click

    def on_button_click(self, operation):
        # Отримую введене значення
        value = self.view.get_input_value()
        if value is None:
            self.view.set_result("Невірне значення!")
            return
        
        try:
            if operation == 'sin':
                result = self.model.sin(value)
            elif operation == 'cos':
                result = self.model.cos(value)
            elif operation == 'tg':
                result = self.model.tg(value)
            elif operation == 'ctg':
                result = self.model.ctg(value)
            elif operation == 'arcsin':
                result = self.model.arcsin(value)
            elif operation == 'arccos':
                result = self.model.arccos(value)
            elif operation == 'arctg':
                result = self.model.arctg(value)
            elif operation == 'arcctg':
                result = self.model.arcctg(value)
            self.view.set_result(result)
        except ValueError:
            self.view.set_result("Помилка при обчисленні")

import tkinter as tk

def main():
    root = tk.Tk()

    model = CalculatorModel()
    view = CalculatorView(root)
    controller = CalculatorController(model, view)

    root.mainloop()

if __name__ == '__main__':
    main()
