#importing tkinter
import tkinter as ui
from tkinter import filedialog, messagebox
# implementing menu operations
def open():
    operation.configure(text="you have selected menu > open")
    filedialog.askopenfilename()
def info():
    messagebox.showinfo("Information", "This is an information") 
def warning():
    messagebox.showwarning("Warning", "This is a warning")      
def error():
    messagebox.showerror("Error", "This is an Error")  
def response():
    ans = messagebox.askyesno("give your feedback", "did you like it")
    if ans == True:
        operation.configure(text="Thanks for loving this")
    else:
        operation.configure(text="we will improve and get back to you soon...")  
# creating a top level window
def open_list_window():
    top = ui.Toplevel(parent)
    top.title("listbox demo")
    top.geometry("300x300")
    ui.Label(top, text="select a language").pack()
    scrollBar = ui.Scrollbar(top)
    scrollBar.pack(side=ui.RIGHT, fill=ui.Y)
    listbox = ui.Listbox(top, yscrollcommand=scrollBar.set)
    languages = ["python", "c", "java", "c++", "javaScript"]
    for lang in languages:
        listbox.insert(ui.END, lang)
    listbox.pack(side=ui.LEFT)
    scrollBar.config(command=listbox.yview)
    def show_selected():
        selected = listbox.get(listbox.curselection())
        messagebox.showinfo("Selected", selected)
    ui.Button(top, text="Show Selection", command=show_selected).pack()
# create a window
parent = ui.Tk()
parent.geometry("600x600")
parent.title("grid layout demo")
# label for message
operation = ui.Label(parent, text="")
operation.grid()
# creating menu
MainMenu = ui.Menu(parent)
# sub menus
FileMenu = ui.Menu(MainMenu, tearoff=0)
showMenu = ui.Menu(MainMenu, tearoff=0)
# File menu
FileMenu.add_command(label="Open", command=open)
FileMenu.add_separator()
FileMenu.add_command(label="Close", command=parent.destroy)
# Show menu
showMenu.add_command(label="Info", command=info)
showMenu.add_command(label="Error", command=error)
showMenu.add_command(label="Warning", command=warning)
showMenu.add_command(label="Feedback", command=response)
showMenu.add_command(label="Listbox", command=open_list_window)  
# adding menu
MainMenu.add_cascade(label="File", menu=FileMenu)
MainMenu.add_cascade(label="Show", menu=showMenu)
parent.config(menu=MainMenu)
# run gui
parent.mainloop()