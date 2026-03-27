import tkinter as tk

gui = tk.Tk()
gui.title("Geometry Methods ")
gui.geometry("800x800")

# PACK 
frame1 = tk.Frame(gui, bg="blue")
frame1.pack(fill="both", expand=True)

label1 = tk.Label(frame1, text="Using pack()", bg="lightblue")
label1.pack(pady=10)

button1 = tk.Button(frame1, text="Button 1",bg="pink")
button1.pack(pady=5)

# GRID 
frame2 = tk.Frame(gui, bg="lightgreen")
frame2.pack(fill="both", expand=True)

label2 = tk.Label(frame2, text="Using grid()", bg="lightgreen")
label2.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(frame2, text="Name:").grid(row=1, column=0)
tk.Entry(frame2).grid(row=1, column=1)

tk.Label(frame2, text="Age:").grid(row=2, column=0)
tk.Entry(frame2).grid(row=2, column=1)

#  PLACE 
frame3 = tk.Frame(gui, bg="yellow")
frame3.pack(fill="both", expand=True)

label3 = tk.Label(frame3, text="Using place()", bg="yellow")
label3.place(x=150, y=20)

# Function for button click
def show_message():
    result.config(text="Hi Aishwarya",font=("Times New Roman",24))

button2 = tk.Button(frame3, text="Click Me", command=show_message)
button2.place(x=180, y=60)

# Label to display message
result= tk.Label(frame3, text="", bg="yellow")
result.place(x=170, y=100)

# Run GUI
gui.mainloop()