from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy


class MyRoot(BoxLayout):

    def __int__(self):
        super(MyRoot,self).__init__()

    def calc_symbol(self,symbol):
        self.calc_field.text += symbol

    def clear(self):
        self.calc_field.text=""

    def get_result(self):
        self.calc_field.text= str(eval(self.calc_field.text))

class SimpleCalc(App):

    def build(self):
        return MyRoot()

simplecalc= SimpleCalc()
simplecalc.run()