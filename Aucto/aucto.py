import os
from tkinter import *
from tkinter import ttk
import pathlib

'''
IDEAS FOR THE PROJECT:
Make a labeling system that color codes list entries
Make actual folder system instead of just a list(hard)
'''


# save directory
saveDir = "auctor_data"
savePath = pathlib.Path(__file__).parent / pathlib.Path(saveDir)

# list of files for file manager
global files

# checking if the save directory exists and making it if it doesn't
print(os.path.isdir(savePath))
if os.path.isdir(savePath) is False:
    print(savePath)
    os.mkdir(savePath)

# setting files to the list of files in the save directory
files = os.listdir(os.path.join(pathlib.Path(__file__).parent.resolve(), saveDir))

# base setting
root = Tk()
root.title("A.U.C.T.O: Anomalous Utilization Console for Technical Organization")
root.option_add("*tearOff", False)

# screen size set
width = root.winfo_width()
height = root.winfo_height()
root.geometry("%dx%d" % (width, height))

def define_color(color):
    return "#%02x%02x%02x" % color

# colors
darker_grey = define_color((85, 85, 90))
light_purple = define_color((187, 134, 252))
darker_purple = define_color((55, 0, 188))
cyan = define_color((3, 218, 198))


class main():

    def __init__(self):
        # Menu:
        menubar = Menu()
        root.config(menu=menubar)
        menubar.config(bg=darker_grey, fg="white", activebackground=light_purple, activeforeground="white")

        # Stylizing
        global can
        can = Canvas(root)
        can.configure(bg=darker_grey, highlightthickness=0)
        can.place(x=0, y=0, width=width, height=height)

        # Tree stylizing
        style = ttk.Style(root)
        style.configure("My.Treeview", background=darker_grey)

        v = Scrollbar(root, orient='vertical')
        v.pack(side=RIGHT, fill='y')

        # main area setup
        mainArea = Text(root, wrap= WORD, yscrollcommand=v.set)
        mainArea.place(x=int(width*0.12), y=0, width=int(width*0.88), height=int(height))

        # Tree setup
        global tree
        tree = ttk.Treeview(root)
        tree.configure(style="My.Treeview")
        tree.tag_configure("row", background=darker_grey)
        tree.place(x=0, y=0, width=int(width*0.12), height=height)

        # file menu
        file = Menu(menubar, bg=darker_grey, fg="white", activebackground=light_purple, activeforeground=darker_grey, bd=0, borderwidth=0)
        menubar.add_cascade(menu=file, label="File")
        file.add_command(label="New File")
        file.add_command(label="Save File")
        file.add_command(label="Open File")
        file.add_command(label="Exit", command=self.quit)

        # window menu
        window = Menu(menubar, bg=darker_grey, fg="white", activebackground=light_purple, activeforeground=darker_grey, bd=0)
        menubar.add_cascade(menu=window, label="Window")
        window.add_command(label="File Manager")
        window.add_command(label="Time Line")
        
        # setting menu
        setting = Menu(menubar, bg=darker_grey, fg="white", activebackground=light_purple, activeforeground=darker_grey, bd=0)
        menubar.add_cascade(menu=setting, label="Setting")
        setting.add_command(label="Preferences")

        '''
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
        '''

    def setDir(startPath, parent):
        dirs = [e for e in startPath.iterdir() if e.is_dir()]
        files = [e for e in startPath.iterdir() if e.is_file()]
        print(type(files))
        print(files)
        for j in range(len(dirs)):
            dirName = os.path.basename(dirs[j])
            if parent == None:
                tree.insert("", index="end", iid=str(dirName), text=str(dirName))
            else:
                tree.insert(parent, index="end", iid=str(dirName), text=str(dirName))
            main.setDir(dirs[j], str(dirName))

        for i in range(len(files)):
            filName = os.path.basename(files[i])
            tree.insert("", index="end", iid=str(filName), text=str(filName))

    def quit(self):
        root.destroy()

main()
main.setDir(savePath, None)

root.mainloop()