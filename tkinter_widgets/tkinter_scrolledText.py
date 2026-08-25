import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title("ScrolledText Widget")

text = ScrolledText(root,
                    width=80,
                    height=8)
text.pack(padx=10,pady=10,fill=tk.BOTH, side = tk.LEFT,expand=True)

root.mainloop()