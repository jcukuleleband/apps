from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.graphics import Color, Rectangle

class GameScreen(GridLayout):

    reset_button = None
    cntDownClock = None

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.cols = 1

        #title
        self.topTitle = TitleLabel()
        self.add_widget(self.topTitle)

        #Timer
        self.cntDownClock = IncrediblyCrudeClock()
        #self.cntDownClock.start()
        self.cntDownClock.text = "Press Start to Begin Charading"
        self.add_widget(self.cntDownClock)

        #barder
        self.border = Border(size = (100,10))
        self.add_widget(self.border)

        #Charade Word
        self.word = CharadeWord(text = "Baseball Player")
        self.add_widget(self.word)

        #Reset button
        green = [0, 1, 0, 1]
        self.start_button =  Button(text ="Start", background_color = green)
        self.start_button.bind(on_press = self.start_button_callback)
        self.add_widget(self.start_button)

    def start_button_callback(self, event):
            print("reset_button_callback")
            self.remove_widget(self.cntDownClock)
            print(self.start_button.text)
            if self.start_button.text == "Start":
                green = [0, 1, 0, 1]
                self.cntDownClock = IncrediblyCrudeClock();
                self.cntDownClock.start();
                self.add_widget(self.cntDownClock,2)  # "2" form the bottom?
                
                self.start_button.text="Stop"
            else:
                self.cntDownClock = IncrediblyCrudeClock()
                self.cntDownClock.text = "Press Start to Begin Charading"
                self.add_widget(self.cntDownClock, 2)
                self.start_button.text="Start"

class IncrediblyCrudeClock(Label):
    a = NumericProperty(45)

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def on_a(self, instance, value):
        self.text = str(round(value, 1))

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 0, 0, 1)
            Rectangle(pos=self.pos, size=self.size)



class CharadeWord(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 1, 0.5)
            Rectangle(pos=self.pos, size=self.size)

class TitleLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1,1,1,1)
            Rectangle(pos=self.pos, size=self.size)


class Border(Label):

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1,1,0,1)
            Rectangle(pos=self.pos, size=self.size)


class MyApp(App):

    def build(self):
        return GameScreen()

if __name__ == '__main__':
    MyApp().run()
