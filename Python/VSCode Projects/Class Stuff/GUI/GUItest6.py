from tkinter import *


class Counter:
    def __init__(self):
        mainWindow = Tk()
        mainWindow.title('Increment/Decrement Counter')
        self.Counter = 0
        
        idImage = PhotoImage(mainWindow, file = "Flag_of_Indonesia.svg.gif")
        idImage.pack()
        
        self.mainLabel = Label(mainWindow, text=self.Counter)
        self.mainLabel.pack()
        
        IncrementButton = Button(mainWindow, text='Increment', fg='black', bg='blue', command=self.Increment)
        IncrementButton.pack()
        
        DecrementButton = Button(mainWindow, text='Decrement', fg='Black', bg='Yellow', command=self.Decrement)
        DecrementButton.pack()
        
        ResetButton = Button(mainWindow, text='Reset', fg='black', bg='Red', command=self.Reset)
        ResetButton.pack()
        
        mainWindow.mainloop()
    
    def Increment(self):
        self.Counter = self.Counter + 1
        self.mainLabel['text'] = self.Counter
        
        
    def Decrement(self):
        self.Counter = self.Counter - 1
        self.mainLabel['text'] = self.Counter
    
    def Reset(self):
        self.Counter = 0
        self.mainLabel['text'] = self.Counter



Counter()