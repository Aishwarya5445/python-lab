import tkinter as tk
gui=tk.Tk()
gui.geometry("400x300")
gui.title("using label,entry and buttons")
#label
num1= tk.Label(gui,text="enter number1")
num1.pack()
#entry
userInput1= tk.Entry(gui)
userInput1.pack()
#label
num2= tk.Label(gui,text="enter number2")
num2.pack()
#entry
userInput2= tk.Entry(gui)
userInput2.pack()

# button function
def sum():
    n1 = userInput1.get()
    n2 = userInput2.get()
    if n1.isdigit() and n2.isdigit():
        total = int(n1) + int(n2)
        result.config(text="Sum = " + str(total))
    else:
        result.config(text="Enter valid numbers")
    
#button   
Sum_Button= tk.Button(gui,text="sum",command=sum)
Sum_Button.pack()
result=tk.Label(gui,text="")
result.pack()
#mainloop
gui.mainloop()
