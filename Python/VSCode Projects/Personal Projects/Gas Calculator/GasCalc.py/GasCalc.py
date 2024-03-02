from tkinter import *

class GasCalc:
    def __init__(self):
        mainWindow = Tk()
        
        TopFrame = Frame(mainWindow)
        TopFrame.pack()
        
        BottomFrame = Frame(mainWindow)
        BottomFrame.pack()
        ## Left Side Frame ##
        
        mainLeftFrame = Frame(TopFrame)
        mainLeftFrame.pack(side=LEFT)
        
        GasTankVolumeFrame = Frame(mainLeftFrame)
        GasTankVolumeFrame.pack(anchor=E)
        GasTankVolumeText = Label(GasTankVolumeFrame, text='Gas Tank Volume: ')
        GasTankVolumeText.pack(side=LEFT, expand=True, anchor=N)
        self.GasTankVolumeEntry = Entry(GasTankVolumeFrame)
        self.GasTankVolumeEntry.pack(side=LEFT, expand=True, anchor=N)
        
        CarsRemainingRangeFrame = Frame(mainLeftFrame)
        CarsRemainingRangeFrame.pack(side=BOTTOM, anchor=E)
        CarsRemainingRangeText = Label(CarsRemainingRangeFrame, text="Car's Remaining Range: ")
        CarsRemainingRangeText.pack(side=LEFT,expand=True, anchor=N)
        self.CarsRemainingRangeEntry = Entry(CarsRemainingRangeFrame)
        self.CarsRemainingRangeEntry.pack(side=LEFT, expand=True, anchor=E)
        
        CarsMaximumRangeFrame = Frame(mainLeftFrame)
        CarsMaximumRangeFrame.pack(side=BOTTOM, anchor=E)
        CarsMaximumRangeText = Label(CarsMaximumRangeFrame, text="Car's Maximum Range: ")
        CarsMaximumRangeText.pack(side=LEFT,expand=True, anchor=N)
        self.CarsMaximumRangeEntry = Entry(CarsMaximumRangeFrame)
        self.CarsMaximumRangeEntry.pack(side=LEFT, expand=True, anchor=E)
        
        GasPricePerLitreFrame = Frame(mainLeftFrame)
        GasPricePerLitreFrame.pack(side=BOTTOM, anchor=E)
        GasPricePerLitreText = Label(GasPricePerLitreFrame, text='Gas Price Per Litre: ')
        GasPricePerLitreText.pack(side=LEFT,expand=True, anchor=N)
        self.GasPricePerLitreEntry = Entry(GasPricePerLitreFrame)
        self.GasPricePerLitreEntry.pack(side=LEFT, expand=True, anchor=E)
        
        ##Bottom Button Frame
        
        ButtonFrame = Frame(BottomFrame)
        ButtonFrame.pack(side=BOTTOM)
        
        self.litPerKmButton 		= Button(ButtonFrame, text='Calculate Lit/Km', command=self.DrawStuff)
        self.litPerKmButton.pack(side=LEFT)
        self.kmPerlitButton 		= Button(ButtonFrame, text='Calculate Km/Lit', command=self.DrawStuff)
        self.kmPerlitButton.pack(side=LEFT)
        self.litresNeedButton 		= Button(ButtonFrame, text='Calculate Litres', command=self.DrawStuff)
        self.litresNeedButton.pack(side=LEFT)
        self.moneyNeedButton 	    = Button(ButtonFrame, text='Calculate Price', command=self.DrawStuff)
        self.moneyNeedButton.pack(side=LEFT)
        
        ## Right Side Frame ##
        CanvasFrame = Frame(TopFrame)
        CanvasFrame.pack(side=LEFT)
        self.mainCanvas = Canvas(CanvasFrame, bg='white')
        self.mainCanvas.pack()
        self.defCanvasHeight = self.mainCanvas.winfo_reqheight()
        self.textHeight = self.defCanvasHeight/6
        self.defCanvasWidth = self.mainCanvas.winfo_reqwidth()
        self.textWidth = self.defCanvasWidth/6
        
        
        mainWindow.mainloop()
    
    ## Calculation Functions ##
    
    ## Calculate Litres Per Kilometre
    def litPerKm(self):
        self.LitresPerKm = int(self.GasTankVolumeEntry.get())
        self.MaxRange = int(self.CarsMaximumRangeEntry.get())
        self.litPerKmResult = self.LitresPerKm / self.MaxRange
        self.litPerKmResultInted = int(self.litPerKmResult)
        return self.litPerKmResultInted
    
    ## Calculate Kilometres Per Litre
    def kmPerlit(self):
        self.litPerKm()
        self.kmPerlitResult = self.MaxRange / self.LitresPerKm
        self.kmPerlitResultInted = int(self.kmPerlitResult)
        return self.kmPerlitResultInted
    
    ## Calculate the Amount of Litres Needed
    def litresNeed(self):
        self.litPerKm()
        self.kmPerlit()
        self.RemainingRange = int(self.CarsRemainingRangeEntry.get())
        self.litresNeedResult = self.litPerKmResult * self.RemainingRange
        self.litresNeedResultInted = int(self.litresNeedResult)
        return self.litresNeedResultInted
    
    ## Calculate the Amount of Money Needed
    def moneyNeed(self):
        self.litPerKm()
        self.kmPerlit()
        self.litresNeed()
        self.GasPrice = int(self.GasPricePerLitreEntry.get())
        self.amountOfMoneyNeeded = self.litresNeedResult * self.GasPrice
        self.amountOfMoneyNeededInted = int(self.amountOfMoneyNeeded)
        return self.amountOfMoneyNeededInted
    
    def DrawStuff(self):
        self.litPerKm()
        self.kmPerlit()
        self.litresNeed()
        self.moneyNeed()
        self.mainCanvas.create_text(((self.defCanvasWidth/5)-10), ((self.defCanvasHeight/12)), text=f"Litres/Km: {self.litPerKmResult} ", fill="black")
        self.mainCanvas.create_text(((self.defCanvasWidth/5)-10), ((self.defCanvasHeight/12)+15), text=f"Km/Litres: {self.kmPerlitResult}", fill="black")
        self.mainCanvas.create_text(((self.defCanvasWidth/5)), ((self.defCanvasHeight/12)+30), text=f"Money Needed: {self.litresNeedResult}", fill="black")
        self.mainCanvas.create_text(((self.defCanvasWidth/5)), ((self.defCanvasHeight/12)+45), text=f"Litres Needed: {self.litresNeedResult}", fill="black")


GasCalc()