import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def update_data():
    first_name_to_update = first_name_entry.get()
    
    if first_name_to_update:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        
        update_query = '''
            UPDATE Student_Data
            SET lastname=?, title=?, age=?, nationality=?, Weight=?, Height=?, Memborship=?
            WHERE firstname=?
        '''
        
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        Weight = weight_entry.get()
        Height = height_entry.get()
        Memborship = m_combobox.get()
        
        cursor.execute(update_query, (lastname, title, age, nationality, Weight, Height, Memborship, first_name_to_update))
        
        conn.commit()
        conn.close()
    else:
        tkinter.messagebox.showwarning(title="Error", message="Please enter the first name to update.")


def delete():
    first_name_to_delete = first_name_entry.get()
    
    if first_name_to_delete:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        
        delete_query = "DELETE FROM Student_Data WHERE firstname = ?"
        cursor.execute(delete_query, (first_name_to_delete,))

        
        conn.commit()
        conn.close()

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Personal info
            Weight=weight_entry.get()
            Height=height_entry.get()
            Memborship=m_combobox.get()
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Weight: ", Weight, "# Height: ", Height)
            print("Memborship status", Memborship)
            print("------------------------------------------")
            
            # Create Table
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
                    Weight INT,Height INT, Memborship TEXT,primary key(firstname))
            '''
            conn.execute(table_create_query)
            
            # Insert Data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
            age, nationality,Weight,Height,Memborship) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title,
                                  age, nationality,  Weight,Height, Memborship)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

            
                
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("GYM REGISTRATION FORM")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=1)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

#    
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=0)
title_combobox.grid(row=1, column=0)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Personal Info

p_frame = tkinter.LabelFrame(frame,text="Personal Info")
p_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

weight_label=tkinter.Label(p_frame,text="Weight")
weight_entry=tkinter.Entry(p_frame)
weight_label.grid(row=0,column=0)
weight_entry.grid(row=1,column=0)

height_label=tkinter.Label(p_frame,text="Height")
height_entry=tkinter.Entry(p_frame)
height_label.grid(row=0,column=1)
height_entry.grid(row=1,column=1)

m_label = tkinter.Label(p_frame, text="Memborship")
m_combobox = ttk.Combobox(p_frame, values=["Regular","Pro","VIP"])
m_label.grid(row=0, column=2)
m_combobox.grid(row=1, column=2)


for widget in p_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

but_frame = tkinter.LabelFrame(frame, text=" ")
but_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)
# Button
button = tkinter.Button(but_frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
#Button 
button=tkinter.Button(but_frame,text="Delete",command=delete)
button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

button=tkinter.Button(but_frame,text="Update",command=update_data)
button.grid(row=3, column=2, sticky="news", padx=20, pady=10)
 


window.mainloop()