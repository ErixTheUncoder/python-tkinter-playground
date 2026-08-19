import tkinter as tk
from tkinter import ttk


#Setup the main window
root = tk.Tk()
root.geometry("400x250")
root.title("Login")

#Styling
style = ttk.Style()
style.theme_use("aqua")
style.configure("Red.TLabel",background="red",foreground="white",bg="red")

#Grid 3x2
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

#username
username_label = ttk.Label(
    root,
    text="Username:",
    style="Red.TLabel",
)
username_label.grid(
    column=0,
    row=0,
    sticky=tk.EW,
    padx=5,
    pady=5
)

#username entry
username_entry = ttk.Entry(root)
username_entry.grid(
    row = 0, 
    column = 1,
    sticky=tk.EW,
    padx=5,
    pady=5,
)

#Password
password_label = ttk.Label(root,text="Password")
password_label.grid(
    row = 1, 
    sticky=tk.EW,
    padx=5,
    pady=5,
    column = 0)

password_entry = ttk.Entry(root, show='*')
password_entry.grid(
    row = 1, 
    sticky=tk.EW,
    padx=5,
    pady=5,
    column = 1)

login_button = ttk.Button(root, text='Login')
login_button.grid(row = 1, column = 3)

#Mainloop
root.mainloop()