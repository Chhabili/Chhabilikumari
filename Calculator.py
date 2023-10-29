from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
# set the app size
Window.size = (400, 600)

# design Our .kv design file
Builder.load_file("calculator.kv")

class Calculator(Widget):
    # create the function clear the all character:
    def clear(self):
        self.ids.calculator.text = '0'

    # create a button pressing function
    def button_press(self, button):
        # create aa variable that contains
        prior = self.ids.calculator.text
        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calculator.text = ''
            self.ids.calculator.text = f'{button}'
        else:
            self.ids.calculator.text = f'{prior}{button}'

    # create decimal function
    def dot(self):
        prior = self.ids.calculator.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calculator.text = prior

        elif "." in prior:
            pass
        else:

            prior = f'{prior}.'
            self.ids.calculator.text = prior

    # create the function to add, subtract, multiply and divide numbers
    def math_sign(self, sign):
        prior = self.ids.calculator.text

        self.ids.calculator.text = f'{prior}{sign}'

    # create function remove the last character
    def remove(self):
        prior = self.ids.calculator.text
        prior = prior[:-1]
        self.ids.calculator.text = prior

    # create equal to function
    def equals(self):
        prior = self.ids.calculator.text
        try:
            # evaluate the math from the text box
            answer = eval(prior)
            # output the answer
            self.ids.calculator.text = str(answer)
        except:
            # given the output is indefinite show the error
            self.ids.calculator.text = "error"
class MyFirstCalculator(App):
    def build(self):
        return Calculator()


MyFirstCalculator().run()
