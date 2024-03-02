from tkinter import *
from tkinter import messagebox

class Test():
    def __init__(self):
        mainWindow = Tk()
        mainLabel = Label(mainWindow, text='Enter: ')
        mainLabel.pack(side=LEFT)

        self.mainEntry = Entry(mainWindow)
        self.mainEntry.bind("<Return>", self.GetEntryBarNi)
        self.mainEntry.pack(side=LEFT)

        mainWindow.mainloop()
        
        
    
    def GetEntryBarNi(self, *args):
        self.ListedEntry = list(str(self.mainEntry.get())) 
        for i in self.ListedEntry:
            if i == '0':
                i == '0001101'
            elif i == '1':
                i == '0011001'
        print(self.ListedEntry)

Test()

