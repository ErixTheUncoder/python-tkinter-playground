import tkinter as tk

root = tk.Tk()

message = tk.Label(root, text="Hello Worldo!")
message.pack()

try:
    from ctypes import windll # Only works on windows, as it fixes blurry issues of the UI
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
