import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

login_win = tk.Tk()
login_win.geometry('590x430+490+150')
login_win.title('Login')

h1 = ('Arial','25')
h2 = ('Arial','20')
f1 = ('Arial','16')
f2 = ('Arial','14')

fr1 = tk.Frame(login_win, highlightbackground="black")
fr1.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")
fr2 = tk.Frame(login_win, highlightbackground="black", highlightthickness=1)
fr2.grid(row=1, column=0, padx=10, pady=5)

# Frame 1 contents
l1 = tk.Label(fr1, text='Face Recognition Attendance System', font=h1)
l1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Frame 2 contents
l2 = tk.Label(fr2, text='Login', font=h2)
l2.grid(row=0, column=0, padx=30, pady=10, columnspan='2', sticky="nsew")
l3 = tk.Label(fr2, text='Username: ', font=f1)
l3.grid(row=1, column=0, padx=50, pady=10, columnspan='1', sticky="nse")
e3 = ttk.Entry(fr2, font=f2)
e3.grid(row=1, column=1, padx=10, pady=10, columnspan='1', sticky="nsw")
l4 = tk.Label(fr2, text='Password: ', font=f1)
l4.grid(row=2, column=0, padx=50, pady=10, columnspan='1', sticky="nse")
e4 = ttk.Entry(fr2, font=f2, show='*')
e4.grid(row=2, column=1, padx=10, pady=10, columnspan='1', sticky="nsw")
b1 = tk.Button(fr2, text='Login', font = f1, background='light blue')
b1.grid(row=3, column=0, padx=50, pady=10, columnspan='2')


def on_enter(event):
    l5.config(fg="blue")  # Change label background and foreground color on hover

def on_leave(event):
    l5.config(fg="black")  # Restore original colors when mouse leaves


l5 = tk.Label(fr2, text='Forgot Password?', font=f1)
l5.grid(row=4, column=0, padx=50, pady=10, columnspan='2', sticky="nsew")
l5.bind("<Enter>", on_enter)  # Binds the hover event to the label
l5.bind("<Leave>", on_leave)  # Binds the mouse leave event to the label
login_win.mainloop()