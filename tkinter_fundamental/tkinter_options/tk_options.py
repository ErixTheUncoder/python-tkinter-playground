import tkinter as tk
from tkinter import ttk

root = tk.Tk()

ttk.Label(root, text="Hi there").pack()

label = ttk.Label(root)
label['text'] = 'Hello there' #Same as config() but config() can do multiple changes
label.pack()


root.mainloop()