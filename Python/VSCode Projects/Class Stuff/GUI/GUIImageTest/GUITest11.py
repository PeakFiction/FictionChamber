from tkinter import *

def nwindow():
    nwin = Toplevel()
    nwin.title("New Window")
    btn.config(state = 'disable')

    photo2 = PhotoImage(file = 'LTGif.gif')
    lbl2 = Label(nwin, image = photo2)
    lbl2.pack()
    nwin.mainloop()

main = Tk()
main.title("Main Window")
main.geometry("750x750")

photo = PhotoImage(file = 'Huhgif.gif')
lbl = Label(main, image = photo)
lbl.pack()

btn = Button(main, text = "New Winodw", command = nwindow)
btn.pack()

main.mainloop()
