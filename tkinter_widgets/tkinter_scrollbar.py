import tkinter as tk
from tkinter import ttk

#Create a root window
root = tk.Tk()
root.title("Tkinter Scrollbar")

#Create frame & display
frame = ttk.Frame(root)
frame.pack(padx=10,
           pady=10,
           fill=tk.BOTH,
           expand=True)

#Create scrollbar to add to frame
v_scrollbar = ttk.Scrollbar(frame)
v_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

#Create a text widget and add to frame
text = tk.Text(frame, height=8)
text.pack(side=tk.LEFT,
          expand=True,
          fill=tk.BOTH,)

#Config scrollbar
text['yscrollcommand'] = v_scrollbar.set
v_scrollbar.config(command=text.yview)

#insert some text into text widget
text.insert(tk.END,'\n' * 20)

root.mainloop()
