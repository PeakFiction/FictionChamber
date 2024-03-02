from tkinter import *

class Test:
    def __init__(self):
        mainWindow = Tk()
        TopFrame = Frame(mainWindow)
        TopFrame.pack()
        
        BottomFrame = Frame(mainWindow)
        BottomFrame.pack()
        
        canvasOne = Canvas(TopFrame, bg='red')
        canvasOne.pack(side=LEFT)
        
        canvasTwo = Canvas(TopFrame, bg='blue')
        canvasTwo.pack(side=LEFT)
        
        canvasThree = Canvas(BottomFrame, bg='green')
        canvasThree.pack()
        mainWindow.mainloop()


Test()