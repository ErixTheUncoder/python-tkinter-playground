from tkinter import ttk
import tkinter as tk

#Setup root windows
root = tk.Tk()
root.geometry("600x400")
root.title("Entry")

#Label for Entry setup
name_label = ttk.Label(
    root,
    text="Name:"
)


email_label = ttk.Label(
    root,
    text='Email:'
)

password_label = ttk.Label(
    root,
    text='Password:'
)


#Entry setup
name_entry = ttk.Entry(
    root
    )
email_entry = ttk.Entry(
    root
    )
password_entry = ttk.Entry(
    root,
    show="*",
)

#Pack
name_label.pack(pady=2)

name_entry.pack(
    pady=5
)

email_label.pack(pady=5)

email_entry.pack(
    pady=5
)

password_label.pack(pady=2)
password_entry.pack(
    pady=5
)

#Focus on the first entry
name_entry.focus()

def current_input():
    print(name_entry.get())
    print(email_entry.get())
    print(password_entry.get())

#Creating a button to print the entered value
button = ttk.Button(root,command=current_input,text="Done")
button.pack()


root.mainloop()