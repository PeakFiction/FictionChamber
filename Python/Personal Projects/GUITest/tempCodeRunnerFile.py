import customtkinter as cst
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

mainWindow = cst.CTk()
mainWindow.geometry("800x600")

def buttonClicked():
    print("Button Clicked")


def openYesWindow():
    mainWindow.withdraw()
    yesWindow = Toplevel(mainWindow)
    yesWindow.title("YOU SHOULD KILL YOURSELF NOW!!!")
    image = Image.open("youshouldKYS.png")
    image = ImageTk.PhotoImage(image)
    
    imageLabel = cst.CTkLabel(master=yesWindow, image=image)
    imageLabel.pack()
    
    def backButtonFunction():
        yesWindow.destroy()
        yesWindow.update()
        mainWindow.deiconify()
    
    backButton = cst.CTkButton(master=yesWindow, text="Back", width=len("Back"), command=backButtonFunction)
    backButton.pack()

def openNoWindow():
    mainWindow.withdraw()
    noWindow = Toplevel(mainWindow)
    noWindow.title("YOU SHOULD LOVE YOURSELF NOW!!!")
    image = Image.open("youshouldLYS.png")
    image = ImageTk.PhotoImage(image)
    
    imageLabel = cst.CTkLabel(master=noWindow, image=image)
    imageLabel.pack()
    
    def backButtonFunctionInNo():
        noWindow.destroy()
        noWindow.update()
        mainWindow.deiconify()
    
    backButton = cst.CTkButton(master=noWindow, text="Back", width=len("Back"), command=backButtonFunctionInNo)
    backButton.pack()

question = cst.CTkLabel(master=mainWindow, text="Are You Depressed?")
question.place(relx=0.5, rely=0.4, anchor="center")  # Adjust rely for the first label

yesButton = cst.CTkButton(master=mainWindow, text="Yes", command=openYesWindow, width=len("Yes"))
yesButton.place(relx=0.47, rely=0.45, anchor="center")

noButton = cst.CTkButton(master=mainWindow, text="No", command=openNoWindow, width=len("No"))
noButton.place(relx=0.53, rely=0.45, anchor="center")

mainWindow.mainloop()
