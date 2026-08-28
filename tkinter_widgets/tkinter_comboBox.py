from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()
root.geometry('300x200')
root.resizable(False,False)
root.title('Combobox Widget')

#label
label = ttk.Label(text='Please select a month')
label.pack(fill=tk.X,padx=5,pady=5)

#Create combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root,
                        textvariable=selected_month)

#Get first 3 letter of every month name
month_cb['values'] = [month_name[m][0:3] for m in range(1,13)]

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X,padx=5,pady=5)

# bind selected value changes
def month_changed(e):
    #Handle the month changed event
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}.'
    )

month_cb.bind('<<ComboboxSelected>>',month_changed)

current_month = datetime.now().strftime('%b')
month_cb.set(current_month)

root.mainloop()