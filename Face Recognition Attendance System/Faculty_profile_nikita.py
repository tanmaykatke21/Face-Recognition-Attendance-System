import tkinter as tk
from tkinter import *
from ttkbootstrap import Style, ttk, DateEntry
import mysql.connector

# Create the main window
root = tk.Tk()
root.title("Faculty Profile")

style = Style(theme="yeti")
frame1 = ttk.Frame(root, borderwidth=2, relief="solid",)
frame1.grid(row=1, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)  

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'nikita@2002',
    'database': 'major_project'
}

# Function to insert data into the database
def insert_data():
    # Get data from entry widgets
    faculty_id = entries[0].get()
    first_name = entries[1].get()
    last_name = entries[2].get()
    email = entries[3].get()
    phone_no = entries[4].get()

    # MySQL connection
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert data into the database
        query = "INSERT INTO Faculty (faculty_id, Faculty_first_name, Faculty_last_name,Email,phone_no) VALUES (%s, %s, %s, %s, %s)"
        values = (faculty_id, first_name, last_name, email, phone_no)
        cursor.execute(query, values)

        # Commit changes and close the connection
        connection.commit()
        connection.close()

        # Clear entry widgets after successful insertion
        for entry in entries:
            entry.delete(0, END)

        print("Data inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

entries_info = {
    "Faculty ID": {"type": "entry"},
    "First Name": {"type": "entry"},
    "Last Name": {"type": "entry"},
    "Email ID": {"type": "entry"},
    "Phone no.": {"type": "entry"}
}

entries = []
label_name=ttk.Label(frame1, text="Faculty Details", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

for i, (label_text, info) in enumerate(entries_info.items()):
    label = ttk.Label(frame1, text=label_text, font=("Helvetica", 12))
    label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)

    if info["type"] == "dropdown":
        entry = ttk.Combobox(frame1, values=info["options"], width=34)
    else:
        entry = ttk.Entry(frame1, width=36)

    entry.grid(row=i + 1, column=1, sticky="e", padx=10, pady=5)
    entries.append(entry)

frame2 = ttk.Frame(root, borderwidth=2, relief="solid")
frame2.grid(row=1, column=1, sticky="nsew")
root.columnconfigure(1, weight=9) 


# Create a sub-frame for the form
form_frame = ttk.Frame(frame2, padding=(10, 10, 10, 0))
form_frame.grid(row=1, column=0, pady=10, padx=(3, 3))


form_entries_info = {
    "Search By": {"type": "dropdown", "options": ["Faculty_id","Faculty_name"]},
    "Search Info": {"type": "entry"},
}

form_entries = []

label_name=ttk.Label(frame2, text="Search System", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

for i, (label_text, info) in enumerate(form_entries_info.items()):
    label = ttk.Label(form_frame, text=label_text, font=("Helvetica", 12))
    label.grid(row=0, column=i * 2, sticky="e", padx=10, pady=5)

    if info["type"] == "dropdown":
        entry = ttk.Combobox(form_frame, values=info["options"], width=14)
    elif info["type"] =="datetime":
        # entry = ttk.DateEntry(form_frame,bootstyle="success")
        entry = DateEntry(form_frame,bootstyle="success")
    else:
        entry = ttk.Entry(form_frame, width=16)

    entry.grid(row=0, column=i * 2 + 1, sticky="w", padx=10, pady=2)
    form_entries.append(entry)

search_button = ttk.Button(form_frame, text="Search",bootstyle="primary")
search_button.grid(row=0, column=5,padx=10 ,pady=2) #, columnspan=len(form_entries_info) * 2

show_all_button = ttk.Button(form_frame, text="Show all",bootstyle="secondary")
show_all_button.grid(row=0, column=6, pady=2,sticky="e") #, columnspan=len(form_entries_info) * 2,


table_frame = ttk.Frame(frame2)
table_frame.grid(row=2, column=0, pady=20, padx=(3, 3))


columns = ["Faculty ID", "First Name", "Last Name", "Email", "Phone no."]

scrollhor=ttk.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="info")
scrollver=ttk.Scrollbar(table_frame,orient=VERTICAL,bootstyle="info")
table = ttk.Treeview(table_frame, columns=columns, show="headings",height=500,xscrollcommand=scrollhor.set,yscrollcommand=scrollver.set)
scrollhor.pack(side=BOTTOM,fill=X)
scrollver.pack(side=RIGHT,fill=Y)
scrollhor.config(command=table.xview)
scrollver.config(command=table.yview)

heading_frame = ttk.Frame(table_frame)

#making the table
table.heading("Faculty ID",text="Faculty ID")
table.heading("First Name",text="First Name")
table.heading("Last Name",text="Last Name")
table.heading("Email",text="Email")
table.heading("Phone no.",text="Phone no.")

table["show"]="headings"

table.column("Faculty ID",width=125)
table.column("First Name",width=125)
table.column("Last Name",width=125)
table.column("Email",width=125)
table.column("Phone no.",width=125)

table.pack(fill=BOTH,expand=10)




frame3 = ttk.Frame(frame1, borderwidth=0, relief="solid")
frame3.grid(row=8, column=0, sticky="nsew",columnspan=2)
root.columnconfigure(0, weight=1) 

save_button = ttk.Button(frame3, text="Save",width=10,bootstyle="success",command=insert_data)
save_button.grid(row=0, column=0,pady=20, padx=10)

update_button = ttk.Button(frame3, text="Update",width=10)
update_button.grid(row=0, column=1,pady=20, padx=10)

delete_button = ttk.Button(frame3, text="Delete",width=10,bootstyle="danger")
delete_button.grid(row=0, column=2,pady=20, padx=10)

reset_button = ttk.Button(frame3, text="Reset",width=10,bootstyle="warning")
reset_button.grid(row=0, column=3, pady=20,padx=10)

Back_button = ttk.Button(frame3, text="Back",width=10,bootstyle="dark")
Back_button.grid(row=1, column=1,columnspan=2, sticky="s",pady=3,padx=3)





title_label = ttk.Label(root, text="FACULTY PROFILE", font=("Helvetica", 20, "bold"), style="TLabel", padding=20)
title_label.grid(row=0, column=0, columnspan=2)

root.mainloop()


