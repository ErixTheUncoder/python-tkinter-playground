#3 types of geometry managers
#Pack, grid, place
#
#Options when using geometry managers
#Side, Expand, Fill, ipadx, ipady, padx, pady
#Anchor

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('600x400')

label1 = tk.Label(root, text='Pack',bg='red',fg='white')
label2 = tk.Label(root, text='Pack',bg='green', fg='white')
label3 = tk.Label(root, text='Pack',bg='blue', fg='white')
label4 = tk.Label(root, text='Pack',bg='purple', fg='white')

label1.pack(side=tk.TOP, fill=tk.X, pady=10)
label2.pack(side=tk.TOP, fill=tk.X, pady=20)
label3.pack(side=tk.TOP, fill=tk.X ,pady=40)
label4.pack(side=tk.TOP, fill=tk.X, pady=60)

root.mainloop()