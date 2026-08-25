import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

#create the main window
root = tk.Tk()
root.geometry("600x250")
root.title('Listbox')

#Create the variable object
programming_languages = ('Java','C','C++','C#','Python',
                         'Go','JS','PHP','Swift','asdf','adsf','adsfadaf','asdfasdf')

list_var = tk.Variable(value=programming_languages)

#label
label = ttk.Label(
    root,
    text='Select your favourite languages: '
)
label.pack(padx=10,pady=0,side=tk.TOP,fill=tk.X)

#Create listbox
listbox = tk.Listbox(
    root,
    listvariable=list_var,
    height=6,
    selectmode=tk.MULTIPLE, #tk.___ is standard rather than 'multiple'
)
#display listbox
listbox.pack(padx=10,pady=10,expand=True,fill=tk.BOTH,side=tk.LEFT)

#handle item selection from listbox
def handle_item_select(e):
    selected_indices = listbox.curselection()
    selected_languages = ','.join([listbox.get(i) for i in selected_indices])

    showinfo(
        title = 'Information',
        message = f'You selected: {selected_languages}',
    )

listbox.bind('<<ListboxSelect>>', handle_item_select)

root.mainloop()