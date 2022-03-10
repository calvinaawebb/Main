import tkinter as tk
from tkinter.ttk import Label
from    tkinter import *
import json as js

# colors
light_grey = "#%02x%02x%02x" % (33, 33, 33)
light_purple = "#%02x%02x%02x" % (187, 134, 252)
darker_purple = "#%02x%02x%02x" % (55, 0, 188)
cyan = "#%02x%02x%02x" % (3, 218, 198)

# configuring main page window
home = Tk()
home.attributes("-fullscreen", True)
home.configure(bg=light_grey)

# getting screen's width and height in pixels
height = home.winfo_screenheight()
width = home.winfo_screenwidth()

# variables
entry_var = tk.StringVar()
f1 = Frame(home)
Home = Frame(home)


class setup:

    def __init__(self):
        title = tk.Label(home, text="Calvin Webb's", font=("Arial", 100), fg=light_purple, bg=light_grey)
        title.pack()
        title.update()
        title.place(x = width/2-(title.winfo_width()/2),y=0)
        title_sub = tk.Label(home, text="Library Encyclopedia", font=("Arial", 50), fg=light_purple, bg=light_grey)
        title_sub.pack()
        title_sub.update()
        title_sub.place(x = width/2-(title_sub.winfo_width()/2),y=title.winfo_height()+5)

    def enter(self, filename):
        file = open(filename, "r")
        data = js.load(file)
        return data

    def output(self, dict, file):
        with open(file, "w") as f:
            js.dump(dict, f)

    def raise_frame(self, frame):
        frame.tkraise()

set = setup()


entry1 = tk.Entry(home, width=116, textvariable=entry_var)
entry1.place(x=900,y=500,height=25)

class list_boxes:

    def __init__(self):
        self.list_box1 = tk.Listbox(home)
        self.list_box1.place(x=900, y=530, width=850, height=height-530)
        self.list_box1.update()
list = list_boxes()


class buttons:
    def __init__(self):
        self.button1 = tk.Button(home, text="Home", font=("Arial", 25), bd=5, bg=light_purple, fg=darker_purple)
        self.button1.place(x=10,y=10)
        self.button2 = tk.Button(home, command=self.add_entry(), text="Add Entry", font=("Arial", 25), bd=5, bg=light_purple, fg=darker_purple)
        self.button2.pack()
        self.button2.update()
        self.button2.place(x=width-(self.button2.winfo_width()+10),y=10)

    def add_entry(self):
        list.list_box1.insert(tk.END, entry_var.get())

button = buttons()

class drop_downs:

    def __init__(self):
        self.languages = ["Python", "Java", "C++", "HTML"]
        self.list1 = tk.StringVar(home)
        self.list1.set(self.languages[0])
        self.Category = ["Math", "GUI", "NN/AI", "Optimization"]
        self.list2 = tk.StringVar(home)
        self.list2.set(self.Category[0])

    def drop_down1(self):
        self.drop_down1 = tk.OptionMenu(home, self.list1, *self.languages)
        self.drop_down1["menu"].config(bg=light_purple)
        self.drop_down1["highlightthickness"]=0
        self.drop_down1.config(bg=light_purple)
        self.drop_down1.pack()
        self.drop_down1.update()
        self.drop_down1.place(x=width-(button.button2.winfo_width()+710), y=500)

    def drop_down2(self):
        self.drop_down2 = tk.OptionMenu(home, self.list2, *self.Category)
        self.drop_down2["menu"].config(bg=light_purple)
        self.drop_down2["highlightthickness"]=0
        self.drop_down2.config(bg=light_purple)
        self.drop_down2.pack()
        self.drop_down2.update()
        self.drop_down2.place(x=width-(button.button2.winfo_width()+780), y=500)




print("got past")
selection = list.list_box1.curselection()
drop = drop_downs()
drop.drop_down1()
drop.drop_down2()
f1.tkraise()
tk.mainloop()
