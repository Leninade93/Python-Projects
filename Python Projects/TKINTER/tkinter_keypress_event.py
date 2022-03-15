# Note: An event is any action that occurs during the event loop that might
# trigger some behavior in the application, such as when a key or mouse button is pressed.
# When an event occurs, an event object is emitted, which means that an
# instance of a class representing the event is instantiated. You don’t need to worry about
# creating these classes yourself. Tkinter will create instances of event classes for you automatically.
# https://realpython.com/python-gui-tkinter/

def event_handling_concept():
    events_list = []

    while True:
        # If events_list is empty, then no events have occurred and you
        # can skip to the next iteration of the loop
        if events_list == []:
            continue

        # If execution reaches this point, then there is at least one
        # event object in events_list
        event = events_list[0]
        
        if event.type == 'keypress':
            handle_keypress(event)

    # this loop would be running waiting for events as your window is open

from cgitb import text
import tkinter as tk

window = tk.Tk()
text_display = tk.Label(text='debug', font=('Arial', 12, 'bold'))
text_display.pack()

# Create an event handler
def handle_keypress(event):
    # Print the character that was pressed
    print(event.char + ' ' + str(event.keycode))
    text_display['text'] = event.char + ' ' + str(event.keycode)

# Bind the keypress to the event handler
# .bind() always takes atleast two arguments
# any tkinter event in string form <event_name>
# an event_handler, the name of the funciton to be called
window.bind('<Key>', handle_keypress)

window.mainloop()

