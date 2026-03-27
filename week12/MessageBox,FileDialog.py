import tkinter as tk
from tkinter import messagebox, filedialog

gui = tk.Tk()
gui.title("MessageBox and FileDialog")
gui.geometry("300x200")

# Function for messagebox
def show_message():
    messagebox.showinfo("Info", "This is a message box")

# Function for file dialog
def open_file():
    file = filedialog.askopenfilename()
    label.config(text="Selected: " + file)

# Buttons
tk.Button(gui, text="Show Message", command=show_message).pack(pady=10)
tk.Button(gui, text="Open File", command=open_file).pack(pady=10)

# Label
label = tk.Label(gui, text="")
label.pack()

gui.mainloop()