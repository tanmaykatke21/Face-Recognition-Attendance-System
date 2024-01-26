import tkinter as tk
from tkinter import *
from ttkbootstrap import Style, ttk
import mysql.connector
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Faculty Profile")
style = Style(theme="yeti")

title_label = ttk.Label(root, text="FACULTY PROFILE", font=("Helvetica", 20, "bold"), style="TLabel", padding=20)
title_label.grid(row=0, column=0, columnspan=2)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'nikita@2002',
    'database': 'major_project'
}

#=========variable declaration=========
var_first_name=StringVar()
var_last_name=StringVar()
var_faculty_id=StringVar()
var_email_id=StringVar()
var_ph_no=StringVar()
var_search_by=StringVar()
var_entry_search=StringVar()

#================Functions=============================

#-------------Fetch Data---------------
def fetch_data():
        conn=mysql.connector.connect(**db_config)

        my_cursor=conn.cursor()
        my_cursor.execute("select * from Faculty")
        data_fetch=my_cursor.fetchall()

        if len(data_fetch)!=0:
            faculty_table.delete(*faculty_table.get_children())
            for i in data_fetch:
                faculty_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#------------------get cursor-----------------

def get_cursor(event=" "):
    try:
        cursor_focus = faculty_table.focus()
        table_content = faculty_table.item(cursor_focus)
        data_cursor = table_content["values"]

        if data_cursor:
            var_faculty_id.set(data_cursor[0])
            var_first_name.set(data_cursor[1])
            var_last_name.set(data_cursor[2])
            var_email_id.set(data_cursor[3])
            var_ph_no.set(data_cursor[4])
    except Exception as e:
        messagebox.showerror("Issue", e)

#-------------Save Data----------------
def save():
    conn=mysql.connector.connect(**db_config)
    my_cursor=conn.cursor()

    faculty_id=var_faculty_id.get()
    first_name=var_first_name.get()
    last_name=var_last_name.get()
    email_id=var_email_id.get()
    ph_no=var_ph_no.get()

    if faculty_id=="":
        messagebox.showerror("Issue","Fill faculty id field",parent=root)

    elif first_name=="":
        messagebox.showerror("Issue","Fill first name field",parent=root)

    elif last_name=="":
        messagebox.showerror("Issue","Fill last name field",parent=root)

    elif email_id=="":
        messagebox.showerror("Issue","Fill email id field",parent=root)

    elif ph_no=="":
        messagebox.showerror("Issue","Fill phone no. field")

    else:
        try:
            my_cursor.execute("insert into Faculty values (%s,%s,%s,%s,%s)", (faculty_id,first_name,last_name,email_id,ph_no))
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Success","Faculty details added",parent=root)	
    
        except ValueError:
            messagebox.showerror("Issue","Please enter correct values for Phone no. field.\nMake sure not to keep any field blank")
        
        except mysql.connector.IntegrityError:
            messagebox.showerror("Issue","Faculty-ID,Email-ID and Phone no. must be unique and cannot be repeated")

        except mysql.connector.Error as err:
            if err.errno == 1366:
                messagebox.showerror("Issue","Phone no. must contain digits only")

        except Exception as e:
            messagebox.showerror("Issue",e)

        finally:
            if conn is not None:
                conn.close()

#-------------------------reset function-------------------------
def reset_data():
    var_faculty_id.set("")
    var_first_name.set("")
    var_last_name.set("")
    var_email_id.set("")
    var_ph_no.set("")

#--------------------------back function----------------------------
def back():
    root.destroy()

#--------------------------delete function--------------------------
def delete_data():
        if var_faculty_id.get()=="":
             messagebox.showerror("ERROR","Faculty id is required",parent=root)
        else:
            try:
                delete=messagebox.askyesno("Deletion Details","Do you want to delete this Faculty's Details?",parent=root)
                if delete>0:
                    conn=mysql.connector.connect(**db_config)
                    my_cursor=conn.cursor()
                    sql="delete from Faculty where Faculty_id=%s"
                    val=(var_faculty_id.get(),) #here extra comma to avoid error which can occur sometimes
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Faculty Deleted",parent=root)

            except Exception as e:
                messagebox.showerror("ERROR",f"Due To: {str(e)}",parent=root)


#---------------------------update function--------------------------
def update_data():
    conn = mysql.connector.connect(**db_config)
    my_cursor = conn.cursor()

    faculty_id = var_faculty_id.get()
    first_name = var_first_name.get()
    last_name = var_last_name.get()
    email_id = var_email_id.get()
    ph_no = var_ph_no.get()

    if faculty_id == "" or first_name == "" or last_name == "" or email_id == "" or ph_no == "":
        messagebox.showerror("Issue", "Fill all fields", parent=root)
    else:
        try:
            update_msg = messagebox.askyesno("Update", "Do you want to Update this Faculty's Details?", parent=root)
            if update_msg > 0:
                sql = "update Faculty set Faculty_first_name=%s, Faculty_last_name=%s, Email=%s, phone_no=%s where Faculty_id=%s"
                val = (first_name, last_name, email_id, ph_no, faculty_id,)
                my_cursor.execute(sql, val)
                conn.commit()
                fetch_data()
                messagebox.showinfo("Success", "Faculty details Updated", parent=root)
            else:
                if not update_msg:
                    return
        except Exception as e:
            messagebox.showerror("ERROR", f"Due To: {str(e)}", parent=root)
        finally:
            conn.close()

#------------------------------------Search Data-----------------------------
def search_data():
    if var_search_by.get()=="" or var_entry_search.get()=="":
        messagebox.showerror("ERROR","Please fill all fields",parent=root)
    else:
        try:
            conn = mysql.connector.connect(**db_config)            
            my_cursor=conn.cursor()
            if var_search_by.get()=="Faculty ID":
                my_cursor.execute("select * from Faculty where Faculty_id LIKE '%"+str(var_entry_search.get())+"%'")
            elif var_search_by.get()=="Faculty First Name":
                my_cursor.execute("select * from Faculty where Faculty_first_name LIKE '%"+str(var_entry_search.get())+"%'")
            elif var_search_by.get()=="Faculty Last Name":
                my_cursor.execute("select * from Faculty where Faculty_last_name LIKE '%"+str(var_entry_search.get())+"%'")

            data=my_cursor.fetchall()
            if len(data)!=0:
                faculty_table.delete(*faculty_table.get_children())
                for i in data:
                    faculty_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        except Exception as e:
            messagebox.showerror("ERROR",f"Due To: {str(e)}",parent=root)


#==============================UI====================================

#-------------------Left Frame--------------------------
left_frame = ttk.Frame(root, borderwidth=2, relief="solid")
left_frame.grid(row=1, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)

label_faculty_details=ttk.Label(left_frame, text="Faculty Details", font=("Helvetica", 14,"bold"))
label_faculty_details.grid(row=0, column=0, sticky="w", padx=10, pady=5)

label_faculty_id=ttk.Label(left_frame, text="Faculty ID", font=("Helvetica", 12))
label_faculty_id.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_faculty_id = ttk.Entry(left_frame, width=36,textvariable=var_faculty_id)
entry_faculty_id.grid(row=1, column=1, sticky="w", padx=10, pady=5)

label_faculty_first_name=ttk.Label(left_frame, text="First Name", font=("Helvetica", 12))
label_faculty_first_name.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_faculty_first_name = ttk.Entry(left_frame, width=36,textvariable=var_first_name)
entry_faculty_first_name.grid(row=2, column=1, sticky="w", padx=10, pady=5)

label_faculty_last_name=ttk.Label(left_frame, text="Last Name", font=("Helvetica", 12))
label_faculty_last_name.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_faculty_last_name = ttk.Entry(left_frame, width=36,textvariable=var_last_name)
entry_faculty_last_name.grid(row=3, column=1, sticky="w", padx=10, pady=5)

label_faculty_email_id=ttk.Label(left_frame, text="Email ID", font=("Helvetica", 12))
label_faculty_email_id.grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_faculty_email_id = ttk.Entry(left_frame, width=36,textvariable=var_email_id)
entry_faculty_email_id.grid(row=4, column=1, sticky="w", padx=10, pady=5)

label_faculty_last_ph_no=ttk.Label(left_frame, text="Phone no.", font=("Helvetica", 12))
label_faculty_last_ph_no.grid(row=5, column=0, sticky="w", padx=10, pady=5)
entry_faculty_last_ph_no = ttk.Entry(left_frame, width=36, textvariable=var_ph_no)
entry_faculty_last_ph_no.grid(row=5, column=1, sticky="w", padx=10, pady=5)

#------------------------Buttons Left frame-------------------------
frame_buttons = ttk.Frame(left_frame, borderwidth=0, relief="solid")
frame_buttons.grid(row=8, column=0, sticky="nsew",columnspan=2)
root.columnconfigure(0, weight=1) 

save_button = ttk.Button(frame_buttons, text="Save",width=10,bootstyle="success",command=save)
save_button.grid(row=0, column=0,pady=20, padx=10)

update_button = ttk.Button(frame_buttons, text="Update",width=10,command=update_data)
update_button.grid(row=0, column=1,pady=20, padx=10)

delete_button = ttk.Button(frame_buttons, text="Delete",width=10,bootstyle="danger",command=delete_data)
delete_button.grid(row=0, column=2,pady=20, padx=10)

reset_button = ttk.Button(frame_buttons, text="Reset",width=10,bootstyle="warning",command=reset_data)
reset_button.grid(row=0, column=3, pady=20,padx=10)

Back_button = ttk.Button(frame_buttons, text="Back",width=10,bootstyle="dark",command=back)
Back_button.grid(row=1, column=1,columnspan=2, sticky="s",pady=3,padx=3)

#================================Right Frame==================================
right_frame = ttk.Frame(root, borderwidth=2, relief="solid")
right_frame.grid(row=1, column=1, sticky="nsew")
root.columnconfigure(1, weight=9) 

# ----------------------Right Top Frame--------------------------------
label_name=ttk.Label(right_frame, text="Search System", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

form_frame = ttk.Frame(right_frame, padding=(10, 10, 10, 0))
form_frame.grid(row=1, column=0, pady=10, padx=(3, 3))

label_search_by=ttk.Label(form_frame, text="Search By", font=("Helvetica", 12))
label_search_by.grid(row=0, column=0, sticky="e", padx=10, pady=5)

search_by_combo=ttk.Combobox(form_frame,textvariable=var_search_by,font=("Helvetica",12),width=10,state="readonly")
search_by_combo["values"]=("Faculty ID","Faculty First Name","Faculty Last Name")
search_by_combo.grid(row=0,column=1,sticky="e", padx=10, pady=5)

label_search_info=ttk.Label(form_frame, text="Search By", font=("Helvetica", 12))
label_search_info.grid(row=0, column=2, sticky="e", padx=10, pady=5)
search_entry=Entry(form_frame,textvariable=var_entry_search,font=("Helvetica",12),width=14,relief=SOLID,bd=1)
search_entry.grid(row=0,column=3,padx=15,pady=10)

search_button = ttk.Button(form_frame, text="Search",bootstyle="primary",command=search_data)
search_button.grid(row=0, column=5,padx=10 ,pady=2) #, columnspan=len(form_entries_info) * 2

show_all_button = ttk.Button(form_frame, text="Show all",bootstyle="secondary",command=fetch_data)
show_all_button.grid(row=0, column=6, pady=2,sticky="e") #, columnspan=len(form_entries_info) * 2,

#------------------------------------Bottom Right Frame---------------------------------
table_frame = ttk.Frame(right_frame)
table_frame.grid(row=2, column=0, pady=20, padx=(3, 3))

columns = ["Faculty ID", "First Name", "Last Name", "Email", "Phone no."]

scrollhor=ttk.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="info")
scrollver=ttk.Scrollbar(table_frame,orient=VERTICAL,bootstyle="info")
faculty_table = ttk.Treeview(table_frame, columns=columns, show="headings",height=12,xscrollcommand=scrollhor.set,yscrollcommand=scrollver.set)
scrollhor.pack(side=BOTTOM,fill=X)
scrollver.pack(side=RIGHT,fill=Y)
scrollhor.config(command=faculty_table.xview)
scrollver.config(command=faculty_table.yview)

heading_frame = ttk.Frame(table_frame)

#making the table
faculty_table.heading("Faculty ID",text="Faculty ID")
faculty_table.heading("First Name",text="First Name")
faculty_table.heading("Last Name",text="Last Name")
faculty_table.heading("Email",text="Email")
faculty_table.heading("Phone no.",text="Phone no.")

faculty_table["show"]="headings"

faculty_table.column("Faculty ID",width=125)
faculty_table.column("First Name",width=125)
faculty_table.column("Last Name",width=125)
faculty_table.column("Email",width=125)
faculty_table.column("Phone no.",width=125)

faculty_table.pack(fill=BOTH,expand=10)
faculty_table.bind("<ButtonRelease>",get_cursor)
fetch_data()


root.mainloop()