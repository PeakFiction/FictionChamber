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
        ButtonTwo = Button(ButtonFrame, text='Test',)
        ButtonTwo.pack()
        
        mainWindow.mainloop()
    
    def LitrePerKm(self):
        self.CarLitre = self.EntryOne.get()
        self.CarRange = self.EntryTwo.get()
        self.LitPerKmResult = self.CarLitre / self.CarRange
        return self.LitPerKmResult
    
    def KmPerLitre(self):
        self.LitrePerKm()
        self.KmPerLitResult = self.CarRange / self.CarLitre
        return self.KmPerLitResult
    
    def AmountLitresNeeded(self):
        self.LitrePerKm()
        self.KmPerLitre()
        self.CarRemainingRange = self.EntryThree.get()
        self.AmountLitNeedResult = self.LitPerKmResult * self.CarRemainingRange
        return self.AmountLitNeedResult
    
    def AmountMoneyNeeded(self):
        self.LitrePerKm()
        self.KmPerLitre()
        self.AmountLitresNeeded
        self.GasPrice = self.EntryFour.get()
        self.AmountMoneyNeedResult = self.AmountLitNeedResult * self.GasPrice
        return self.AmountMoneyNeedResult
    
    def DrawStuff(self):
        self.LitrePerKm()
        self.KmPerLitre()
        self.AmountLitresNeeded()
        self.AmountMoneyNeeded()
        self.MainCanvas.create_text(((self.defCanvasWidth/5)-20), ((self.defCanvasHeight/12)), text=f"Litres/Km: {self.LitPerKmResult} ", fill="black")
        self.MainCanvas.create_text(((self.defCanvasWidth/5)-20), ((self.defCanvasHeight/12)+15), text=f"Km/Litres: {self.KmPerLitResult}", fill="black")
        self.MainCanvas.create_text(((self.defCanvasWidth/5)-3), ((self.defCanvasHeight/12)+30), text=f"Money Needed: {self.AmountMoneyNeedResult}", fill="black")
        self.MainCanvas.create_text(((self.defCanvasWidth/5)-5), ((self.defCanvasHeight/12)+45), text=f"Litres Needed: {self.AmountLitNeedResult}", fill="black")


Tester()