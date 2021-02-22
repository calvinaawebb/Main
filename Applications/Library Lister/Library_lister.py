import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
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

# getting screen's width and height in pixels
height = home.winfo_screenheight()
width = home.winfo_screenwidth()

# string variables
entry_var = tk.StringVar()

# functions
def enter(filename):
    file = open(filename, "r")
    data = js.load(file)
    return data

def output(dict, file):
    with open(file, "w") as f:
        js.dump(dict, f)

def add_entry():
    list_box1.insert(tk.END, entry_var.get())



# title
title = tk.Label(home, text="Calvin Webb's", font=("Arial", 100), fg=light_purple, bg=light_grey)
title.pack()
title.update()
title.place(x = width/2-(title.winfo_width()/2),y=0)
title_sub = tk.Label(home, text="Library Encyclopedia", font=("Arial", 50), fg=light_purple, bg=light_grey)
title_sub.pack()
title_sub.update()
title_sub.place(x = width/2-(title_sub.winfo_width()/2),y=title.winfo_height()+5)

# interactables
button1 = tk.Button(home, text="Home", font=("Arial", 25), bd=5, bg=light_purple, fg=darker_purple)
button1.place(x=10,y=10)
button2 = tk.Button(home, command=add_entry, text="Add Entry", font=("Arial", 25), bd=5, bg=light_purple, fg=darker_purple)
button2.pack()
button2.update()
button2.place(x=width-(button2.winfo_width()+10),y=10)
languages = ["Python", "Java", "C++", "HTML"]
list1 = tk.StringVar(home)
list1.set(languages[0])
drop_down1 = tk.OptionMenu(home, list1, *languages)
drop_down1["menu"].config(bg=light_purple)
drop_down1["highlightthickness"]=0
drop_down1.config(bg=light_purple)
drop_down1.pack()
drop_down1.update()
drop_down1.place(x=width-(button2.winfo_width()+710), y=500)
Category = ["Math", "GUI", "NN/AI", "Optimization"]
list2 = tk.StringVar(home)
list2.set(Category[0])
drop_down2 = tk.OptionMenu(home, list2, *Category)
drop_down2["menu"].config(bg=light_purple)
drop_down2["highlightthickness"]=0
drop_down2.config(bg=light_purple)
drop_down2.pack()
drop_down2.update()
drop_down2.place(x=width-(button2.winfo_width()+780), y=500)
entry1 = tk.Entry(home, width=116, textvariable=entry_var)
entry1.place(x=900,y=500,height=25)
list_box1 = tk.Listbox(home)
list_box1.place(x=900, y=530, width=850, height=height-530)
tk.mainloop()
