from tkinter import *
from tkinter import messagebox

class Barcode:
    def __init__(self):
        mainWindow = Tk() #creates the main window
        mainWindow.title("EAN-13 by Muhammad Sakhran Thayyib // Duden") #sets the main window title
        
        
        LabelIchi = Label(mainWindow, text='Save barcode to PS file [e.g.: EAN13.eps]: ') #creates the first very top label that tells the user to name the barcode file
        LabelIchi.pack() #packs the LabelIchi to the very top
        
        self.EntryBarIchi = Entry(mainWindow) #create the entry bar within the main window
        self.EntryBarIchi.pack() #packs it to the bottom of the LabelIchi
        self.EntryBarIchi.bind('<Return>', self.GetEntryBarIchi) #binds the 'Enter' key to the command that gets the value of EntryBarIchi
        
        LabelNi = Label(mainWindow, text='Enter code (first 12 decimal digits): ' ) #2nd label that tells the user to enter the code of the barcode
        LabelNi.pack() #packs it to the bottom of the first entry bar
        
        self.EntryBarNi = Entry(mainWindow) # creates another Entry bar for the barcode decimals
        self.EntryBarNi.pack() #packs it to the bottom of the label
        self.EntryBarNi.bind('<Return>', self.ChangeR) #binds the 'Enter' key to the command that gets the value of EntryBarNi
        
        mainCanvas = Canvas(mainWindow, bg='white') #creates a canvas with a white background, with its default size as 300x150
        mainCanvas.pack() #packs it so its below everything

        defCanvasWidth = mainCanvas.winfo_reqwidth()
        defCanvasWidthStart = (defCanvasWidth-190)/2
        defCanvasWidthStop = (defCanvasWidth-defCanvasWidthStart)

        defCanvasHeight = mainCanvas.winfo_reqheight()
        defCanvasHeightStart = (defCanvasHeight-190)/2
        
        self.EncodingF6Dict = {
            '0':'LLLLLL',
            '1':'LLGLGG',
            '2':'LLGGLG',
            '3':'LLGGGL',
            '4':'LGLLGG',
            '5':'LGGLLG',
            '6':'LGGGLL',
            '7':'LGLGLG',
            '8':'LGLGGL',
            '9':'LGGLGL'
            }
        
        self.EncodingRDict = {
            '0':'1110010',
            '1':'1100110',
            '2':'1101100',
            '3':'1000010',
            '4':'1011100',
            '5':'1001110',
            '6':'1010000',
            '7':'1000100',
            '8':'1001000',
            '9':'1110100'
            }

        mainCanvas.create_text(defCanvasWidth/2, (defCanvasHeight/4)-20, fill='black', text='EAN-13 Barcode:', font='Times 12 bold')
        #101 First
        mainCanvas.create_line(defCanvasWidthStart,defCanvasHeight/4,defCanvasWidthStart,(defCanvasHeight/4)+95, width=2, fill='green')
        mainCanvas.create_line(defCanvasWidthStart+4,defCanvasHeight/4,defCanvasWidthStart+4,(defCanvasHeight/4)+95, width=2, fill='green')

        # #01010 Middle
        mainCanvas.create_line(defCanvasWidthStart+90,defCanvasHeight/4,defCanvasWidthStart+90,(defCanvasHeight/4)+95, width=2, fill='red') #0
        mainCanvas.create_line(defCanvasWidthStart+92,defCanvasHeight/4,defCanvasWidthStart+92,(defCanvasHeight/4)+95, width=2, fill='green') #1
        mainCanvas.create_line(defCanvasWidthStart+94,defCanvasHeight/4,defCanvasWidthStart+94,(defCanvasHeight/4)+95, width=2, fill='red') #0
        mainCanvas.create_line(defCanvasWidthStart+96,defCanvasHeight/4,defCanvasWidthStart+96,(defCanvasHeight/4)+95, width=2, fill='green') #1
        mainCanvas.create_line(defCanvasWidthStart+98,defCanvasHeight/4,defCanvasWidthStart+98,(defCanvasHeight/4)+95, width=2, fill='red') #0

        # #101 Last
        mainCanvas.create_line(defCanvasWidthStart+184,defCanvasHeight/4,defCanvasWidthStart+184,(defCanvasHeight/4)+95, width=2, fill='green')
        mainCanvas.create_line(defCanvasWidthStart+186,defCanvasHeight/4,defCanvasWidthStart+186,(defCanvasHeight/4)+95, width=2, fill='green')
        mainCanvas.create_line(defCanvasWidthStart+188,defCanvasHeight/4,defCanvasWidthStart+188,(defCanvasHeight/4)+95, width=2, fill='green')

        
        mainWindow.mainloop() #executes what we wish to execute in an application
    
    def GetEntryBarIchi(self, *args): #method that gets the value of the EntryBarIchi
        ValEBI = self.EntryBarIchi.get()
        print(ValEBI)
    
    def GetEntryBarNi(self, *args): #method that gets the value of the EntryBarNi
        try: #method that makes sure that the entered numbers are proper
            if len(str(self.EntryBarNi.get())) != 12: #it has to be exactly 12 in length
                raise ValueError #or it will pop up an error message
            else: #if its 12 in length, then it'll run these
                self.entryData = str(self.EntryBarNi.get())
                print(int(self.EntryBarNi.get()))
                print(list(str(self.EntryBarNi.get())))
            
        except ValueError: #if its not an integer, then an error will pop up in accordance to the ValueError
            messagebox.showerror('Wrong Input!', 'Please enter correct input code')
            
    def CheckSum(self): #Function that calculates the checksum
        self.listedEntryData = list(self.entryData) #lists the entry
        positionCounter = 0 #counter positions
        evenSum = 0 # initial number for the even sum to be added later on
        oddSum = 0 #multiply oddSum by 3 later
        for x in self.listedEntryData: #for x in entrydata
            if positionCounter%2 == 0: #if the position is even
                evenSum += int(x) #add that to even sum
                positionCounter += 1 #add the position counter by 1 to move it forward
            else: #otherwise, if odd
                oddSum += int(x) #add said number to the oddsum
                positionCounter += 1 #add the position counter by 1 to move it forward
        self.checkSumValue = ((oddSum*3)+(evenSum))%10 #counts what will be the checksum in accordance to oddsum and even sum
        if self.checkSumValue != 0:
            self.checkSumValue = 10 - self.checkSumValue
        else:
            self.checkSumValue = self.checkSumValue
        self.listedEntryData.append(str(self.checkSumValue)) #adds the checksum number to the end of the entry data
        self.newEntryData = str(self.listedEntryData) #reconverts it into a string
        
    def ChangeR(self, *args):
        self.RnewEntryDataListed = list(self.newEntryData)
        self.RnewEntryDataListedSnicked = self.listedEntryData[7:]
        self.ConvertedR = []
        print(self.RnewEntryDataListedSnicked)
        for R in self.listedEntryData:
            R = self.EncodingRDict[R]
            self.ConvertedR.append(R)
        print('The original numbers are: ', self.entryData)
        print('The check digit was: ', self.checkSumValue)
        print('After added check digit: ', self.listedEntryData)
        print('The R digits are: ', self.RnewEntryDataListedSnicked)
        print('The Converted list is', self.ConvertedR)




Barcode()
