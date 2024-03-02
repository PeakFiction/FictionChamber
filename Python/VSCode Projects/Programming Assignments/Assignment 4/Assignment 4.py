from tkinter import *
from tkinter import messagebox

class Barcode:
    def __init__(self):
        mainWindow = Tk()
        mainWindow.title("EAN-13 by Muhammad Sakhran Thayyib // Duden")
        
        LabelIchi = Label(mainWindow, text='Save barcode to PS file [e.g.: EAN13.eps]: ')
        LabelIchi.pack()
        
        self.EntryBarIchi = Entry(mainWindow)
        self.EntryBarIchi.pack()
        self.EntryBarIchi.bind('<Return>', self.GetEntryBarIchi)
        
        LabelNi = Label(mainWindow, text='Enter code (first 12 decimal digits): ' )
        LabelNi.pack()
        
        self.EntryBarNi = Entry(mainWindow)
        self.EntryBarNi.pack()
        self.EntryBarNi.bind('<Return>', self.GetEntryBarNi)
        
        self.OutputPrompt = self.EntryBarIchi.get()
        self.InputPrompt = list(str(self.EntryBarNi.get()))
        
        
        self.mainCanvas = Canvas(mainWindow, bg='white')
        self.mainCanvas.pack()
        
        defCanvasWidth = self.mainCanvas.winfo_reqwidth()
        defCanvasWidthStart = (defCanvasWidth-190)/2
        defCanvasWidthStop = (defCanvasWidth-defCanvasWidthStart)
        defCanvasHeight = self.mainCanvas.winfo_reqheight()
        defCanvasHeight
        
        #101 First
        self.mainCanvas.create_line(defCanvasWidthStart,150,defCanvasWidthStart,55, width=2, fill='green')
        self.mainCanvas.create_line(defCanvasWidthStart+4,150,defCanvasWidthStart+4,55, width=2, fill='green')

        # #01010 Middle
        self.mainCanvas.create_line(defCanvasWidthStart+90,150,defCanvasWidthStart+90,55, width=2, fill='red') #0
        self.mainCanvas.create_line(defCanvasWidthStart+92,150,defCanvasWidthStart+92,55, width=2, fill='green') #1
        self.mainCanvas.create_line(defCanvasWidthStart+94,150,defCanvasWidthStart+94,55, width=2, fill='red') #0
        self.mainCanvas.create_line(defCanvasWidthStart+96,150,defCanvasWidthStart+96,55, width=2, fill='green') #1
        self.mainCanvas.create_line(defCanvasWidthStart+98,150,defCanvasWidthStart+98,55, width=2, fill='red') #0

        # #101 Last
        self.mainCanvas.create_line(defCanvasWidthStart+184,150,defCanvasWidthStart+184,55, width=2, fill='green')
        self.mainCanvas.create_line(defCanvasWidthStart+186,150,defCanvasWidthStart+186,55, width=2, fill='green')
        self.mainCanvas.create_line(defCanvasWidthStart+188,150,defCanvasWidthStart+188,55, width=2, fill='green')
        
        mainWindow.mainloop()
        
        
    def GetEntryBarIchi(self, *args):
        ValEBI = self.EntryBarIchi.get()
        print(ValEBI)
    
    def GetEntryBarNi(self, *args): 
        try:
            if len(str(self.EntryBarNi.get())) != 12:
                messagebox.showerror('Wrong Input!', 'Please enter correct input code')
            else:
                print(int(self.EntryBarNi.get()))
                print(list(str(self.EntryBarNi.get())))
        except ValueError:
            messagebox.showerror('Wrong Input!', 'Please enter correct input code')


Barcode()




#if __name__ == '__main__':
#   main()