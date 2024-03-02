import tkinter as tk

window = tk.Tk()

window.title("My First GUI")
window.geometry("500x500")

label = tk.Label(window, text = "Hello World!", font = ('Arial', 18))
label.pack(padx = 20, pady = 20)

textbox = tk.Text(window, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

button1 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
button1.grid(row=0, column=0, sticky=tk.W+tk.E)

button2 = tk.Button(buttonFrame, text='2', font=('Arial', 18))
button2.grid(row=0, column=1, sticky=tk.W+tk.E)

button3 = tk.Button(buttonFrame, text='3', font=('Arial', 18))
button3.grid(row=0, column=2, sticky=tk.W+tk.E)

button4 = tk.Button(buttonFrame, text='4', font=('Arial', 18))
button4.grid(row=1, column=0, sticky=tk.W+tk.E)

button5 = tk.Button(buttonFrame, text='5', font=('Arial', 18))
button5.grid(row=1, column=1, sticky=tk.W+tk.E)

button6 = tk.Button(buttonFrame, text='6', font=('Arial', 18))
button6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')

anotherButton = tk.Button(window, text='Test')
anotherButton.place(x=200, y=200, height=100, width=100)




window.mainloop()