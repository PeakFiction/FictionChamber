from tkinter import *
from PIL import Image, ImageTk


class ImageDemo:
    def __init__(self):
        mainWindow = Tk()
        mainWindow.title('Image Demo Test')
        
        idImage = Image.open('Flag_of_Indonesia.svg.gif')
        resizeIdImage = idImage.resize((100, 100))
        TrueIdImage = ImageTk.PhotoImage(resizeIdImage)
        
        Fasilkom = Image.open("makara-ui-fasilkom.gif")
        resizedFasilkomImage = Fasilkom.resize((100, 100))
        FasilkomEmblem = ImageTk.PhotoImage(resizedFasilkomImage)
        
        ImageFrame = Frame(mainWindow)
        ImageFrame.pack()
        
        IndonesiaFlag = Label(ImageFrame, image = TrueIdImage)
        IndonesiaFlag.grid(row=0, column=0)
        
        FasilkomImage = Label(ImageFrame, image=FasilkomEmblem)
        FasilkomImage.grid(row=0, column=1)
        
        ButtonFrame = Frame(mainWindow)
        ButtonFrame.pack()
        
        
        
        mainWindow.mainloop()
        
        

ImageDemo()