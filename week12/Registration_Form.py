#importing tkinter
import tkinter as tk
import csv
#creating a window
parent=tk.Tk()
parent.title("Registration Form")
parent.geometry("800x800")
#creating a label1 name
label1=tk.Label(parent,text="Name :")
label1.grid(row=0,column=0,columnspan=2)
#entry for label1 name
userInput1=tk.Entry(parent)
userInput1.grid(row=0,column=2)
#creating a label2 age
label1=tk.Label(parent,text="Age :")
label1.grid(row=1,column=0,columnspan=2)
#entry for label2 age
userInput2=tk.Entry(parent)
userInput2.grid(row=1,column=2)
#creating a label3 regID
label1=tk.Label(parent,text="Registration Id :")
label1.grid(row=2,column=0,columnspan=2)
#entry for label3 regID
userInput3=tk.Entry(parent)
userInput3.grid(row=2,column=2)
#creating a label4 phoneno
label1=tk.Label(parent,text="Phone Number :")
label1.grid(row=3,column=0,columnspan=2)
#entry for label4 phoneno
userInput4=tk.Entry(parent)
userInput4.grid(row=3,column=2)
#creating a label5 emailId
label1=tk.Label(parent,text="emailId :")
label1.grid(row=4,column=0,columnspan=2)
#entry for label5 emailId
userInput5=tk.Entry(parent)
userInput5.grid(row=4,column=2)


gender_var = tk.StringVar(value="others") 

# Create a Label
label_title = tk.Label(parent, text="gender:")
label_title.grid(row=0,column=6)

radio_male = tk.Radiobutton(parent, text="Male", variable=gender_var,value="Male")
radio_male.grid(row=0,column=7) 

radio_female = tk.Radiobutton(parent, text="Female", variable=gender_var, value="Female")
radio_female.grid(row=0,column=8)

radio_other = tk.Radiobutton(parent, text="Others", variable=gender_var, value="Others")
radio_other.grid(row=0,column=9)
#scrollbar bar select the course
label_scroll=tk.Label(parent,text="Course")
# save to csv file
def save_data():
    name = userInput1.get()
    age = userInput2.get()
    regId = userInput3.get()
    phno = userInput4.get()
    emailId = userInput5.get()
    data = [name, age,regId,phno,emailId]

    try:
        with open("data.csv", mode="a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
        print("Data saved successfully!")
        
        userInput1.delete(0, tk.END)
        userInput2.delete(0, tk.END)
        userInput3.delete(0, tk.END)
        userInput4.delete(0, tk.END)
        userInput5.delete(0, tk.END)

    except IOError as e:
        print(f"Error saving file: {e}")

# Save Button
save_button = tk.Button(parent, text="Save to CSV", command=save_data)
save_button.grid(row=6, column=9)

#run mainloop
parent.mainloop()