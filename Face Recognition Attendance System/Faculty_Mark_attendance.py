import tkinter as tk
from tkinter import *
from ttkbootstrap import Style, ttk

#==================================ROOT WINDOW=================================

root = tk.Tk()
root.title("Mark Attendance")
style = Style(theme="yeti")

#===================================LEFT FRAME=================================

frame1 = ttk.Frame(root, borderwidth=0, relief="solid", )
frame1.grid(row=1, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)

class_entries_info = {
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
                                                   "BE Electrical A", "BE Electrical B", "BE Electrical C", ]},
    "Time Slot": {"type": "dropdown", "options": ["9.00 - 10.00", "10.00 - 11.00", "11.15 - 12.15",
                                                  "12.15 - 13.15", "13.45 - 14.45", "13.45 - 15.45",
                                                  "14.45 - 15.45", "16.00 - 18.00", ]},
    "Subject name": {"type": "dropdown", "options": ["subj1", "subj2"]},
}

entries = []
label_name = ttk.Label(frame1, text="Class Details", font=("Helvetica", 14, "bold"))
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

for i, (label_text, info) in enumerate(class_entries_info.items()):
    label = ttk.Label(frame1, text=label_text, font=("Helvetica", 12))
    label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)

    if info["type"] == "dropdown":
        entry = ttk.Combobox(frame1, values=info["options"], width=34)
    else:
        entry = ttk.Entry(frame1, width=36)

    entry.grid(row=i + 1, column=1, sticky="e", padx=10, pady=5)
    entries.append(entry)

unknown_label_name = ttk.Label(frame1, text="Class Details", font=("Helvetica", 14, "bold"),foreground="white")
unknown_label_name.grid(row=4, column=0, sticky="w", padx=10, pady=5)

Back_button = ttk.Button(frame1, text="Back",width=10,bootstyle="dark")
Back_button.grid(row=5, column=0,columnspan=2,sticky="n",pady=3,padx=3)

#=========================RIGHT FRAME================================

frame2 = ttk.Frame(root, borderwidth=0, relief="solid")
frame2.grid(row=1, column=1, sticky="nsew")
root.columnconfigure(1, weight=9)

frame6 = ttk.Frame(frame2, borderwidth=0, relief="solid")
frame6.grid(row=1, column=0, sticky="nsew")
root.columnconfigure(1, weight=9)

label_name=ttk.Label(frame2, text="Mark Attendance", font=("Helvetica", 14,"bold"))
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=3)

def on_button_click():
    print("Button clicked!")

def on_enter(event):
    canvas.config(cursor="hand2")

def on_leave(event):
    canvas.config(cursor="")

def create_round_button(canvas, x, y, radius, text,outline_width=2):
    button = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue", outline="black", width=outline_width)
    text = canvas.create_text(x, y, text=text, font=("Helvetica", 12), anchor="center")
    return button, text

# Create a Canvas widget
canvas = tk.Canvas(frame6, width=200, height=200, bg="white")
canvas.pack()

# Create a round button on the canvas
button, text = create_round_button(canvas, 100, 100, 90, "    Click here to\nMark Attendance!!", outline_width=4)

# Bind events to change cursor
canvas.tag_bind(button, "<Button-1>", lambda event: on_button_click())
canvas.tag_bind(button, "<Enter>", on_enter)
canvas.tag_bind(button, "<Leave>", on_leave)

title_label = ttk.Label(root, text="MARK STUDENT ATTENDANCE", font=("Helvetica", 20, "bold"), style="TLabel", padding=20)
title_label.grid(row=0, column=0, columnspan=2)

root.mainloop()