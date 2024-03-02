from tkinter import *
from tkinter import messagebox

class Barcode:
    def __init__(self):
        mainWindow = Tk() #creates the main window
        mainWindow.title("EAN-13 by Muhammad Sakhran Thayyib // Duden") #sets the main window title
        
        
        LabelIchi = Label(mainWindow, text='Save barcode to PS file [e.g.: EAN13.eps]: ', font = ('Helvetica 12 bold')) #creates the first very top label that tells the user to name the barcode file
        LabelIchi.pack() #packs the LabelIchi to the very top
        
        self.EntryBarIchi = Entry(mainWindow) #create the entry bar within the main window
        self.EntryBarIchi.pack() #packs it to the bottom of the LabelIchi
        self.EntryBarIchi.bind('<Return>', self.GetEntryBarIchi) #binds the 'Enter' key to the command that gets the value of EntryBarIchi
        
        LabelNi = Label(mainWindow, text='Enter code (first 12 decimal digits): ', font = ('Helvetica 12 bold') ) #2nd label that tells the user to enter the code of the barcode
        LabelNi.pack() #packs it to the bottom of the first entry bar
        
        self.EntryBarNi = Entry(mainWindow) # creates another Entry bar for the barcode decimals
        self.EntryBarNi.pack() #packs it to the bottom of the label
        self.EntryBarNi.bind('<Return>', self.DrawBarcode) #binds the 'Enter' key to the command that gets the value of EntryBarNi
        
        self.mainCanvas = Canvas(mainWindow, bg='white') #creates a canvas with a white background, with its default size as 300x150
        self.mainCanvas.pack() #packs it so its below everything

        #gets the value of the width and height based on the default canvas size on the computer
        self.defCanvasWidth = self.mainCanvas.winfo_reqwidth()
        self.defCanvasWidthStart = (self.defCanvasWidth/2) -85
        self.defCanvasWidthStop = (self.defCanvasWidth-self.defCanvasWidthStart)

        self.defCanvasHeight = self.mainCanvas.winfo_reqheight()
        self.defCanvasHeightStart = (self.defCanvasHeight/2)-50
        
        ### BELOW ARE ENCODING DICTIONARIES ### 
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

        self.EncodingGDict = {
            '0':'0100111',
            '1':'0110011',
            '2':'0011011',
            '3':'0100001',
            '4':'0011101',
            '5':'0111001',
            '6':'0000101',
            '7':'0010001',
            '8':'0001001',
            '9':'0010111'
            }
        
        mainWindow.mainloop() #executes what we wish to execute in an application
    
    def GetEntryBarIchi(self, *args): #method that gets the value of the EntryBarIchi
        self.ValEBI = self.EntryBarIchi.get()
        print(self.ValEBI)
    
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
        self.GetEntryBarNi()
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
        
    def ChangeR(self, *args): #Method that Changes the right side into binary
        self.CheckSum()
        self.ChangeL()
        self.RnewEntryDataListed = list(self.newEntryData) #makes it into a list
        self.RnewEntryDataListedSnicked = self.listedEntryData[7:] #and then spliced the last 6
        self.ConvertedR = [] 
        for R in self.RnewEntryDataListedSnicked: #for every element in the spliced list
            R = self.EncodingRDict[R] #refer back to the original dictionary
            self.ConvertedR.append(R) #append it to the list
        ### BELOW ARE FOR CHECKING ###
        print('The original numbers are: ', self.entryData)
        print('The check digit was: ', self.checkSumValue)
        print('After added check digit: ', self.listedEntryData)
        print('The R digits are: ', self.RnewEntryDataListedSnicked)
        print('The Converted R list is', self.ConvertedR)
        print('The Converted L list is', self.ConvertedL)


    def DrawR(self, *args): #method that draws R
        self.ChangeR()
        nextCounter = 100 #sets a position counter for the next lines
        for i in self.ConvertedR: #for every I in the converted R list
            for x in i: #and for every element in I
                if x == '1': #if it's 1, create a purple line
                    self.mainCanvas.create_line(self.defCanvasWidthStart+nextCounter,self.defCanvasHeight/4,self.defCanvasWidthStart+nextCounter,(self.defCanvasHeight/4)+80, width=2, fill='magenta') #1
                    nextCounter = nextCounter + 2
                else:       #if it's 0, create a white line
                    self.mainCanvas.create_line(self.defCanvasWidthStart+nextCounter,self.defCanvasHeight/4,self.defCanvasWidthStart+nextCounter,(self.defCanvasHeight/4)+80, width=2, fill='white') #0
                    nextCounter = nextCounter + 2
    
    def ChangeL(self, *args): #method that changes L into binary
        self.NewL = self.listedEntryData[1:7] #spliced it to get the first 7 without the first digit
        self.LFirstDigit = self.listedEntryData[0] #spliced to get the first digit
        self.ConvertedL = []
        LEncoding = self.EncodingF6Dict[str(self.LFirstDigit)] #find which one to use based on the first digit
        for i in range(6): #for every number in said range
            if LEncoding[i] == 'L': #if assigned is L
                i = self.EncodingRDict[self.NewL[i]] #then use the R dictionary
                self.result = "" #to invert the value
                for y in i:
                    if y=="1":
                        self.result += '0'
                    else:
                        self.result += '1'
            elif LEncoding[i] == 'G': #if assigned is G
                self.result = self.EncodingGDict[self.NewL[i]] #use the G dictionary to change it 
            self.ConvertedL.append(self.result) #and append the result
        
    def DrawL(self, *args): #method that draws L
        self.ChangeL()
        nextCounter = 6 #sets a position counter for the next lines
        for i in self.ConvertedL:  #for every I in the converted R list
            for x in i:     #and for every element in I
                if x == '1': #if x is one, create purple line
                    self.mainCanvas.create_line(self.defCanvasWidthStart+nextCounter,self.defCanvasHeight/4,self.defCanvasWidthStart+nextCounter,(self.defCanvasHeight/4)+80, width=2, fill='purple')
                    nextCounter += 2
                else:   #otherwise, create white line
                    self.mainCanvas.create_line(self.defCanvasWidthStart+nextCounter,self.defCanvasHeight/4,self.defCanvasWidthStart+nextCounter,(self.defCanvasHeight/4)+80, width=2, fill='white')
                    nextCounter += 2

    def DrawBarcode(self, *args): #method that draws the entire thing on the canvas
        #calls previous methods
        self.CheckSum()
        self.DrawL()
        self.DrawR()
        self.GetEntryBarIchi()

        ### BELOW ARE QOL TEXTS, SIZES AND POSITIONS ARE BASED ON THE POSITION IN RELATION TO THE OTHER WIDGETS ###
        self.mainCanvas.create_text((self.defCanvasWidth/2)+10, (self.defCanvasHeight/4)-20, fill='black', text='EAN-13 Barcode:', font='Times 12 bold') 

        #101 First
        self.mainCanvas.create_line(self.defCanvasWidthStart,self.defCanvasHeight/4,self.defCanvasWidthStart,(self.defCanvasHeight/4)+95, width=2, fill='red')
        self.mainCanvas.create_line(self.defCanvasWidthStart+4,self.defCanvasHeight/4,self.defCanvasWidthStart+4,(self.defCanvasHeight/4)+95, width=2, fill='red')

        # #01010 Middle
        self.mainCanvas.create_line(self.defCanvasWidthStart+92,self.defCanvasHeight/4,self.defCanvasWidthStart+92,(self.defCanvasHeight/4)+95, width=2, fill='blue') #1
        self.mainCanvas.create_line(self.defCanvasWidthStart+96,self.defCanvasHeight/4,self.defCanvasWidthStart+96,(self.defCanvasHeight/4)+95, width=2, fill='blue') #1

        # #101 Last
        self.mainCanvas.create_line(self.defCanvasWidthStart+184,self.defCanvasHeight/4,self.defCanvasWidthStart+184,(self.defCanvasHeight/4)+95, width=2, fill='green')
        self.mainCanvas.create_line(self.defCanvasWidthStart+188,self.defCanvasHeight/4,self.defCanvasWidthStart+188,(self.defCanvasHeight/4)+95, width=2, fill='green')

        self.mainCanvas.create_text((self.defCanvasWidth/2)+10, (self.defCanvasHeight/4)+120,fill='#fcba03', text=f'Check Digit: {self.checkSumValue} ', font='Times 12 bold')

        self.mainCanvas.create_text((self.defCanvasWidthStart-10), (self.defCanvasHeight/4)+90, fill='black', text=self.LFirstDigit, font='Times 12 bold')

        self.mainCanvas.create_text((self.defCanvasWidthStart+50), (self.defCanvasHeight/4)+90, fill='black', text=self.NewL, font='Times 12 bold')

        self.mainCanvas.create_text((self.defCanvasWidthStart+140), (self.defCanvasHeight/4)+90, fill='black', text=self.RnewEntryDataListedSnicked, font='Times 12 bold')

        #function that saves it into eps
        self.mainCanvas.postscript(file=self.ValEBI, colormode = 'color')



#creates an object of the Barcode class
def main():
    Barcode()

#runs the function that makes the barcode class when the file is run directly
if __name__ == '__main__':
    main()
