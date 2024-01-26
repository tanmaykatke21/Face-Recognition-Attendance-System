import tkinter as tk
from tkinter import *
from ttkbootstrap import Style, ttk, DateEntry

#==================================ROOT WINDOW=================================

root = tk.Tk()
root.title("Forgot Password")
style = Style(theme="yeti")

frame1 = ttk.Frame(root, borderwidth=2, relief="solid",)
frame1.grid(row=1, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)

entries_info = {
    "Username": {"type": "entry"},
    "Security Question": {"type": "dropdown", "options": ["My birthplace","My favourite fast food","My favourite colour","My first school name",]},
    "Security Answer": {"type": "entry"},
}

entries = []
label_name=ttk.Label(frame1, text="Forgot Password", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, columnspan=2,sticky="n", padx=10, pady=5)

for i, (label_text, info) in enumerate(entries_info.items()):
    label = ttk.Label(frame1, text=label_text, font=("Helvetica", 12))
    label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)

    if info["type"] == "dropdown":
        entry = ttk.Combobox(frame1, values=info["options"], width=34)
    else:
        entry = ttk.Entry(frame1, width=36)

    entry.grid(row=i + 1, column=1, sticky="e", padx=10, pady=5)
    entries.append(entry)

class_name_var = StringVar()
class_name_var.set(entries_info["Security Question"]["options"][0])  # Set default value
class_name_dropdown = ttk.Combobox(frame1, values=entries_info["Security Question"]["options"], width=34, textvariable=class_name_var)
class_name_dropdown.grid(row=2, column=1, sticky="e", padx=10, pady=5)
entries.append(class_name_dropdown)

Back_button = ttk.Button(frame1, text="Proceed",width=10,bootstyle="success")
Back_button.grid(row=4, column=0,columnspan=2,sticky="nsew",pady=3,padx=3)

root.mainloop()