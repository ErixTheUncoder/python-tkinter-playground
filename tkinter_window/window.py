import tkinter as tk


#Setup the main window
root = tk.Tk()
root.title("Tkinter Window Demo")

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

#get screen dimension
screen_width= root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#find center point
center_x = int(screen_width/2 - WINDOW_WIDTH)
center_y = int(screen_height/2 - WINDOW_HEIGHT)

root.attributes("-topmost")

#Setup the geometry
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")

root.mainloop()