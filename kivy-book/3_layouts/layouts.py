import kivy
kivy.require('1.9.0')

from kivy.app import App 
from kivy.uix.label import Label


class LayoutsApp(App):
    def build(self):
        return Label()

if __name__=="__main__":
    LayoutsApp().run()