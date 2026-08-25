import tkinter as tk

root = tk.Tk()
root.title('Textbox with embedded img')

text = tk.Text(
    root,
    height=8,
)
text.pack(padx=10,
          pady=10,
          expand=True,
          fill=tk.BOTH
          )

text.insert(index='1.0',
            chars='This is a Text widget demo with embedding img')

#embed an image
image = tk.PhotoImage(file="./tkinter_widgets/plan/pythonicon.png")
text.image_create('1.0',image=image)

#mainloop
root.mainloop()