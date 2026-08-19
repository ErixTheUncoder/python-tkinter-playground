#Tkinter Frame widget
import tkinter as tk
from tkinter import (TclError, ttk)
    

def create_input_frame(container):
    frame = ttk.Frame(container)

    #Grid layout for input frame
    frame.columnconfigure(0,weight=1)
    frame.columnconfigure(0,weight=3)

    #Find [user_input] (label)
    find_user_input = ttk.Label(frame, text = 'Find:')
    find_user_input.grid(row = 0, column = 0, sticky=tk.W)

    #Find [user_input] (Entry)
    keyword = ttk.Entry(frame,width=30)
    keyword.grid(row = 0, column = 1, sticky=tk.W)
    keyword.focus()

    #Replace With (label)
    replacement_label = ttk.Label(frame, text = 'Replace with:')
    replacement_label.grid(row = 1, column = 0, sticky=tk.W)

    #Replace With(Entry)
    replacement_entry = ttk.Entry(frame,width=30)
    replacement_entry.grid(row = 1, column = 1, sticky=tk.W)

    #Match Case checkbox
    match_case = tk.StringVar()
    match_case_checkbox = ttk.Checkbutton(frame, text = 'Match Case', variable = match_case,
                                          command=lambda: print(match_case.get())
                                          )
    match_case_checkbox.grid(row = 2, column = 0, sticky=tk.W)

    #Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_checkbox = ttk.Checkbutton(frame, text = 'Wrap around', variable = wrap_around,
                                           command= lambda: print(wrap_around.get())
                                           )
    wrap_around_checkbox.grid(row = 3, column = 0, sticky = tk.W)

    #
    for widget in frame.winfo_children(): #What does winfo_children do?
        widget.grid(padx=5,pady=5)

    #Return
    return frame

#TODO: create_button_frame 

def create_main_window():
    root = tk.Tk()
    root.title('Text Replace')
    root.resizable(False,False)

    try:
        #Windows only (remove the min/max button)
        root.attributes("-toolwindow",True)
    except TclError:
        print("min/max button removal not supported on your platform")

    #Layout on the root window
    root.columnconfigure(0,weight=4)
    root.columnconfigure(1,weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0,row=0)

    # button_frame = create_button_frame(root)
    # button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()