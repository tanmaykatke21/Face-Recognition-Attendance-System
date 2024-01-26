import tkinter as tk
from tkinter import *
from ttkbootstrap import Style, ttk, DateEntry

#==================================ROOT WINDOW=================================

root = tk.Tk()
root.title("Faculty Subject Allotment")
style = Style(theme="yeti")

#===================================LEFT FRAME=================================

frame1 = ttk.Frame(root, borderwidth=2, relief="solid",)
frame1.grid(row=1, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)

entries_info = {
    "Faculty id": {"type": "entry"},
    "Class name": {"type": "dropdown", "options": ["FE Comps A", "FE Comps B", "FE Comps C", 
                                                   "SE Comps A", "SE Comps B", "SE Comps C", 
                                                   "TE Comps A", "TE Comps B", "TE Comps C", 
                                                   "BE Comps A", "BE Comps B", "BE Comps C",
                                                   "FE I.T A", "FE I.T B", "FE I.T C", 
                                                   "SE I.T A", "SE I.T B", "SE I.T C", 
                                                   "TE I.T A", "TE I.T B", "TE I.T C", 
                                                   "BE I.T A", "BE I.T B", "BE I.T C",
                                                   "FE Mech A", "FE Mech B", "FE Mech C", 
                                                   "SE Mech A", "SE Mech B", "SE Mech C", 
                                                   "TE Mech A", "TE Mech B", "TE Mech C", 
                                                   "BE Mech A", "BE Mech B", "BE Mech C",
                                                   "FE Civil A", "FE Civil B", "FE Civil C", 
                                                   "SE Civil A", "SE Civil B", "SE Civil C", 
                                                   "TE Civil A", "TE Civil B", "TE Civil C", 
                                                   "BE Civil A", "BE Civil B", "BE Civil C",
                                                   "FE EXTC A", "FE EXTC B", "FE EXTC C", 
                                                   "SE EXTC A", "SE EXTC B", "SE EXTC C", 
                                                   "TE EXTC A", "TE EXTC B", "TE EXTC C", 
                                                   "BE EXTC A", "BE EXTC B", "BE EXTC C",
                                                   "FE Electrical A", "FE Electrical B", "FE Electrical C", 
                                                   "SE Electrical A", "SE Electrical B", "SE Electrical C", 
                                                   "TE Electrical A", "TE Electrical B", "TE Electrical C", 
                                                   "BE Electrical A", "BE Electrical B", "BE Electrical C",]},
    "Last Name": {"type": "entry"},
}

entries = []
label_name=ttk.Label(frame1, text="Allotment Details", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

for i, (label_text, info) in enumerate(entries_info.items()):
    label = ttk.Label(frame1, text=label_text, font=("Helvetica", 12))
    label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)

    if info["type"] == "dropdown" and label_text == "Faculty id":
        entry = ttk.Entry(frame1, width=36)  # Use Entry instead of Combobox for "Faculty id"
    elif info["type"] == "dropdown":
        entry = ttk.Combobox(frame1, values=info["options"], width=34)
    else:
        entry = ttk.Entry(frame1, width=36)

    entry.grid(row=i + 1, column=1, sticky="e", padx=10, pady=5)
    entries.append(entry)

class_name_var = StringVar()
class_name_var.set(entries_info["Class name"]["options"][0])  # Set default value
class_name_dropdown = ttk.Combobox(frame1, values=entries_info["Class name"]["options"], width=34, textvariable=class_name_var)
class_name_dropdown.grid(row=2, column=1, sticky="e", padx=10, pady=5)
entries.append(class_name_dropdown)


frame4 = ttk.Frame(frame1, borderwidth=0, relief="solid")
frame4.grid(row=3, column=0, columnspan=2, sticky="nsew")

table_frame = ttk.Frame(frame4)
table_frame.grid(row=2, column=0, pady=20, padx=(3, 3))

columns = ["Select", "Subject name", "Faculty ID"]

scrollhor=ttk.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="info")
scrollver=ttk.Scrollbar(table_frame,orient=VERTICAL,bootstyle="info")
table = ttk.Treeview(table_frame, columns=columns, show="headings",height=15,xscrollcommand=scrollhor.set,yscrollcommand=scrollver.set)
scrollhor.pack(side=BOTTOM,fill=X)
scrollver.pack(side=RIGHT,fill=Y)
scrollhor.config(command=table.xview)
scrollver.config(command=table.yview)

heading_frame = ttk.Frame(table_frame)

#making the table
table.heading("Select",text="Select")
table.heading("Subject name",text="Subject name")
table.heading("Faculty ID",text="Faculty ID")

table["show"]="headings"

table.column("Select",width=133)
table.column("Subject name",width=135)
table.column("Faculty ID",width=135)

table.pack(fill=BOTH,expand=10)

frame5 = ttk.Frame(frame1, borderwidth=0, relief="solid")
frame5.grid(row=8, column=0, sticky="nsew",columnspan=2)
root.columnconfigure(0, weight=1) 

save_button = ttk.Button(frame5, text="Save",width=10,bootstyle="success")
save_button.grid(row=0, column=0,pady=3, padx=10)

update_button = ttk.Button(frame5, text="Update",width=10)
update_button.grid(row=0, column=1,pady=3, padx=10)

delete_button = ttk.Button(frame5, text="Delete",width=10,bootstyle="danger")
delete_button.grid(row=0, column=2,pady=3, padx=10)

reset_button = ttk.Button(frame5, text="Reset",width=10,bootstyle="warning")
reset_button.grid(row=0, column=3, pady=3,padx=10)


#=========================RIGHT FRAME================================

frame2 = ttk.Frame(root, borderwidth=2, relief="solid")
frame2.grid(row=1, column=1, sticky="nsew")
root.columnconfigure(1, weight=9)

# Create a sub-frame for the form
form_frame = ttk.Frame(frame2, borderwidth=2,padding=(2,2,2, 0))
form_frame.grid(row=1, column=0, pady=2, padx=3)

form_entries_info = {
    "Search By": {"type": "dropdown", "options": ["Faculty_id","Subject"]},
    "Search Info": {"type": "entry"},
}

form_entries = []

label_name=ttk.Label(frame2, text="Search System", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=3)

for i, (label_text, info) in enumerate(form_entries_info.items()):
    label = ttk.Label(form_frame, text=label_text, font=("Helvetica", 12))
    label.grid(row=0, column=i * 2, sticky="e", padx=3, pady=0)

    if info["type"] == "dropdown":
        entry = ttk.Combobox(form_frame, values=info["options"], width=14)
    elif info["type"] =="datetime":
        # entry = ttk.DateEntry(form_frame,bootstyle="success")
        entry = DateEntry(form_frame,bootstyle="success")
    else:
        entry = ttk.Entry(form_frame, width=16)

    entry.grid(row=0, column=i * 2 + 1, sticky="w", padx=3, pady=2)
    form_entries.append(entry)

search_button = ttk.Button(form_frame, text="Search",bootstyle="primary",width=10)
search_button.grid(row=1, column=1,padx=10 ,pady=5)

show_all_button = ttk.Button(form_frame, text="Show all",bootstyle="secondary",width=10)
show_all_button.grid(row=1, column=3, pady=5,sticky="n") 


table_frame = ttk.Frame(frame2)
table_frame.grid(row=2, column=0, pady=20, padx=(3, 3))

columns = ["Allotment ID", "Faculty ID", "Subject name"]

scrollhor=ttk.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="info")
scrollver=ttk.Scrollbar(table_frame,orient=VERTICAL,bootstyle="info")
table = ttk.Treeview(table_frame, columns=columns, show="headings",height=15,xscrollcommand=scrollhor.set,yscrollcommand=scrollver.set)
scrollhor.pack(side=BOTTOM,fill=X)
scrollver.pack(side=RIGHT,fill=Y)
scrollhor.config(command=table.xview)
scrollver.config(command=table.yview)

heading_frame = ttk.Frame(table_frame)

#making the table
table.heading("Allotment ID",text="Allotment ID")
table.heading("Faculty ID",text="Faculty ID")
table.heading("Subject name",text="Subject name")

table["show"]="headings"

table.column("Allotment ID",width=125)
table.column("Faculty ID",width=125)
table.column("Subject name",width=125)

table.pack(fill=BOTH,expand=10)

Back_button = ttk.Button(frame2, text="Back",width=10,bootstyle="dark")
Back_button.grid(row=3, column=0,columnspan=2,sticky="nsew",pady=3,padx=3)

title_label = ttk.Label(root, text="FACULTY SUBJECT ASSIGNMENT", font=("Helvetica", 20, "bold"), style="TLabel", padding=20)
title_label.grid(row=0, column=0, columnspan=2)

root.mainloop()
