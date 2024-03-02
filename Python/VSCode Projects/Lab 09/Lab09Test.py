from tkinter import *
from tkinter.colorchooser import askcolor

class Scribble(object):
    '''a simple pen drawing application'''
    
    def __init__(self):
        master = Tk()
        master.title = ('Simple Mouse/Stylus/Finger Scribble')
        
        #mouse coordinates and the drawing color are instance variables
        self.oldx, self.oldy = 0,0
        self.color = 'green'
        
        #create canvas 400x250 and bind mouse events to handlers
        self.canvas = Canvas(master, bg='white', height=400, width=250 )
        self.canvas.bind("<Button-1>", command=self.begin)
        self.canvas.bind("<Button1-Motion>", command=self.draw)
        
        self.canvas.pack(expand=True, fill=BOTH)
        
        #create a new frame for holding the buttons
        
        frame1 = Frame(master)
        frame1.pack(side=TOP)
        
        self.bt_clear = Button(frame1, text='Clear', command=self.delete)
        self.bt_clear.pack(side=LEFT, padx=5)
        
        self.bt_color = Button(frame1, text='Colour', bg = self.color, command=self.change_color)
        self.bt_color.pack(side=LEFT)
        
        self.message = Label(master, text='Press and drag the left mouse-button to draw', fg='blue')
        self.message.pack(side=BOTTOM)
        
        #start the event loop
        master.mainloop()
        
        
if __name__ == "__main__":
    Scribble()