from tkinter import *

class Tester:
    def __init__(self):
        mainWindow = Tk()
        TopFrame = Frame(mainWindow)
        TopFrame.pack()
        
        BottomFrame = Frame(mainWindow)
        BottomFrame.pack()
        
        ##Entry Frame
        EntryFrame = Frame(TopFrame)
        EntryFrame.pack(side=LEFT)
        
        EntryOneFrame = Frame(EntryFrame)
        EntryOneFrame.pack()
        EntryOneText = Label(EntryOneFrame, text='Gas Tank Volume')
        EntryOneText.pack(side=LEFT)
        self.EntryOne = Entry(EntryOneFrame)
        self.EntryOne.pack(side=LEFT)
        
        EntryTwoFrame = Frame(EntryFrame)
        EntryTwoFrame.pack()
        EntryTwoText = Label(EntryTwoFrame, text="Car's Maximum Range")
        EntryTwoText.pack(side=LEFT)
        self.EntryTwo = Entry(EntryTwoFrame)
        self.EntryTwo.pack(side=LEFT)
        
        EntryThreeFrame = Frame(EntryFrame)
        EntryThreeFrame.pack()
        EntryThreeText = Label(EntryThreeFrame, text="Car's Remaining Range")
        EntryThreeText.pack(side=LEFT)
        self.EntryThree = Entry(EntryThreeFrame)
        self.EntryThree.pack(side=LEFT)
        
        EntryFourFrame = Frame(EntryFrame)
        EntryFourFrame.pack()
        EntryFourText = Label(EntryFourFrame, text='Price of Gas Per Litre')
        EntryFourText.pack(side=LEFT)
        self.EntryFour = Entry(EntryFourFrame)
        self.EntryFour.pack(side=LEFT)
        
        ##Canvas Frame##
        CanvasFrame = Frame(TopFrame)
        CanvasFrame.pack(side=LEFT)
        
        
        self.MainCanvas = Canvas(CanvasFrame, bg='white')
        self.MainCanvas.pack()
        self.defCanvasHeight = self.MainCanvas.winfo_reqheight()
        self.textHeight = self.defCanvasHeight/6
        self.defCanvasWidth = self.MainCanvas.winfo_reqwidth()
        self.textWidth = self.defCanvasWidth/6
        
        
        ##Button Frame ##
        ButtonFrame = Frame(mainWindow)
        ButtonFrame.pack()
        
        ButtonOne = Button(ButtonFrame, text='Calculate', command=self.DrawStuff)
        ButtonOne.pack()
        
        mainWindow.mainloop()
        
        