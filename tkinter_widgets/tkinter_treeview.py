import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Treeview")

frame = ttk.Frame(root)

# create a treeview widget
treeview = ttk.Treeview(frame, columns=( "Salary","Bonus"))

treeview.heading("#0", text="Employee")
treeview.heading("Salary", text="Salary")
treeview.heading("Bonus", text="Bonus")


icon_city = tk.PhotoImage(file="./tkinter_widgets/assets/city.png")
level1 = treeview.insert('', tk.END, text="San Jose", image=icon_city)


icon_male = tk.PhotoImage(file="./tkinter_widgets/assets/male.png")
icon_female= tk.PhotoImage(file="./tkinter_widgets/assets/female.png")


treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}",f"${8000: ,}"), image=icon_male)
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}",f"${9000: ,}"), image=icon_female)

# create a vertical scrollbar
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=v_scrollbar.set)

# pack the treeview and scrollbar
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# package the frame
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


root.mainloop()