# Goal of this file will be to create a basic GUI with TK
# This GUI will allow the users to select which methods to run from
# the imported file. This could be done with command line arguements 
# or accomplished far easier with method calls to the class directly

# After that we can create additional methods to copy, paste, and manipulate
# web pages to further expand upon selenium.

# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

import tkinter as tk

# creation of the frame
window = tk.Tk()
window.wm_title('TK Basic GUI') # sets the window title bar

#################################################################################
# adds a text widget
greetings_widget = tk.Label(
    text        = 'Python rocks! \n\n Enter your Username:',
    foreground  = 'white', # sets the text color
    background  = '#b00b69',
    width       = 80,
    height      = 4,
)
greetings_widget.pack()

################################    Entry       ########################################
entry = tk.Entry(justify = 'left', background = 'white', foreground = 'black')
entry.pack()
login = entry.get()

################################    Button      #########################################
button = tk.Button(text='Try Me!', background = '#aaaaaa')
button.pack() 
radio_widget = tk.Radiobutton()
#radio_widget.pack() 
check_box = tk.Checkbutton()
#check_box.pack()

################################# Text Field    ################################################
display_username = tk.Text(background = 'white', foreground = 'black')
display_username.insert('1.0', 'Hello, ')
display_username.insert('2.0', '\nWorld!')
display_username.insert(tk.END, '\n\n\n\n\n\n\n\nBottom Text')

display_username.get('1.0', tk.END) # will retrieve all the text in the box
display_username.pack()



# Create the handler that will execute on button click using bind method
def handler_button(self):
    second_window = tk.Tk()
    label = tk.Label(text="Thanks for trying out the button!")
    label2= tk.Label(text = 'Click here to return')
    button = tk.Button(text = 'Close Window')
    label.pack()
    label2.pack()
    button.pack()
    second_window.mainloop()
    button.bind('<ButtonRelease>', window.destroy())
button.bind('<ButtonRelease>', handler_button)



# mainloop runs the event loop which listens for input. blocks any code
# from executing until the window it's called on is closed.
window.mainloop()


