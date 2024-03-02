from tkinter import *

class GUICounter:
    def __init__(self):
        window = Tk()
        self.count = 0

        self.display = Label(master = window, text="0")
        btincrement = Button(window, text='Increment', fg='black', bg='#00FFFF', command=self.increment)
        btdecrement = Button(window, text='Decrement', fg='black', bg='Yellow', command=self.decrement)
        btreset = Button(window, text='Reset', fg='black', bg='blue', command=self.reset)
        self.display.pack()
        btincrement.pack()
        btdecrement.pack()
        btreset.pack()
        window.mainloop()
    
    def increment(self):
        self.count+=1
        self.display['text'] = self.count
    def decrement(self):
        self.count-=1
        self.display['text'] = self.count
    def reset(self):
        self.count = 0
        self.display['text'] = self.count


GUICounter()
