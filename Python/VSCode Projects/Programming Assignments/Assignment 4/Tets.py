from tkinter import *

mainWindow = Tk()
mainCanvas = Canvas(mainWindow, bg='white')
mainCanvas.pack()


defCanvasWidth = mainCanvas.winfo_reqwidth()
defCanvasWidthStart = (defCanvasWidth-190)/2
defCanvasWidthStop = (defCanvasWidth-defCanvasWidthStart)

defCanvasHeight = mainCanvas.winfo_reqheight()


#101 First
mainCanvas.create_line(defCanvasWidthStart,150,defCanvasWidthStart,55, width=2, fill='green')
mainCanvas.create_line(defCanvasWidthStart+4,150,defCanvasWidthStart+4,55, width=2, fill='green')

# #01010 Middle
mainCanvas.create_line(defCanvasWidthStart+90,150,defCanvasWidthStart+90,55, width=2, fill='red') #0
mainCanvas.create_line(defCanvasWidthStart+92,150,defCanvasWidthStart+92,55, width=2, fill='green') #1
mainCanvas.create_line(defCanvasWidthStart+94,150,defCanvasWidthStart+94,55, width=2, fill='red') #0
mainCanvas.create_line(defCanvasWidthStart+96,150,defCanvasWidthStart+96,55, width=2, fill='green') #1
mainCanvas.create_line(defCanvasWidthStart+98,150,defCanvasWidthStart+98,55, width=2, fill='red') #0

# #101 Last
mainCanvas.create_line(defCanvasWidthStart+184,150,defCanvasWidthStart+184,55, width=2, fill='green')
mainCanvas.create_line(defCanvasWidthStart+186,150,defCanvasWidthStart+186,55, width=2, fill='green')
mainCanvas.create_line(defCanvasWidthStart+188,150,defCanvasWidthStart+188,55, width=2, fill='green')




print(mainCanvas.winfo_reqwidth())
print(mainCanvas.winfo_reqheight())


mainWindow.mainloop()