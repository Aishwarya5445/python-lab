import tkinter as tk

gui = tk.Tk()
gui.title("Checkbutton and Radiobutton")
gui.geometry("400x400")

# Checkbuttons
h1 = tk.IntVar()
h2 = tk.IntVar()

tk.Label(gui, text="Select Hobbies").pack()
tk.Checkbutton(gui, text="Reading", variable=h1).pack()
tk.Checkbutton(gui, text="Sports", variable=h2).pack()

# Radiobuttons
gender = tk.StringVar()

tk.Label(gui, text="Select Gender").pack()
tk.Radiobutton(gui, text="Male", variable=gender, value="Male").pack()
tk.Radiobutton(gui, text="Female", variable=gender, value="Female").pack()

# Function
def show():
    hobbies = ""
    if h1.get() == 1:
        hobbies += "Reading "
    if h2.get() == 1:
        hobbies += "Sports "
    
    result.config(text="Hobbies: " + hobbies + "\nGender: " + gender.get())

# Button
tk.Button(gui, text="Submit", command=show).pack()

# Result Label
result = tk.Label(gui, text="")
result.pack()

gui.mainloop()