import customtkinter as cst
from tkinter import *
from tkinter.ttk import *

root = cst.CTk()
root.geometry("500x350")

def open_new_window():
    root.withdraw()
    newWindow = Toplevel(root)
    newWindow.title("New Window Bitch")
    newWindow.geometry("200x200")
    label = cst.CTkLabel(master=newWindow, text="This is a New Window")
    label.pack()
    
    def exitButton():
        newWindow.destroy()
        newWindow.update()
        root.deiconify()
    
    backButton = cst.CTkButton(newWindow, text="EXIT", command=exitButton)
    backButton.pack()

rootLabel = cst.CTkLabel(master=root, text="This is the Main Window")

# Create a button that opens the new window when clicked
button = cst.CTkButton(master=root, text='Open New Window', command=open_new_window)
button.pack(pady=20)

root.mainloop()





