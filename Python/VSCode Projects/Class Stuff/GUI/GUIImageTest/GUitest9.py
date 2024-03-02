from tkinter import *
from PIL import Image, ImageTk

class FirstWindow:
    def __init__(self):
        self.MainWindow = Tk()
        self.MainWindow.title('First Window')
        
        CheckImage = Image.open('Huhgif.gif')
        CheckImageResized = CheckImage.resize((200, 200))
        HuhImage = ImageTk.PhotoImage(CheckImageResized)
        
        HuhLabel = Label(self.MainWindow, image=HuhImage)
        HuhLabel.pack()
        
        QLabel = Label(self.MainWindow, text='Are You Depressed?')
        QLabel.pack()
        
        Open2ndWindowButton = Button(text='Yes', command=self.OtherWindow)
        Open2ndWindowButton.pack()
        
        NoButton = Button(text='No', command=self.OtherWindow)
        NoButton.pack()
        self.MainWindow.mainloop()
    
    def OtherWindow(self):
        SecondWindow2 = Toplevel()
        SecondWindow2.title('Window 2')
        
        LTGimage = PhotoImage(file = 'LTGif.gif')
        LabelTG = Label(SecondWindow2, image=LTGimage)
        LabelTG.pack()

        WillDoButton = Button(SecondWindow2, text='Right Away!', command=SecondWindow2.destroy)
        WillDoButton.pack()
        
        SecondWindow2.mainloop()

FirstWindow()

