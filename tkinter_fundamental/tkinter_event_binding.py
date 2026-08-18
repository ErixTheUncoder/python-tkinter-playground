import tkinter as tk
from tkinter import ttk

def return_pressed(e):
    print("Return key pressed.")

def log(e):
    print(e)

root = tk.Tk()

btn = ttk.Button(root,text='Save')
# btn.bind('<Return>',return_pressed)
# btn.bind('<Return>', log, add='+')

# btn.focus()
# btn.pack(expand=True)

root.bind('<Return>',return_pressed)

root.mainloop()