import tkinter as tk

window = tk.Tk()
lower_frame = tk.Frame(master = window)
upper_frame = tk.Frame(master = window)
value_lbl = tk.Label(text = '0', master = upper_frame, padx = 20, pady = 2)

def truncate(*arg):
    # get the float as string
    temp = str(arg[0])

    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x+arg[1]+1])
            except:
                return float(temp[temp])
    return float(temp)

    

def increase():
    increment_value = float(value_lbl['text']) + 0.1
    value_lbl['text'] = truncate(f'{increment_value}', 2)
    

def decrease():
    decrement_value = float(value_lbl['text']) - 0.1
    value_lbl['text'] = truncate(f'{decrement_value}', 2)

dec_btn = tk.Button(master = lower_frame, text = ' - ', command = decrease, padx = 5, pady = 2)
inc_btn = tk.Button(master = lower_frame, text = ' + ', command = increase, padx = 5, pady = 2)

upper_frame.pack()
lower_frame.pack()
dec_btn.pack(side=tk.LEFT),value_lbl.pack(side = tk.TOP), inc_btn.pack(side=tk.RIGHT)

window.mainloop()

