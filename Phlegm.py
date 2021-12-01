import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *

class Phlegm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # message
        self.my_text = Label(self, borderwidth = 0, bg='white', text="Phlegm", font=("Helvetica", 30), fg="black")
        self.my_text.place(relx=.5, rely=0, anchor=N)

        # button = tk.Button(self, text="Create Diagnosis!", bg='black', height = 2, borderwidth=0, 
        #                     command=lambda : controller.show_frame(FirstQuestion))
        # button.place(relx=.7, rely=.5, anchor=E)

        i2 = IntVar()
        c = Checkbutton(self, text = "Python2", variable=i2)
        c.place(relx=.7, rely=.5, anchor=E)

        button = tk.Button(self, borderwidth = 0, bg='white', text="Next Question", font=("Helvetica", 30), fg="black", command=lambda : [controller.click_me2(i2)])
        button.place(relx=.4, rely=.2, anchor=E)

        