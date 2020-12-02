import kivy
kivy.require('1.10.0')


from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
#todo; Add kivy.garden & possibly MatPlotLib

class XYGraphApp(App):
    def build(self):
        return BoxLayout()

if __name__ == "__main__":
    XYGraphApp().run()