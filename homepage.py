import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
from BlackBile import BlackBile

class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # message
        self.my_text = Label(self, borderwidth = 0, bg='white', text="Welcome to Galen's Four Humor System!", font=("Helvetica", 30), fg="black")
        self.my_text.place(relx=.5, rely=0, anchor=N)

        button = tk.Button(self, text="Create Diagnosis!", bg='black', height = 2, borderwidth=0, 
                            command=lambda : controller.show_frame(BlackBile))
        button.place(relx=.7, rely=.5, anchor=E)
        
        # Create widgets/grid
        '''
        #background 
        self.bg = PhotoImage(file='tester.png')
        self.my_label = Label(self, image=self.bg)
        self.my_label.place(relwidth=1, relheight=1)
        
        
         
        # Buttons
        button = tk.Button(self, text="Enter Score", bg='black', height = 2, borderwidth=0, 
                            command=lambda : controller.show_frame(EnterScore))
        button.place(relx=.7, rely=.5, anchor=E)

        button1 = tk.Button(self, text="View Previous Scores", height = 2, borderwidth = 0, 
                            command=lambda : controller.show_frame(ViewScores))
        button1.place(relx=.3, rely=.5, anchor=W)

        #display handicap
        self.handicap = db.calculate_handicap()
        self.my_handicap = Label(self, borderwidth = 0, bg='blue', text="Current Handicap: "+str(self.handicap), font=("Helvetica", 20), fg="white")
        self.my_handicap.place(relx=.0, rely=.93, anchor=NW)
        '''