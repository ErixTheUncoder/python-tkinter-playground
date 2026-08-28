import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False,False)
root.title('Spinbox Demo')

current_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=50,
    values=(0,5,10,15,20,25,30,35,40,45,50),
    textvariable = current_value,
    wrap = True
)

spin_box.pack()

root.mainloop()