from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from math import *

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "."]
        self.functions = {"π": "pi", "√x": "sqrt", "x²": "**2", "x³": "**3", "e": "e",
                          "sin": "sin", "cos": "cos", "tan": "tan", "log": "log10", "ln": "log"}

        self.result = TextInput(
            multiline=False, readonly=True, halign="right", font_size=40)

        layout = GridLayout(cols=4, padding=10, spacing=10)
        layout.add_widget(self.result)

        buttons = [
            "C", "(", ")", "⌫",
            "π", "7", "8", "9",
            "/", "sin", "4", "5",
            "6", "*", "cos", "1",
            "2", "3", "-", "tan",
            "0", ".", "=", "+",
            "log", "ln", "e", "x²",
            "x³", "√x"
        ]

        for button in buttons:
            layout.add_widget(self.create_button(button))

        return layout

    def create_button(self, text):
        return Button(
            text=text,
            font_size=24,
            on_press=self.on_button_press
        )

    def on_button_press(self, instance):
        text = instance.text
        current = self.result.text

        if text == "C":
            self.result.text = ""
        elif text == "⌫":
            self.result.text = current[:-1]
        elif text == "=":
            try:
                expression = current
                for k, v in self.functions.items():
                    expression = expression.replace(k, v)
                expression = expression.replace("√x", "sqrt")
                self.result.text = str(eval(expression))
            except Exception:
                self.result.text = "Erro"
        else:
            self.result.text += text

if __name__ == "__main__":
    CalculatorApp().run()
