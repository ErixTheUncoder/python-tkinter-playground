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


#Set max size
root.resizable(True,True) #Locks the x and y axis

root.minsize(300,300)

root.maxsize(1200,800)

#Set properties
root.attributes('-alpha',0.5)
root.attributes("-topmost")

#Setup for Icon
icon = tk.PhotoImage(file='./../icon/rocket.png')
root.iconphoto(True,icon)

#Setup the geometry
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")


root.mainloop()