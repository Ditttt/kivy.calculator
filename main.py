from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
import re
import sys
import traceback


class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = "0"

    def button_value(self, value):
        if "error in evaluation" in self.ids.input_box.text:
            self.ids.input_box.text = ""

        self.ids.input_box.text, self.ids.input_box.text = (
            "",
            f"{value}"
            if self.ids.input_box.text == "0"
            else f"{self.ids.input_box.text}{value}",
        )

    def sings(self, sing):
        print(self.ids.input_box.text[0])
        if self.ids.input_box.text[0] == '0':
            self.ids.input_box.text = f"0"
            return
        print(self.ids.input_box.text[-1])
        print(sing)
        if self.ids.input_box.text[-1] == sing or self.ids.input_box.text[-1] == '÷':
            return
        self.ids.input_box.text = f"{self.ids.input_box.text}{sing}"
        if "/" in self.ids.input_box.text:
            self.ids.input_box.text = f"{self.ids.input_box.text.replace('/', '÷')}"

    def remove_last(self):
        self.ids.input_box.text = self.ids.input_box.text[:-1]
        self.ids.input_box.text = (
            "0" if self.ids.input_box.text == "" else self.ids.input_box.text
        )

    def results(self):
        try:
            res = list(self.ids.input_box.text)
            indx = 0
            for i in res:
                if res[indx] == "÷":
                    res[indx] = "/"
                indx += 1
            if self.ids.input_box.text[-1] in ["+", "-", "*", "÷", "%"]:
                return
            self.ids.input_box.text = str(eval("".join(res)))
            koma = self.ids.input_box.text
            if koma[-1] == "0" and koma[-2] == ".":
                self.ids.input_box.text = koma[0 : len(koma) - 2]
        except ZeroDivisionError:
            self.ids.input_box.text = "0"
        except (SyntaxError, NameError):
            self.ids.input_box.text = "error in evaluation"
        except Exception:
            traceback.print_exc()

    def positive_number(self):
        if "-" in self.ids.input_box.text:
            self.ids.input_box.text = f'{self.ids.input_box.text.replace("-", "")}'

        else:
            self.ids.input_box.text = f"-{self.ids.input_box.text}"

    def dot(self):
        num_list = re.split("\+|\*|-|/|%", self.ids.input_box.text)
        if (
            "+" in self.ids.input_box.text
            or "*" not in self.ids.input_box.text
            or "-" not in self.ids.input_box.text
            or "/" not in self.ids.input_box.text
            or "%" not in self.ids.input_box.text
        ) and "." not in num_list[-1]:
            self.ids.input_box.text = f"{self.ids.input_box.text}."
        if "." in self.ids.input_box.text:
            pass
        else:
            prev_number = f"{self.ids.input_box.text}."
            self.ids.input_box.text = prev_number


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    builder = Builder.load_file("./main.kv")
    CalculatorApp().run()
