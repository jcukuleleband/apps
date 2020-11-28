#filename: HelloKivy.py
#python HelloKivy.py --size=250x150
#Kivy API: http://kivy.org/docs/api-kivy.html
import kivy

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

#fun fact: The Kv File must be named in lower case the naem of the app class without the "app" part -so dumb
#Kivy looks for a Kv file with the same name as your App class in lowercase, minus “App” if it ends with ‘App’ e.g:
#MyApp -> my.kv
#https://kivy.org/doc/stable/guide/lang.html
