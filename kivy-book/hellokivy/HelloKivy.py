#filename: HelloKivy.py
#python HelloKivy.py --size=250x150
#Kivy API: http://kivy.org/docs/api-kivy.html
import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget

#tThis is a pass through 'Weidget' I define in the HellowKivy.kv file
class MyWidget(Widget):
    pass

#this class returns the custom Widgets I defined in MyWidget class
class HelloKivyApp(App):
    def build(self):
        return MyWidget()
#this starts the App
if __name__=="__main__":
    HelloKivyApp().run()
