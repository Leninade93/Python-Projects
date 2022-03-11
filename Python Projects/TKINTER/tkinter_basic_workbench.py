import tkinter as tk

# Create basic welcome message, and login page

class Program_GUI:
    pass

class Login_Page():
    def __init__(self):
        # Variables
        self.authenciation_check = False
        
        # Frame
        self.welcome_window = tk.Tk()
        self.welcome_window.wm_title("Login Form")
        self.title_frame = tk.Frame(master=self.welcome_window, relief = tk.SUNKEN, width = 35, height = 10, borderwidth = 5)
        self.title_label = tk.Label(
            master      = self.title_frame,
            text        = 'Welcome, please enter your login credentials', 
            foreground  = 'white', 
            background  = 'black',
            font        = ('Arial', 14, 'bold'),
            padx       = 30
        )
        self.title_label.pack(), self.title_frame.pack()

        self.uid_frame = tk.Frame(
            master = self.welcome_window,
        )
        self.uid_label = tk.Label(
            master      = self.uid_frame,
            font        = ('Arial', 12, 'bold'),
            text        = 'Username: ',
            justify     = tk.LEFT
        )
        self.uid_entry = tk.Entry(
            master  = self.uid_frame,
            font    = ('Arial', 12, 'bold')
        )
        self.pass_frame = tk.Frame(
            master = self.welcome_window
        )
        self.pass_label = tk.Label(
            master  = self.pass_frame,
            font    = ('Arial', 12, 'bold'),
            text    = 'Password: ',
            justify = tk.LEFT
        )
        self.pass_entry = tk.Entry(
            master  = self.pass_frame,
            font    = ('Arial', 12, 'bold'),
            show    = '*'
        )
        self.submit_frame = tk.Frame(
            relief = tk.FLAT,
            border = 5
        )
        self.submit_button = tk.Button(
            master  = self.submit_frame,
            padx    = 5,
            pady    = 2,
            text    = 'Submit',
            font    =('Arial', 12, 'bold')
        )
        # Layout will change based upon pack. Maybe grid is better because of this
        self.uid_frame.pack(), self.uid_label.pack(side = tk.LEFT), self.uid_entry.pack(side = tk.RIGHT)
        self.pass_frame.pack(), self.pass_label.pack(side = tk.LEFT), self.pass_entry.pack(side = tk.RIGHT)
        self.submit_frame.pack(), self.submit_button.pack()
        #Alternative layout. Messing with different options to send as paramaters
        'uid_frame.pack(side=tk.TOP), pass_frame.pack( after=uid_frame), submit_frame.pack(side = tk.RIGHT)'
        'uid_label.pack(side = tk.LEFT), uid_entry.pack(side = tk.RIGHT)'
        'pass_label.pack(side = tk.LEFT), pass_entry.pack(side = tk.RIGHT)'
        'submit_button.pack()'
    
    def handle_keypress(self, event):
        # Print the character that was pressed
        print(event.char)

    def login_get(self, event):
        self.username = self.uid_entry.get()
        self.password = self.pass_entry.get()
        #print('Debug message: ' + str(self.uid_entry.select_present()))
        self.authenciation_check = False

        if self.username == 'admin' and self.password == 'password':
            print("Authentication Success!")
            self.title_label.destroy()
            self.title_label = tk.Label(
                master      = self.title_frame,
                text        = 'Authentication Successful!', 
                foreground  = 'white', 
                background  = 'black',
                font        = ('Arial', 14, 'bold'),
                padx       = 30
            )
            self.title_label.pack()
            self.authenciation_check = True
            self.welcome_window.destroy()
        else:
            print("Invalid Username or Password. Please try again")
            self.uid_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)
            self.title_label.destroy()
            self.title_label = tk.Label(
                master      = self.title_frame,
                text        = 'Invalid Username or Password, Please try again', 
                foreground  = 'white', 
                background  = 'black',
                font        = ('Arial', 14, 'bold'),
                padx       = 30
            )
            self.title_label.pack()

class File_Manager():
    # Idea will be on the left user can select "buttons" that will load
    # images into a widget on the right. Not sure which widget will work
    # best. Maybe a label.

    def __init__(self):
        # Widgets
        self.Image_Window   = tk.Tk()
        self.title_frame    = tk.Frame()
        self.title_label    = tk.Label(
            text='File Browser',
            master = self.title_frame,
            foreground  = 'white', 
            background  = 'black',
            font        = ('Arial', 14, 'bold'),
            padx       = 30
        )
        self.file_frame     = tk.Frame()
        self.file_buttons   = tk.Button(
            master = self.file_frame,
            padx    = 5,
            pady    = 2,
            text    = 'test',
            font    = ('Arial', 12, 'bold')
        )
        self.display_frame  = tk.Frame()
        self.display_label  = tk.Label()

        # Pack Layout
        self.title_frame.pack() 
        self.title_label.pack(side=tk.TOP)
        self.file_frame.pack()
        self.file_buttons.pack(side = tk.LEFT)
        self.display_frame.pack()
        self.display_label.pack(side = tk.RIGHT)
        

Welcome_GUI = Login_Page()
Welcome_GUI.submit_button.bind('<ButtonRelease>', Welcome_GUI.login_get)
Welcome_GUI.submit_button.bind('<Enter>', Welcome_GUI.login_get)
Welcome_GUI.welcome_window.mainloop()

if Welcome_GUI.authenciation_check == True:
    File_GUI = File_Manager()
    File_GUI.Image_Window.mainloop()



# Mess with classes, inheritance, and overloading to create gui framwork
# toplevel() and hide(), show()


