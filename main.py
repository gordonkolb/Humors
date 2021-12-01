import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
from homepage import Homepage
from homepage import *
from lastpage import Lastpage
from lastpage import *
from BlackBile import BlackBile
from BlackBile import *
from Phlegm import Phlegm
from Phlegm import *
from humors import Humors

# Instanciate databse object
humors = Humors()

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Homepage, Lastpage, BlackBile, Phlegm):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Homepage, "fake")

    # to display the current frame passed as
    # parameter

    def black_bile_function(self, moody, anxious, rigid):
        print(moody.get())
        print(anxious.get())
        print(rigid.get())
        if (moody.get()):
            humors.add_symptom("Moody")
        if (anxious.get()):
            humors.add_symptom("Anxious")
        if (rigid.get()):
            humors.add_symptom("Rigid")

        humors.print_symptoms()
        
        frame = self.frames[Phlegm]
        frame.tkraise()

    def click_me2(self, i):
        print(i.get())
        frame = self.frames[Lastpage]
        frame.tkraise()

    def show_homepage(self):
        frame = self.frames[Homepage]
        frame.tkraise()

    def show_FirstQuestion(self):
        frame = self.frames[BlackBile]
        frame.tkraise()

    def show_frame(self, cont, action=""):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    # Driver Code
    app = tkinterApp()
    app.title("Galens Four Humors System")
    app.geometry("1000x500")
    app.minsize(800, 400)
    app.maxsize(800, 400)
    app.mainloop()  