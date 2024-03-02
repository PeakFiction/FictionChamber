import customtkinter as cst
from PIL import Image, ImageTk

# Create the main window
parent = cst.CTk()
parent.title("Image in CustomTkinter")

# Load and display an image 
# (replace 'your_logo.png' with the path to your image file)
image = Image.open('youshouldKYS.png')
image = ImageTk.PhotoImage(image)

# Create a label to display the image using customtkinter
image_label = cst.CTkLabel(parent, image=image)
image_label.pack()

# Start the CustomTkinter event loop
parent.mainloop()
