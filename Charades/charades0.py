#DUMB SIMPLE POORLY PROGRAMMED CHARARD Generator
#TODO:Needs event handling and error handling along
#TODO:NEEDS REAL TIMER
#TODO:NEEDS SOUNDS FOR START, END, END Round
#POTENTIAL FUTURE UPDATES: SCORE KEEPER???

from tkinter import Tk, Label, Button, Text
import time
import winsound
from LoadCharadeWords import LoadCharadeWords
import random

class CharadesUI:
    charade_list = []

    def __init__(self, master):
        self.play = False
        self.master = master
        master.title("Simple Charades")

        self.label = Label(master, text="Simple Charades Generator")
        self.label.pack()

        self.next_button = Button(master, text="Next Charade Word", command=self.Next, width=50, height=5)
        self.next_button.pack()

        self.start_button = Button(master, text="Start Timer", command=self.Start, width=50, height=5)
        self.start_button.pack()

        self.charade_word = Label(master, text="Press Next Charade Word, Then Start to Begin", fg = "red", width=50, height=10)
        self.charade_word.pack()

        self.timer_display = Label(master, text="45", width=50, height=10)
        self.timer_display.pack()

        self.end_round_button = Button(master, text="End Round", command=self.EndRound, width=50, height=5)
        self.end_round_button.pack()

    def Next(self):

        self.charade_word.config(text=self.ReturnRandomCharadeWord())
        self.charade_word.update()

        #reset display timer
        self.timer_display.config(fg = "black",text="45")
        self.timer_display.update()
        self.play = True

    def Start(self):
        if (self.play==True):
            for x in range(1, 46):
                self.timer_display.config(fg="black",text=46-x)
                self.timer_display.update()
                if(self.play==False):
                    break
                time.sleep(1)

            if(self.play==False):
                self.timer_display.config(fg = "Green",text="Round Ended")
                self.timer_display.update()
            else:
                self.Beep()
                self.timer_display.config(fg = "red",text="TIMES UP")
                self.timer_display.update()

    def EndRound(self):
        self.play = False
        print ("Round Over")

    def Beep(self):
        frequency = 500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

    def SetWordList(self, words):
        self.charade_list = words

    def ReturnRandomCharadeWord(self):
        return random.choice(self.charade_list)


root = Tk()
charade_words = ""
charadeWords = LoadCharadeWords()
charadeWords.setDataLocation("data.txt")
charade_words = charadeWords.getCharadeWords()
my_gui = CharadesUI(root)
my_gui.SetWordList(charade_words)
root.mainloop()
