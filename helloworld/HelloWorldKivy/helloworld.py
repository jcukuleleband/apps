from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty

class GameScreen(GridLayout):

    reset_button = None
    cntDownClock = None

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.cols = 1

        #Reset button
        green = [0, 1, 0, 1]
        self.reset_button =  Button(text ="Reset", background_color = green)
        self.reset_button.bind(on_press = self.reset_button_callback)
        self.add_widget(self.reset_button)

        self.cntDownClock = IncrediblyCrudeClock()
        self.cntDownClock.start()
        self.add_widget(self.cntDownClock)


    def reset_button_callback(self, event):
        print("reset_button_callback")
        self.remove_widget(self.cntDownClock)
        self.cntDownClock = IncrediblyCrudeClock();
        self.cntDownClock.start();
        self.add_widget(self.cntDownClock)

class IncrediblyCrudeClock(Label):
    a = NumericProperty(5)  # seconds

    def start(self):
        print("ICC:start")
        print(self)
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def on_a(self, instance, value):
        self.text = str(round(value, 1))


class MyApp(App):

    def build(self):
        return GameScreen()

if __name__ == '__main__':
    MyApp().run()
