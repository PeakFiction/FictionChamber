import tkinter as tk

class MyGUI():
    
    def __init__(self): #method that initialisies the class itself
        
        self.mainWindow = tk.Tk()
        
        self.label = tk.Label(self.mainWindow, text='Your Message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.mainWindow, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        
        self.checkState = tk.IntVar()
        
        self.check = tk.Checkbutton(self.mainWindow, text='Show Message Box', font=('Arial', 16), variable=self.checkState)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.mainWindow, text='Show Message', font=('Arial', 18))
        self.button.pack(padx=10, pady=10)
        
        self.mainWindow.mainloop()
    
    def showMessage(self):
        pass



MyGUI()