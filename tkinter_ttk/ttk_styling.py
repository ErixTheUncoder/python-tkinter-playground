import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()

# Map background colors to specific states
style.map(
    "TButton",
    background=[
        ("disabled", "#d3d3d3"),  # Gray when disabled
        ("pressed", "#0056b3"),  # Dark blue when clicked
        ("active", "#007bff"),  # Light blue when hovered
    ],
)

def disabled_button(self):
    self.state(["disabled"])

button = ttk.Button(root, text="Hover / Click Me", style="Test.TButton",command=lambda:disabled_button(button)) #prevents the function with parameter being called
button.pack(pady=20)



root.mainloop()