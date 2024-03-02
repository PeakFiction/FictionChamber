from tkinter import *

class CanvasDemo:
    def __init__(self):
        mainWindow = Tk()
        mainWindow.geometry("500x500")
        myCanvas = Canvas(mainWindow, bg='white')
        myCanvas.pack()
        
        TestLine = myCanvas.create_line(250, 250, 300, 300, fill='green', width=5)
        
        
        
        mainWindow.mainloop()


CanvasDemo()