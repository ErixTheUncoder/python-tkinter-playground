import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#main Window
root = tk.Tk()
root.geometry("800x500")
root.title("Label Widget Demo")

#Create label
label = ttk.Label(root,
                  text='This is an image',
                  font=("Comic Sans", 14))
label.pack()

#Resizing the image
photo = Image.open('./icon/rocket.png')
resized_pht = photo.resize((250,250))
TkImg = ImageTk.PhotoImage(resized_pht)

image_label = ttk.Label(
    root,
    text="Rocket",
    image=TkImg,
    padding=5,
    compound=tk.RIGHT,
)
image_label.pack()

root.mainloop()