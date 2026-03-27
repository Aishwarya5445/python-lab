import tkinter as tk

gui = tk.Tk()
gui.title("Simple Menu Example")
gui.geometry("300x200")

# -------- Menu --------
def show():
    label.config(text="Menu Clicked")

menu = tk.Menu(gui)
menu.add_command(label="Click Me", command=show)
gui.config(menu=menu)

# -------- Menubutton --------
mb = tk.Menubutton(gui, text="Options")
mb.pack()

mb.menu = tk.Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Option 1", command=show)

# Label
label = tk.Label(gui, text="")
label.pack()

gui.mainloop()