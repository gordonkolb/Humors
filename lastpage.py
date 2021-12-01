import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *

class Lastpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # message
        self.my_text = Label(self, borderwidth = 0, bg='white', text="Welcome to Gordie's Handicap System!", font=("Helvetica", 30), fg="black")
        self.my_text.place(relx=.5, rely=0, anchor=N)
        