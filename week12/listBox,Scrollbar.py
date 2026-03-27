import tkinter as tk

gui = tk.Tk()
gui.title("Listbox with Scrollbar")
gui.geometry("300x300")

# Scrollbar
scroll = tk.Scrollbar(gui)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
listbox = tk.Listbox(gui, yscrollcommand=scroll.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Adding items
items = ["Python", "Java", "C", "C++", "JavaScript", "HTML", "CSS"]
for i in items:
    listbox.insert(tk.END, i)

# Connect scrollbar
scroll.config(command=listbox.yview)

# Function
def show():
    selected = listbox.get(listbox.curselection())
    label.config(text="Selected: " + selected)

# Button
tk.Button(gui, text="Show", command=show).pack()

# Label
label = tk.Label(gui, text="")
label.pack()

gui.mainloop()