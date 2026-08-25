from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.geometry('400x200')
root.title('Separator Vertical Widget Demo')

#Left frame
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
ttk.Label(left_frame,text='Left frame').pack(pady=20)


#Right frame
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
ttk.Label(right_frame,
          text='Right Frame',
          ).pack(pady=20)

#create a horizontal separator
separator = ttk.Separator(root, orient=tk.HORIZONTAL)
separator.pack(side=tk.LEFT, fill=tk.Y, pady=5)


root.mainloop()