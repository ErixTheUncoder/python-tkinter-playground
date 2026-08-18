import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#Setup the root window
root = tk.Tk()
root.geometry("600x480")
root.title("Exit button Testing")

#Define button functions here
def handle_click():
    showinfo(
        title='Information',
        message='Download have been clicked'        
    )

#Download icon
download_icon = tk.PhotoImage(file='./icon/rocket.png')
download_button = ttk.Button(
    root,
    image=download_icon,
    command=handle_click,
    text="Download",
    compound=tk.TOP,
)
#Pack download icon
download_button.pack(
    expand=True,
    ipadx=50,
    ipady=50,
)

#Setup exit button
exit_button = ttk.Button(
    root,
    text="Exit",
    command=lambda: root.quit(),
)

#Pack exit button
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True,
)


#Main loop
root.mainloop()


