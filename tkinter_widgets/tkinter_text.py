import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#Create root window
root = tk.Tk()
root.title("Text Widget Example")

#Create text area
text = tk.Text(root,height=8)
text.pack(padx=10,pady=10,expand=True,fill=tk.BOTH)

#text insert
text.insert(
    index='1.0', #Where to insert the text, eg. '1.0' = line 1, character 0
    chars='This is Text widget demo'
)

#Create a button to get text
button = ttk.Button(
    root, 
    text = 'Get Text', 
    command = lambda: showinfo(
        title="Text Data",
        message=text.get('1.0',tk.END))
        )

#display the button
button.pack(padx = 10,
            pady=10,
            side=tk.LEFT
            )


#Mainloop
root.mainloop()