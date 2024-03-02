"""
Lab 10 FPROG1 2022
- draw elastic (rubber) shapes on a canvas by
a left mouse-click and dragging,
- move the last drawn shape by a right mouse-click 
"""

from tkinter import *
from tkinter.colorchooser import askcolor

class DrawRubberShapes(object):
    # Construct the GUI
    def __init__(self):
        window = Tk() # Create a window
        window.title("Lab 10: Drawing Rubber Shapes") # Set a title 
        frame1 = Frame(window) # Create and add a frame to window 
        frame1.pack()
        
        def ClearCommand(): #command to clear the canvas
            canvas.delete("all")
        
        # Create a button for choosing color using a color chooser 
        self.fillColor = StringVar()
        self.fillColor.set('red')
        
        def colorCommand(): #command to open the color wheel
            (rgb,color) = askcolor()
            if color != None:
                self.fillColor.set(color)
                colorButton["bg"] = color 
        colorButton = Button(frame1, text = "Color", command=colorCommand, bg = self.fillColor.get()) 
        colorButton.grid(row=1,column=1,columnspan=2)
        
        clearButton = Button(frame1, text='Clear', command=ClearCommand, bg='blue', fg='white')
        clearButton.grid(row=1, column=6, columnspan=2)
        
        # Create radio buttons for geometrical shapes
        self.v1 = StringVar() #sets the variable to be a string 
        self.v1.set('R') #sets the default radio button to rectangle
        rbRectangle = Radiobutton(frame1, text = "Rectangle", variable = self.v1, value = 'R', command = self.processRadiobutton)
        rbRectangle.grid(row = 1, column = 5)
        
        rbOval  = Radiobutton(frame1, text='Oval', variable = self.v1, value='O', command=self.processRadiobutton)
        rbOval.grid(row = 1, column = 4)
        
        rbLine = Radiobutton(frame1, text='Line', variable=self.v1, value='L', command=self.processRadiobutton)
        rbLine.grid(row=1, column=3)
        
        
        # Create a canvas, bound to mouse events
        canvas = Canvas(window, width=400, height=300) #sets the canvas
        self.canvas = canvas
        self.canvas.pack()  #packs the canvas
        self.canvas.bind('<ButtonPress-1>', self.onStart) #binds mouse button 1 (left click)
        self.canvas.bind('<B1-Motion>', self.onGrow)      #binds the motion of mouse button 1 (left click)
        self.canvas.bind('<ButtonPress-3>', self.onMove)  #binds mouse button 3 (right click)
        
        # for remembering the last drawing
        self.drawn = None       
        self.length = 0
        self.height = 0
        self.shape = self.canvas.create_rectangle 
        window.mainloop()
        
    def processRadiobutton(self): #function that determines which shapes in accordance to the radio button
        if self.v1.get() == 'R': #creates a rectangle
            self.shape = self.canvas.create_rectangle
        elif self.v1.get() == 'O': #creates an oval
            self.shape = self.canvas.create_oval
        elif self.v1.get() == 'L': #creates a line
            self.shape = self.canvas.create_line
        
    def onStart(self, event): #function that defines the start point of the shape
        self.start = event
        self.drawn = None
    
    # elastic drawing: delete and redraw, repeatedly 
    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn) #deletes the previous drawing, and then redraw it again until the mouse stops
        self.length = self.start.x - event.x #tells the length of the shape
        self.height = self.start.y - event.y #tells the height of the shape
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y, fill=self.fillColor.get()) 
        self.drawn = objectId
        
    # move the shape to the click spot
    def onMove(self, event):
        if self.drawn:
            canvas = event.widget
            diffX, diffY = ((event.x+(self.length/2))-self.start.x),((event.y+(self.height/2))-self.start.y) #tells the difference of the current mouse position with the center of the drawn shape
            canvas.move(self.drawn, diffX, diffY) 
            self.start = event # determines the start point and calls it before a new drawing is made
            self.start.x = self.start.x + self.length/2
            self.start.y = self.start.y + self.height/2
    

#runs the class
if __name__ == '__main__':
    DrawRubberShapes()
