# Resource File
# Basic GUI Implementation
#############################################################################################

# Importing and assigning an alias for easy use

import outputGen
from tkinter import *
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        # Creating the foreground
        appWindow = tk.Label(self, height = 40, width = 160, bg = 'black')
        appWindow.grid(columnspan = 3, rowspan = 4)
        
        #Need label/button to chose which list to display
        Title_Information = tk.Label(self, text = 'Database Output', bg = 'grey', fg = 'white', font = 'none 24 bold').grid(row = 0, column = 1)
        
        # With each button picked should display output from console to lower label
        p_Button = tk.Button(self, text = 'Person', width = 9, font = 'none 18 bold').grid(row = 1, column = 0)
        e_Button = tk.Button(self, text = 'Employee', width = 9, font = 'none 18 bold').grid(row = 1, column = 1)
        c_Button = tk.Button(self, text = 'Customer', width = 9, font = 'none 18 bold').grid(row = 1, column = 2)
        
        # Label for displaying the information from outputGen? Scroll bar?
        output = Text(self, width = 140, background = 'grey', fg= 'yellow')
        output.grid(row = 2, rowspan = 4, columnspan = 3)
        
        #list_one = "test output"
        #p_Button(command = output.insert(END, list_one))
        
        # Need way to clear information.
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()