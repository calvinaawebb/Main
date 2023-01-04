import tkinter as tk
import os
from tkinter import *

# colors
light_grey = "#%02x%02x%02x" % (33, 33, 33)
light_purple = "#%02x%02x%02x" % (187, 134, 252)
darker_purple = "#%02x%02x%02x" % (55, 0, 188)
cyan = "#%02x%02x%02x" % (3, 218, 198)

# configuring main page window
home = Tk()
home.title("Chemiae: An Interactive and Intuitive Stoichiometry Calculator")
#home.attributes("-fullscreen", True)
home.configure(bg=light_grey)

# screen size set
home.geometry("%dx%d" % (home.winfo_screenwidth(), home.winfo_screenheight()))
home.update()

# getting screen's width and height in pixels
height = home.winfo_screenheight()
width = home.winfo_screenwidth()

class main():

    def __init__(self):
        title = tk.Label(home, text="Chemiae: The Stoichiometry Calculator", font=("Arial", 75), fg=light_purple, bg=light_grey)
        title.pack()
        title.update()
        title.place(x=width / 2 - (title.winfo_width() / 2), y=0)
        title_sub = tk.Label(home, text="By: Calvin Webb, Olivia, Daisy, and Red", font=("Arial", 25), fg=light_purple, bg=light_grey)
        title_sub.pack()
        title_sub.update()
        title_sub.place(x=width / 2 - (title_sub.winfo_width() / 2), y=title.winfo_height() + 5)

main()
tk.mainloop()



