import tkinter as tk
import webbrowser

#Create root window
root = tk.Tk()
root.title('Textbox with link attached')

#Create Textbox (With default text)
text = tk.Text(root,height=8)
text.pack(padx=10,pady=10,expand=True,fill=tk.BOTH)

text.insert(
    '1.0',
    'Click here to visit pythontutorial.net',
)

#Create tags (links)
text.tag_add("link","1.0","1.10")
text.tag_config("link",foreground="blue",underline=True)

#Add links function
text.tag_bind(
    "link",
    "<Button-1>",
    lambda e: webbrowser.open("https://www.pythontutorial.net")
)

#Hover
text.tag_bind(
    "link",
    "<Enter>",
    lambda e: text.config(cursor="hand2")
)

#link leave
text.tag_bind(
    "link",
    "<Leave>",
    lambda e: text.config(cursor="")
)

#Show text
text.pack(padx=10,pady=10,side=tk.LEFT)

#Mainloop
root.mainloop()