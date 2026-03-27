import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Hello App")
window.geometry("300x200")

# Create a label to display Hello World
label = tk.Label(window, text="Hello World!", font=("Arial", 16))
label.pack(pady=50)

# Run the application
window.mainloop()