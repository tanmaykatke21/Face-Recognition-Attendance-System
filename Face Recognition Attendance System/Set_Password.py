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
    "New password": {"type": "entry"},
    "Confirm Password": {"type": "entry"},
}

entries = []
label_name=ttk.Label(frame1, text="Set Password", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, columnspan=2,sticky="n", padx=10, pady=5)

for i, (label_text, info) in enumerate(entries_info.items()):
    label = ttk.Label(frame1, text=label_text, font=("Helvetica", 12))
    label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)
    entry = ttk.Entry(frame1, width=36)

    entry.grid(row=i + 1, column=1, sticky="e", padx=10, pady=5)
    entries.append(entry)

Back_button = ttk.Button(frame1, text="Reset Password",width=10,bootstyle="success")
Back_button.grid(row=3, column=0,columnspan=2,sticky="nsew",pady=3,padx=3)

root.mainloop()