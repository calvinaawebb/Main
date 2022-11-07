import os
from tkinter import *
import pathlib

'''
IDEAS FOR THE PROJECT:
Make a labeling system that color codes list entries
Make actual folder system instead of just a list(hard)
'''


# save directory
saveDir = "auctor_data"
savePath = os.path.join(pathlib.Path(__file__).parent.resolve(), saveDir)

# list of files for file manager
global files

# checking if the save directory exists and making it if it doesn't
print(os.path.isdir(savePath))
if os.path.isdir(savePath) is False:
    print(savePath)
    os.mkdir()

# setting files to the list of files in the save directory
files = os.listdir(os.path.join(pathlib.Path(__file__).parent.resolve(), saveDir))

# base setting
root = Tk()
root.title("A.U.C.T.O: Anomalous Utilization Console for Technical Organization")

# screen size set
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# colors
darker_grey = "#%02x%02x%02x" % (85, 85, 90)
light_purple = "#%02x%02x%02x" % (187, 134, 252)
darker_purple = "#%02x%02x%02x" % (55, 0, 188)
cyan = "#%02x%02x%02x" % (3, 218, 198)


class main():

    def __init__(self):
        # Menu:
        # Stylizing
        global can
        can = Canvas(root)
        can.create_line(0, 30, width, 30, fill="grey")
        can.configure(bg=darker_grey, highlightthickness=0)
        can.place(x=0, y=0, width=width, height=height)

        # New File
        nf = Button(root, text="New File", bg=darker_grey, fg="white", activebackground=light_purple, activeforeground="white", bd=0, font=("Arial", 11))
        nf.place(x=0, y=0)
        nf.update()

        # Edit
        ed = Button(root, text="Edit", bg=darker_grey, fg="white", activebackground=light_purple, activeforeground="white", bd=0, font=("Arial", 11))
        ed.place(x=nf.winfo_width(), y=0)
        ed.update()

        # Windows
        win = Button(root, text="Windows", bg=darker_grey, fg="white", activebackground=light_purple, activeforeground="white", command=fileManager.clicked, bd=0, font=("Arial", 11))
        win.place(x=(nf.winfo_width() + ed.winfo_width()), y=0)
        win.update()

        # Settings
        set = Button(root, text="Settings", bg=darker_grey, fg="white", activebackground=light_purple, activeforeground="white", bd=0, font=("Arial", 11))
        set.place(x=(nf.winfo_width() + ed.winfo_width() + win.winfo_width()), y=0)
        set.update()

class fileManager(Frame):

    def __init__(self):
        super().__init__()
        #mana = self.Listbox(files)

    def clicked():
        can.create_line(500, 30, 500, height, fill="grey")

main()
fs = fileManager()

mainMenu = Frame(root)
mainMenu.place(x=0,y=0)
mainMenu.configure(bd=10)
mainMenu.pack()

# mainMenu.mainloop()
root.mainloop()