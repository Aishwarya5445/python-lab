#importing tkinter
import tkinter as ui
from tkinter import filedialog,messagebox

#implemening menu oprations
def open():
    operation.configure(text="you have selected menu > open")
    filedialog.askopenfilename()
def info():
    messagebox.showinfo("Inforation","This is an information") 
def warning():
    messagebox.showwarning("Warning","This is a warning")      
def error():
    messagebox.showerror("Error","This is an Error")  
def response():
    ans=messagebox.askyesno("give your feedback","did you like it")
    if ans==True:
        operation.configure(text="Thanks for loving this")
    else:
        operation.configure(text="we will improve and get back to you soon...")  

# create a window
parent=ui.Tk()
parent.geometry("600x600")
parent.title("grid layout demo")
# label for message
operation= ui.Label(parent,text="")
operation.grid()
#creating menu
MainMenu=ui.Menu(parent)
# creating sub menu
FileMenu=ui.Menu(MainMenu)
showMenu=ui.Menu(MainMenu)
#adding menu options
FileMenu.add_command(label="open",command=open)
FileMenu.add_separator()
FileMenu.add_command(label="close",command=parent.destroy)

showMenu.add_command(label="info",command=info)
showMenu.add_command(label="error",command=error)
showMenu.add_command(label="warning",command=warning)
showMenu.add_command(label="feedback",command=response)

#adding menu to window
MainMenu.add_cascade(label="File",menu=FileMenu)
MainMenu.add_cascade(label="Show",menu=showMenu)
parent.config(menu=MainMenu)

#craeting a top level window
def open_list_window():
    top=ui.Toplevel(parent)
    top.title("listbox demo")
    top.geometry("300x300")
    # message label
    ui.Label(top,text="select a language").pack()
    #crate a scrollbar
    scrollBar=ui.Scrollbar(top)
    scrollBar.pack(side=ui.RIGHT,fill=ui.Y)
    # create a listbox
    listbox=ui.Listbox(top,yscrollcommand=scrollBar.set)
    #insert in listbox
    languages=["python","c","java","c++","javaScript"]
    for lang in languages:
        listbox.insert(ui.END,lang)
    listbox.pack(side=ui.LEFT)
    #adding scrollbar o list box
    scrollBar.config(command=listbox.yview)
    #button to display selected item

    def show_selected():
        selected=listbox.get(listbox.curselection)
        messagebox.showinfo("selected",selected)
        ui.Button(top,text="show selection",command= show_selected).pack()
# run gui
parent.mainloop()