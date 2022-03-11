## Tkinter GUI using frames for layouts
import tkinter as tk

main_window = tk.Tk()
main_window.wm_title('Tutorial')

" Frame is a widget used to contain other widgets for layout you can assign a widget to a frame by setting the widget's master attribute "

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(text = "I'm label in frame a!", master = frame_a)
label_a.pack()

label_b = tk.Label(text = "I'm in label in frame b!", master = frame_b)
label_b.pack()

# Note that frame_a is packed into the window before frame_b. The window that opens shows the label in frame_a above the label in frame_b

frame_a.pack()
frame_b.pack()

# Creating a loop to show off all relief efects that can applied to frames
relief_options = {
    'flat'      : tk.FLAT,
    'sunken'    : tk.SUNKEN,
    'raised'    : tk.RAISED,
    'groove'    : tk.GROOVE,
    'ridge'     : tk.RIDGE,
}
left_nav_button = tk.Button(text = ' < ', master = main_window, relief = tk.RAISED, padx = 15, background='white')
left_nav_button.pack(side = tk.LEFT)

for relief, relief_name in relief_options.items():
    frame_c = tk.Frame(master = main_window, relief = relief, borderwidth = 5)
    button_c = tk.Button(master = frame_c, text = relief_name)
    frame_c.pack(side = 'left')
    button_c.pack()
    print(relief + ' ' +  relief_name)


right_nav_button = tk.Button(text = '> ', master = main_window, relief = tk.RAISED, padx = 15, background= 'white')
right_nav_button.pack(side = tk.RIGHT)

main_window.mainloop()