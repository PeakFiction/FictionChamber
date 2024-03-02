import tkinter 

mainWindow = tkinter.Tk(screenName="You ARE A DINGUS", baseName="YOU ARE A DINGUS")
mainWindow.title("TestName")

buttonTest = tkinter.Button(mainWindow, text="Test Button", width='10', activebackground="blue", activeforeground="red"
                            , command=mainWindow.destroy)
label = tkinter.Label(mainWindow, text="Test")
label2 = tkinter.Label(mainWindow, text="Click to Acknowledge:")
label.pack()
label2.pack()
buttonTest.pack()


secondWindow = tkinter.Tk(screenName="You ARE A DINGUS", baseName="YOU ARE A DINGUS")
secondWindow.title("TestName")

secondbuttonTest = tkinter.Button(secondWindow, text="Test Button", width='10', activebackground="blue", activeforeground="red"
                            , command=secondWindow.destroy)
secondlabel = tkinter.Label(secondWindow, text="Test")
secondlabel2 = tkinter.Label(secondWindow, text="Test1")
secondlabel.pack()
secondlabel2.pack()
secondbuttonTest.pack()
mainWindow.mainloop()