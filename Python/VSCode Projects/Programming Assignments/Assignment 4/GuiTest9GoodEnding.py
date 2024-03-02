from tkinter import *

class FirstWindow:
    def __init__(self):
        self.MainWindow = Tk()
        self.MainWindow.title('Are You?')
        
        HuhImage = PhotoImage(file = "Huhgif.gif")
        
        
        HuhLabel = Label(self.MainWindow, image=HuhImage)
        HuhLabel.pack()
        
        QLabel = Label(self.MainWindow, text='Are You Depressed?')
        QLabel.pack()
        
        Open2ndWindowButton = Button(text='Yes', command=self.OtherWindow)
        Open2ndWindowButton.pack()
        
        NoButton = Button(text='No', command=self.OkayWindow)
        NoButton.pack()
        self.MainWindow.mainloop()

    def OtherWindow(self):
        SecondWindow2 = Toplevel()
        SecondWindow2.title('Try This Then!')
        
        LTGimage = PhotoImage(file = 'ltggoodending.gif')
        LabelTG = Label(SecondWindow2, image=LTGimage)
        LabelTG.pack()

        WillDoButton = Button(SecondWindow2, text='Right Away!', command=SecondWindow2.destroy)
        WillDoButton.pack()
        
        SecondWindow2.mainloop()
    
    def OkayWindow(self):
        OkayWindow1 = Toplevel()
        OkayWindow1.title('Okay!')
        
        OkayImage = PhotoImage(file = "okayimage.gif")
        OkayLabel = Label(OkayWindow1, image=OkayImage )
        OkayLabel.pack()
        
        OkayWindow1.mainloop()

FirstWindow()


