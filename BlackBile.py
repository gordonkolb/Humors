import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *

class BlackBile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # message
        self.my_text = Label(self, borderwidth = 0, bg='white', text="Black Bile", font=("Helvetica", 30), fg="black")
        self.my_text.place(relx=.5, rely=0, anchor=N)

        # button = tk.Button(self, text="Create Diagnosis!", bg='black', height = 2, borderwidth=0, 
        #                     command=lambda : controller.show_frame(FirstQuestion))
        # button.place(relx=.7, rely=.5, anchor=E)

        moody = IntVar()
        c = Checkbutton(self, text = "Moody", variable=moody)
        c.place(relx=.7, rely=.3, anchor=W)

        anxious = IntVar()
        c = Checkbutton(self, text = "Anxious", variable=anxious)
        c.place(relx=.7, rely=.5, anchor=W)

        rigid = IntVar()
        c = Checkbutton(self, text = "Rigid", variable=rigid)
        c.place(relx=.7, rely=.7, anchor=W)

        button = tk.Button(self, borderwidth = 0, bg='white', text="Next Question", font=("Helvetica", 30), fg="black", command=lambda : [controller.black_bile_function(moody, anxious, rigid)])
        button.place(relx=.4, rely=.2, anchor=E)

        