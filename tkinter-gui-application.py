import tkinter as tk    #import tkinter
from tkinter import ttk
from csv import DictWriter
import os 
win = tk.Tk()
win.title('Information Store')    #give a title name

#create labels
#name label
name_label = ttk.Label(win,text = "Enter Your Name : ")
name_label.grid(row=0, column=0, sticky = tk.W)

#email label
email_label = ttk.Label(win,text = "Enter Your Email : ")
email_label.grid(row=1, column = 0,sticky =tk.W)

#age label
age_label = ttk.Label(win,text = "Enter Your Age : ")
age_label.grid(row=2, column = 0, sticky = tk.W)

#mobile number label
mobile_label = ttk.Label(win, text = "Enter Your Mobile Number : ")
mobile_label.grid(row=3, column = 0, sticky =tk.W)

#gender label
gender_label = ttk.Label(win,text = "Select Your Gender : ")
gender_label.grid(row=4, column = 0, sticky = tk.W)

#Create entry box
#name entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width = 16, textvariable = name_var)
name_entrybox.grid(row=0 , column = 1)
name_entrybox.focus()

#email entry box
email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width = 16, textvariable = email_var)
email_entrybox.grid(row = 1, column = 1)

#age entry box
age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width = 16, textvariable= age_var)
age_entrybox.grid(row=2, column =1)

#mobile entry box
mobile_var = tk.StringVar()
mobile_entrybox = ttk.Entry(win, width= 16, textvariable = mobile_var)
mobile_entrybox.grid(row=3, column= 1)

#gender entry box
#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width = 13, textvariable = gender_var, state="readonly")
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row = 4, column=1)

#Create radio button
user_type = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text = 'Student', value='Student', variable = user_type)
radiobtn1.grid(row=5, column=0)

radiobtn2 = ttk.Radiobutton(win, text = 'Teacher', value='Teacher', variable = user_type)
radiobtn2.grid(row=5, column=1)

#create check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win,text='Click Check Button to Subscribe Our Newsletter',variable=checkbtn_var)
checkbtn.grid(row=6,columnspan=3)

#Create button code action function
def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    usermobile = mobile_var.get()
    usergender = gender_var.get()
    usertype = user_type.get()
    #change value 0,1 to Yes or No
    if checkbtn_var.get() == 0:
        subscribe = 'No'
    else:
        subscribe = 'Yes'

    #write to csv file code here
    with open('file.csv', 'a', newline = '') as f:
        dict_writer = DictWriter(f, fieldnames=['User Name', 'User Age', 'User Email','User Mobile', 'User Gender', 'User Type', 'Subscribe'])
        if os.stat('file.csv').st_size == 0:        #if file is not empty than header write else not
            dict_writer.writeheader()
       
        dict_writer.writerow({
            'User Name' : username,
            'User Age' : userage,
            'User Email' : useremail,
            'User Mobile' : usermobile,
            'User Gender' : usergender,
            'User Type' : usertype,
            'Subscribe' : subscribe
        })
    #Change color after submit button
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    mobile_entrybox.delete(0, tk.END)
    name_label.configure(foreground = 'Blue')
    email_label.configure(foreground = 'Blue')
    age_label.configure(foreground = 'Blue')
    mobile_label.configure(foreground = 'Blue')
    gender_label.configure(foreground = 'Blue')

#submit button
submit_button = ttk.Button(win, text = "Submit", command = action)  
submit_button.grid(row=7, column=0)
win.mainloop()      #application is not closed auto
