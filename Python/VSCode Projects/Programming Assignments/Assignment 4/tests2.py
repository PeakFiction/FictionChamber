# Import the required libraries
from tkinter import *
from tkinter import messagebox

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the error message
def on_click():
    messagebox.showerror('Python Error', 'Error: This is an Error Message!')

# Create a label widget
label = Label(win, text="Click the button to show the message ",
font=('Calibri 15 bold'))
label.pack(pady=20)


# Create a button to delete the button
b = Button(win, text="Click Me", command=on_click)
b.pack(pady=20)

win.mainloop()