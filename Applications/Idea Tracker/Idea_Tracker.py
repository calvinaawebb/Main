import tkinter as tk
from tkinter.ttk import Label
import json as js

# colors
light_grey = "#%02x%02x%02x" % (33, 33, 33)
light_purple = "#%02x%02x%02x" % (187, 134, 252)
darker_purple = "#%02x%02x%02x" % (55, 0, 188)
cyan = "#%02x%02x%02x" % (3, 218, 198)

# configuring main page window
home = tk.Tk()
home.attributes("-fullscreen", True)
home.configure(bg=light_grey)

# variables
name_var = tk.StringVar(home, value="Enter Submission...")
data = {}
counter = 0

# functions
def submit_entry():
    name=name_var.get()
    if len(name) != 0:
        list_box1.insert(tk.END, name)
        counter += 1
        data["Name" + str(counter)] = name
        print(data)
                

    name_var.set("")

def enter(filename):
    file = open(filename, "r")
    data = js.load(file)
    return data

def output(dict, file):
    with open(file, "w") as f:
        js.dump(dict, f)

# getting screen's width and height in pixels
height = home.winfo_screenheight()
width = home.winfo_screenwidth()


# title
title = tk.Label(home, text="Calvin Webb's", font=("Arial", 100), fg=light_purple, bg=light_grey)
title.pack()
title.update()
title.place(x = width/2-(title.winfo_width()/2),y=0)
title_sub = tk.Label(home, text="Idea Tracker", font=("Arial", 50), fg=light_purple, bg=light_grey)
title_sub.pack()
title_sub.update()
title_sub.place(x = width/2-(title_sub.winfo_width()/2),y=title.winfo_height()+5)

# interactables
button1 = tk.Button(home, text="Submit", command=submit_entry ,font=("Arial", 25), bd=5, bg=light_purple, fg=darker_purple)
button1.place(x=10,y=10)
button2 = tk.Button(home, text="Delete", command=submit_entry ,font=("Arial", 25), bd=5, bg=light_purple, fg=darker_purple)
button2.place(x=home.winfo_screenwidth() - 140,y=10)
entry1 = tk.Entry(home, textvariable = name_var)
entry1.place(x = 400, y = 300, width = 750, height = 25)
list_box1 = tk.Listbox(home)    
list_box1.place(x=400, y=325, width=750, height=height-325)
tk.mainloop()
                                                                        
