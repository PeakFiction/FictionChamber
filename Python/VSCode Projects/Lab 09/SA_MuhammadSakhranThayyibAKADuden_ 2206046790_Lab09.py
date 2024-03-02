#Lab 09 Muhammad Sakhran T
from tkinter import Tk, Frame, Canvas, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor

class Scribble(object):
    '''a simple pen drawing application'''
    
    def __init__(self):
        master = Tk()
        master.title("Simple Mouse/Stylus/Finger Scribble")
        
        #mouse coordinates and the drawing color are instance variables
        self.oldx, self.oldy = 0,0 # sets the main coordinate to zero
        self.color = 'green'       # sets the default color to green
        
        #create canvas 400x250 and bind mouse events to handlers
        self.canvas = Canvas(master, bg='white', height=400, width=250 ) 
        self.canvas.bind("<Button-1>", self.begin) #binds the click mouse button 1 to self.begin
        self.canvas.bind("<Button1-Motion>", self.draw) #binds mouse button 1's motion to self.draw
        
        self.canvas.pack(expand=True, fill=BOTH)
        
        #create a new frame for holding the buttons
        
        frame1 = Frame(master) 
        frame1.pack(side=TOP)
        
        self.bt_clear = Button(frame1, text='Clear', bg='Yellow', command=self.delete) #binds the command to self.delete to clear the canvas, have the text be clear
        self.bt_clear.pack(side=LEFT, padx=5) #pads it by 5 on the x axis, places it on the left side
        
        self.bt_color = Button(frame1, text='Colour', bg = self.color, command=self.change_color) #binds the command to self.change_color, text button as Colour
        self.bt_color.pack(side=LEFT) #packs it
        
        self.message = Label(master, text='Press and drag the left mouse-button to draw', fg='blue') #makes the Label in accordance to the master window, have the text 'Press and drag the left mouse-button to draw'
        self.message.pack(side=BOTTOM) #packs it
        
        #start the event loop
        master.mainloop()
        
    def begin(self, event): #begin function used to record the mouse position at the start of the curve
        '''handles left button click by recording mouse position as the start of the curve'''
        self.oldx, self.oldy = event.x, event.y 
        
    def draw(self, event): #draw function to draw the line whilst pressing the left button
        '''handles the mouse motion, while pressing left button, by connecting the previous mouse position to the new one using a line segment'''
        self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=2.5)
        self.oldx, self.oldy = event.x, event.y
        
    def delete(self): #delete function that clear the canvas
        '''clear the canvas'''
        self.canvas.delete('all')
        
    def change_color(self): #function that opens a color wheel to change the color of the line
        '''change the drawing color using the color chooser, also change the background color of the color button'''
        self.color = askcolor()[-1] #get the hex value from the color chooser
        self.bt_color['bg'] = self.color
            

if __name__ == "__main__": #if function help when the file is imported
    Scribble() #calls the main class
