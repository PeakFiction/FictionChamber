from tkinter import *
import math

class Counter:
    def __init__(self):
        mainWindow = Tk()
        mainWindow.title('Counter')
        self.Counter = 0
        self.r = IntVar()
        self.r.set(1)

        self.mainLabel = Label(mainWindow, text=self.Counter)
        self.mainLabel.pack()

        IncrementButton = Button(mainWindow, text='Increment', bg='blue', fg='white', command=self.Increment)
        IncrementButton.pack()

        DecrementButton = Button(mainWindow, text='Decrement', bg='red', fg='white', command=self.Decrement)
        DecrementButton.pack()
        
        FunnyNumberButton = Button(mainWindow, text='Click for Funny Number', bg='purple', fg='white', command=self.funnyNumber)
        FunnyNumberButton.pack()

        ResetButton = Button(mainWindow, text='Reset', bg='Yellow', fg='Black', command=self.Reset)
        ResetButton.pack()

        self.RadioBTN1 = Radiobutton(mainWindow, text='+1 / -1', variable=self.r, value=1, command= self.integerChange)
        self.RadioBTN1.pack()

        self.RadioBTN2 = Radiobutton(mainWindow, text='+10 / -10', variable=self.r, value=10, command = self.integerChange)
        self.RadioBTN2.pack()

        self.Label1 = Label(mainWindow, text=f"You've picked to add/subtract by {self.r.get()}")
        self.Label1.pack()


        mainWindow.mainloop()
    
    def funnyNumber(self):
        self.Counter = 69
        self.mainLabel['text'] = self.Counter

    def Increment(self):
        self.Counter = self.Counter + self.r.get()
        self.mainLabel['text'] = self.Counter
    
    def Decrement(self):
        self.Counter = self.Counter - self.r.get()
        self.mainLabel['text'] = self.Counter

    def Reset(self):
        self.Counter = 0
        self.mainLabel['text'] = self.Counter

    def integerChange(self):
        self.Label1['text'] = f"You've picked to add/subtract by {self.r.get()}"

Counter()