from tkinter import *


class LineDrawer:
    def __init__(self):
        mainWindow = Tk()
        self.canvass = Canvas(mainWindow, width=100, height=100, bg='white')
        self.canvass.pack()
        frame1 = Frame(mainWindow)
        x1Label = Label(frame1, text='X1:')
        x1Label.pack(side=LEFT)
        self.x1Entry = Entry(frame1, text='X1')
        self.x1Entry.pack(side=LEFT)
        
        y1Label = Label(frame1, text='Y1:')
        y1Label.pack(side=LEFT)
        self.y1Entry = Entry(frame1, text='Y1')
        self.y1Entry.pack(side=LEFT)
        
        x2Label = Label(frame1, text='X2:')
        x2Label.pack(side=LEFT)
        self.x2Entry = Entry(frame1, text='X2')
        self.x2Entry.pack(side=LEFT)
        
        y2Label = Label(frame1, text='Y2:')
        y2Label.pack(side=LEFT)
        self.y2Entry = Entry(frame1, text='Y2')
        self.y2Entry.pack(side=LEFT)
        
        frame1.pack()
        
        CheckButt = Button(mainWindow, text='Check', command=self.getCoor)
        CheckButt.pack()
        
        mainWindow.mainloop()
    
    def getCoor(self):
        x1Value = self.x1Entry.get()
        x2Value = self.x2Entry.get()
        y1Value = self.y1Entry.get()
        y2Value = self.y2Entry.get()
        self.canvass.delete('all')
        self.canvass.create_line(x1Value, y1Value, x2Value, y2Value, fill='black')






LineDrawer()