from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Demo Image Test')

openedIDimage = Image.open("Flag_of_Indonesia.svg.gif")
resizedIDimage = openedIDimage.resize((250, 100))

IDimage = ImageTk.PhotoImage(resizedIDimage)

meinLabel = Label(window, text='INDONESIA UBER ALLES', image=IDimage)
meinLabel.pack()

window.mainloop()