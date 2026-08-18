import tkinter as tk
from tkinter import ttk

#Create root window
root = tk.Tk()
root.geometry("600x480")
root.title("Tracing Text")

#Setup text variable
name_var = tk.StringVar()
name_entry = ttk.Entry(
    root,
    textvariable=name_var,
)

name_entry.pack()
name_entry.focus()

output_label = ttk.Label(root)
output_label.pack()

name_var.trace_add(
    "write",
    lambda *args: output_label.config(
        text=name_var.get().upper()
    )
)

root.mainloop()