import tkinter
from tkinter import *
#from idlelib.autocomplete_w import DOUBLECLICK_SEQUENCE

# Key down function
def click():
    enteredText=TextEntry.get() # collect the text from the entry box
    output.delete(0.0, END) # Cleaning any pre-existing output from the box. From first line and character to end of box
    #now will do try to navigate the list
    try:
        definition = my_Dictionary[enteredText]
    except:
        definition = 'Sorry there is no word like that stored in this dictionary. Please try again'
    # Insert the definition
    output.insert(END, definition)

# Using Labels
window = Tk()
# Naming the window
window.title("Python GUI")
# Setting the background of the window
window.configure(background="black")

# Loading an image into the file
photo1 = PhotoImage(file="window (2).png")
# Changing values for the image
Label(window, bg='black', image=photo1).grid(row=0,column=0,sticky=W)
# Creating a dialogue box
Label(window,text="Enter the word you would like a definition for: ", bg='black', fg='white', font = 'none 12 bold').grid(row=1,column= 0, sticky = W)

# Create a text entry box
TextEntry = Entry(window, width = 24, bg = 'white')
TextEntry.grid(row = 2 , column = 0, sticky = W)

# Create a submit button
Button(window, width = 6, text = 'SUBMIT', command = click).grid(row = 3, column = 0, sticky = W)

# Create a definition label
Label(window, text = '\nDefintion: ', bg = 'black', fg = 'white', font = 'none 12 bold').grid(row = 4, column = 0, stick = W)

# Create an output box
output = Text(window, width = 80, height = 6, wrap = WORD, background = 'white' )
output.grid(row = 5, column = 0, columnspan = 2, sticky = W )

# Call the dictionary
my_Dictionary = {'algorithm' : 'Step by step instructions to complete a task',
                 'bug'       : 'A piece of code that causes a program to fail',
                 'dog'       : 'Man\'s best friend'}

# Create a label for an exit button
Label(window,text="Click to exit: ", bg='black', fg='white', font = 'none 12 bold').grid(row=6,column= 0, sticky = W)
Button(window, width = 4, text = 'EXIT', command = quit).grid(row = 7, column = 0, sticky = W)

# Runs the main GUI program
window.mainloop()
