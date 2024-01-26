import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

alogin_win = tk.Tk()

alogin_win.geometry('400x500+620+100')
alogin_win.title('Attendance System Admin Login')

h1 = ('Arial','25')
h2 = ('Arial','20')
f1 = ('Arial','16')
f2 = ('Arial','14')

l1 = ttk.Label(alogin_win, text='Attendance System', font=h1)
l1.pack(pady=20)
b1 = tk.Button(alogin_win, text='Student Profile', font=f1, width=20)
b1.pack(pady=5)
b2 = tk.Button(alogin_win, text='Faculty Profile', font=f1, width=20)
b2.pack(pady=5)
b3 = tk.Button(alogin_win, text='Assign Subject', font=f1, width=20)
b3.pack(pady=5)
b4 = tk.Button(alogin_win, text='Train Data', font=f1, width=20)
b4.pack(pady=5)
b5 = tk.Button(alogin_win, text='Register Admin', font=f1, width=20)
b5.pack(pady=5)
b6 = tk.Button(alogin_win, text='Developer', font=f1, width=20)
b6.pack(pady=5)
b7 = tk.Button(alogin_win, text='Photos', font=f1, width=20)
b7.pack(pady=5)

button_style = {
    "font": ("Arial", 16),  # Change font and size here
    "bg": "#Ff0000",  # Background color
    "fg": "black",  # Foreground (text) color
    "pady": 5,  # Vertical padding
    "text": "Logout",  # Button text
}

b8 = tk.Button(alogin_win, width=20, **button_style)
b8.pack(pady=5)

alogin_win.mainloop()