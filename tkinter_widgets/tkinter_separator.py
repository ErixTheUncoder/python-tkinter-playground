from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.geometry('400x200')
root.title('Separator Widget Demo')

#top frame
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP,fill=tk.BOTH, expand=True)
ttk.Label(top_frame,text='Top frame').pack(pady=20)

#create a horizontal separator
separator = ttk.Separator(root, orient=tk.HORIZONTAL)
separator.pack(side=tk.TOP, fill=tk.X, pady=5)

#bottom frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
ttk.Label(bottom_frame,
          text='Bottom Frame',
          ).pack(pady=20)

root.mainloop()