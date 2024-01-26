import tkinter as tk
from tkinter import *
from ttkbootstrap import Style, ttk,DateEntry

# Create the main window
root = tk.Tk()
root.title("Faculty Attendance View")

style = Style(theme="flatly") 
frame1 = ttk.Frame(root, borderwidth=2, relief="solid",)
frame1.grid(row=1, column=0, sticky="nsew")
root.columnconfigure(0, weight=2)  


entries_info = {
    "Class Name": {"type": "dropdown", "options": ["FE Comps A", "FE Comps B", "FE Comps C", "SE Comps A", "SE Comps B", "SE Comps C", "TE Comps A", "TE Comps B", "TE Comps C", "BE Comps A", "BE Comps B", "BE Comps C", "FE I.T A", "FE I.T B", "FE I.T C", "SE I.T A", "SE I.T B", "SE I.T C", "TE I.T A", "TE I.T B", "TE I.T C", "BE I.T A", "BE I.T B", "BE I.T C", "FE Mech A", "FE Mech B", "FE Mech C", "SE Mech A", "SE Mech B", "SE Mech C", "TE Mech A", "TE Mech B", "TE Mech C", "BE Mech A", "BE Mech B", "BE Mech C", "FE Civil A", "FE Civil B", "FE Civil C", "SE Civil A", "SE Civil B", "SE Civil C", "TE Civil A", "TE Civil B", "TE Civil C", "BE Civil A", "BE Civil B", "BE Civil C", "FE EXTC A", "FE EXTC B", "FE EXTC C", "SE EXTC A", "SE EXTC B", "SE EXTC C", "TE EXTC A", "TE EXTC B", "TE EXTC C", "BE EXTC A", "BE EXTC B", "BE EXTC C", "FE Electrical A", "FE Electrical B", "FE Electrical C", "SE Electrical A", "SE Electrical B", "SE Electrical C", "TE Electrical A", "TE Electrical B", "TE Electrical C", "BE Electrical A", "BE Electrical B", "BE Electrical C"]},
    "Student ID": {"type": "entry"},
    "Student Name": {"type": "entry"},
    "Subject Name": {"type": "entry"},
    "Roll No": {"type": "dropdown","options": list(range(1, 101))},
    "Date": {"type": "datetime"},
    "Time Slot": {"type": "dropdown", "options":["10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM"]},
    "Attendance Status": {"type": "dropdown","options":["Present","Absent"]}
}

entries = []

for i, (label_text, info) in enumerate(entries_info.items()):
    label = ttk.Label(frame1, text=label_text, font=("Helvetica", 14))
    label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)

    if info["type"] == "dropdown":
        entry = ttk.Combobox(frame1, values=info["options"], width=34)
    elif info["type"] =="datetime":
        entry = DateEntry(frame1,width=31)
    else:
        entry = ttk.Entry(frame1, width=36)

    entry.grid(row=i + 1, column=1, sticky="e", padx=10, pady=5)
    entries.append(entry)

submit_button = ttk.Button(frame1, text="Submit",bootstyle="success")
submit_button.grid(row=len(entries_info)+1,column=0, sticky="w", pady=10, padx=70,)

Back_button = ttk.Button(frame1, text="Back",bootstyle="secondary")
Back_button.grid(row=len(entries_info) + 1, column=1, sticky="w", pady=10,padx=70)

Update_button = ttk.Button(frame1, text="Update",bootstyle="danger")
Update_button.grid(row=len(entries_info)+2, column=0, sticky="w", pady=10, padx=70)

Reset_button = ttk.Button(frame1, text="Reset",bootstyle="primary")
Reset_button.grid(row=len(entries_info) + 2, column=1, sticky="w", pady=10,padx=70)

importCSV_button = ttk.Button(frame1, text="Import CSV",width=10,bootstyle="success")
importCSV_button.grid(row=len(entries_info) + 3, column=0, pady=10,padx=60,sticky="w")

exportCSV_button = ttk.Button(frame1, text="export CSV",width=10,bootstyle="warning",)
exportCSV_button.grid(row=len(entries_info) + 3, column=1, pady=10,padx=60,sticky="w")

frame2 = ttk.Frame(root, borderwidth=2, relief="solid")
frame2.grid(row=1, column=1, sticky="nsew")
root.columnconfigure(1, weight=9) 



text_label = ttk.Label(frame2, text="Search System.", font=("Helvetica", 12,"bold"), padding=10)
text_label.grid(row=0, column=0,sticky="w")

# Create a sub-frame for the form
form_frame = ttk.Frame(frame2, padding=(10, 10, 10, 0))
form_frame.grid(row=1, column=0, pady=10, padx=(3, 3))


form_entries_info = {
    "Search By": {"type": "dropdown","options":["ID","Name"]},
    "Faculty Name":{"type":"entry"},
    "Class Name": {"type": "dropdown", "options": ["Math", "Science", "English", "History"]},
    "Subject Name": {"type": "datetime"},
}

form_entries = []

for i, (label_text, info) in enumerate(form_entries_info.items()):
    label = ttk.Label(form_frame, text=label_text, font=("Helvetica", 10))
    label.grid(row=1, column=i * 2, sticky="e", padx=10, pady=5)

    if info["type"] == "dropdown":
        entry = ttk.Combobox(form_frame, values=info["options"], width=10)
    
    else:
        entry = ttk.Entry(form_frame, width=10)

    entry.grid(row=1, column=i * 2 + 1, sticky="w", padx=10, pady=5)
    form_entries.append(entry)

Search_button = ttk.Button(form_frame, text="Search", bootstyle="primary")
Search_button.grid(row=2, column=3, pady=10)


ShowAll_button = ttk.Button(form_frame, text="Show All", bootstyle="primary")
ShowAll_button.grid(row=2, column=4 , pady=10)

# table_frame = ttk.Frame(frame2)
# table_frame.grid(row=2, column=0, pady=20, padx=(3, 3))


# columns = ["Class Name", "Student ID", "Student Name", "Roll No", "Date", "Time Slot", "Attendance Status"]
# table = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)
# heading_frame = ttk.Frame(table_frame)

# for col in columns:
#     label = ttk.Label(heading_frame, text=col, font=("Helvetica", 10, "bold"), anchor="center",)
#     label.grid(row=0, column=columns.index(col), ipadx=5, ipady=2)

# for col in columns:
#     table.heading(col, text=col, anchor="center")

# #sample data
# data = [
#     ["Math", "001", "John", "101", "2022-12-01", "10:00 AM", "Present"],
#     ["Science", "002", "alice", "102", "2022-12-01", "11:00 AM", "Absent"],
#     ["English", "003", "Bob", "103", "2022-12-02", "09:30 AM", "Present"]
# ]

# for row in data:
#     table.insert("", "end", values=row)

# for col in columns:
#     table.column(col, anchor="center", width=119, stretch=False)

# for i in range(len(data)):
#     table.insert("", "end", values=[""] * len(columns))

# table.grid(row=0, column=0, pady=10)



# title_label = ttk.Label(root, text="Faculty Attendance View", font=("Helvetica", 16, "bold"), style="TLabel", padding=20)
# title_label.grid(row=0, column=0, columnspan=2)




table_frame = ttk.Frame(frame2)
table_frame.grid(row=2, column=0, pady=20, padx=(3, 3))


columns = ["Class Name", "Student ID", "Student Name", "Subject Name", "Roll No","Date","TimeSlot","Attendance Status"]

scrollhor=ttk.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="info")
scrollver=ttk.Scrollbar(table_frame,orient=VERTICAL,bootstyle="info")
table = ttk.Treeview(table_frame, columns=columns, show="headings",height=12,xscrollcommand=scrollhor.set,yscrollcommand=scrollver.set)
scrollhor.pack(side=BOTTOM,fill=X)
scrollver.pack(side=RIGHT,fill=Y)
scrollhor.config(command=table.xview)
scrollver.config(command=table.yview)

heading_frame = ttk.Frame(table_frame)

#making the table
table.heading("Class Name",text="Class Name")
table.heading("Student ID",text="Student ID")
table.heading("Student Name",text="Student Name")
table.heading("Subject Name",text="Subject Name")
table.heading("Roll No",text="Roll No")
table.heading("Date",text="Date")
table.heading("TimeSlot",text="TimeSlot")
table.heading("Attendance Status",text="Attdendance Status")
table["show"]="headings"

table.column("Class Name",width=100)
table.column("Student ID",width=100)
table.column("Student Name",width=100)
table.column("Subject Name",width=100)
table.column("Roll No",width=90)
table.column("Date",width=100)
table.column("TimeSlot",width=90)
table.column("Attendance Status",width=120)

table.pack(fill=BOTH,expand=10)



# frame3 = ttk.Frame(frame1, borderwidth=0, relief="solid")
# frame3.grid(row=8, column=0, sticky="nsew",columnspan=2)
# root.columnconfigure(0, weight=1) 

# save_button = ttk.Button(frame3, text="Save",width=10,bootstyle="success")
# save_button.grid(row=0, column=0,pady=20, padx=10)

# update_button = ttk.Button(frame3, text="Update",width=10)
# update_button.grid(row=0, column=1,pady=20, padx=10)

# delete_button = ttk.Button(frame3, text="Delete",width=10,bootstyle="danger")
# delete_button.grid(row=0, column=2,pady=20, padx=10)

# reset_button = ttk.Button(frame3, text="Reset",width=10,bootstyle="warning")
# reset_button.grid(row=0, column=3, pady=20,padx=10)


# importCSV_button = ttk.Button(frame3, text="Import CSV",width=10,bootstyle="success")
# importCSV_button.grid(row=1, column=0, pady=20,padx=10, columnspan=2,sticky="e")

# exportCSV_button = ttk.Button(frame3, text="export CSV",width=10,bootstyle="warning",)
# exportCSV_button.grid(row=1, column=1, pady=20,padx=10,columnspan=2,sticky="e")

# Back_button = ttk.Button(frame3, text="Back",width=10,bootstyle="dark")
# Back_button.grid(row=2, column=1,columnspan=2, sticky="s",pady=20,padx=3)

title_label = ttk.Label(root, text="FACULTY ATTENDANCE VIEW", font=("Helvetica", 16, "bold"), style="TLabel", padding=20)
title_label.grid(row=0, column=0, columnspan=2)

root.mainloop()
