import tkinter as tk
from tkinter import ttk

def button_clicked():
    print('Button clicked')

def select(option):
    print(option)

root = tk.Tk()

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()