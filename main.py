from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re
import sys


class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = "0"

    def button_value(self, value):
        if "error in evaluation" in (prev_number := self.ids.input_box.text):
            prev_number = ""

        if prev_number == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{value}"

        else:
            self.ids.input_box.text = f"{prev_number}{value}"

    def sings(self, sing):
        self.ids.input_box.text = f"{self.ids.input_box.text}{sing}"

    def remove_last(self):
        self.ids.input_box.text = self.ids.input_box.text[:-1]

    def results(self):
        try:
            self.ids.input_box.text = str(eval(self.ids.input_box.text))
        except ZeroDivisionError:
            self.ids.input_box.text = "0"
        except (SyntaxError, NameError):
            self.ids.input_box.text = "error in evaluation"
        except Exception as e:
            e = sys.exc_info()
            print(e)

    def positive_number(self):
        if "-" in (prev_number := self.ids.input_box.text):
            self.ids.input_box.text = f'{prev_number.replace("-", "")}'

        else:
            self.ids.input_box.text = f"-{prev_number}"

    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", prev_number)
        if (
            "+" in prev_number
            or "*" not in prev_number
            or "-" not in prev_number
            or "/" not in prev_number
            or "%" not in prev_number
        ) and "." not in num_list[-1]:
            self.ids.input_box.text = f"{prev_number}."
        if "." in prev_number:
            pass
        else:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    builder = Builder.load_file("./main.kv")
    CalculatorApp().run()
