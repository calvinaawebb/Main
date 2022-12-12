import _tkinter
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pathlib
from pathlib import *

'''
IDEAS FOR THE PROJECT:
Make a labeling system that color codes list entries
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
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.update()
width = root.winfo_width()
height = root.winfo_height()
print(width, height)

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
        style.configure("My.Treeview", background=darker_grey, foreground=light_purple)

        # main area setup
        self.mainArea = Text(root, wrap= WORD)
        self.mainArea.place(x=int(width*0.12), y=0, width=int(width*0.88), height=int(height))

        # scrollbar
        vert = Scrollbar(root, orient='vertical', command= self.mainArea.yview)
        vert.pack(side=RIGHT, fill='y')

        self.mainArea.configure(yscrollcommand=vert.set)

        # Tree setup
        global tree
        tree = ttk.Treeview(root)
        tree.tag_configure("row", background=darker_grey)
        tree.place(x=0, y=0, width=int(width*0.12), height=height)
        tree.bind('<Button-1>', self.openFile)

        # this is here because it needs to be after tree
        #long = Scrollbar(root, orient='vertical', command=tree.yview)
        #long.place(x=int(width*0.12), height=int(height))
        tree.configure(style="My.Treeview") # , yscrollcommand=long.set)

        # file menu
        file = Menu(menubar, bg=darker_grey, fg="white", activebackground=light_purple, activeforeground=darker_grey, bd=0, borderwidth=0)
        menubar.add_cascade(menu=file, label="File")
        file.add_command(label="New File")
        file.add_command(label="Save File")
        file.add_command(label="Open Directory", command=self.open)
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

        if width == root.winfo_width():
            print("yes")

    def setDir(startPath, parent, count):
        if parent is None:
            for item in tree.get_children():
                tree.delete(item)
        try:
            dirs = [e for e in startPath.iterdir() if e.is_dir()]
            files = [e for e in startPath.iterdir() if e.is_file()]
            #print(type(files))
            #print(files)
            for j in range(len(dirs)):
                if len(tree.get_children()) != 0:
                    count += 1
                print("count:" + str(count))
                dirName = os.path.basename(dirs[j])
                if parent == None:
                    try:
                        tree.insert("", index="end", iid=str(dirs[j]), text=str(dirName))
                    except _tkinter.TclError:
                        print(str(dirs[j]))
                        tree.insert("", index="end", iid=str(dirs[j]), text=str(dirName))
                        #count += 1
                    except PermissionError:
                        pass
                else:
                    try:
                        tree.insert(parent, index="end", iid=str(dirs[j]), text=str(dirName))
                    except _tkinter.TclError:
                        print("parent:" + parent)
                        print("child:" + str(dirs[j]))
                        tree.insert(parent, index="end", iid=str(dirs[j]), text=str(dirName))
                        #count += 1
                    except PermissionError:
                        pass
                print("count:" + str(count))
                print("addition:" + str(dirs[j]))
                for i in range(len(files)):
                    try:
                        filName = os.path.basename(files[i])
                        if parent is None:
                            tree.insert("", index="end", iid=str(files[i]), text=str(filName))
                        else:
                            tree.insert(str(dirs[j]), index="end", iid=str(files[i]), text=str(filName))
                    except _tkinter.TclError:
                        pass

                main.setDir(dirs[j], str(dirs[j]), count)
            for i in range(len(files)):
                filName = os.path.basename(files[i])
                try:
                    if count == 0:
                        tree.insert("", index="end", iid=str(files[i]), text=str(filName))
                except _tkinter.TclError:
                    pass
        except PermissionError:
            pass


    def openFile(self, event):
        print(len(self.mainArea.get("1.0", "end-1c")))
        if len(self.mainArea.get("1.0", "end-1c")) != 0:
            self.mainArea.delete("1.0", "end")
        else:
            curId = tree.focus()
            curItem = tree.item(curId)
            if not tree.get_children(curId) and curItem["text"].endswith(".txt"):
                print(curId)
                file = open(curId, "r")
                self.mainArea.insert("1.0", file.read())
                print("????")


    def quit(self):
        root.destroy()

    def open(self):
        file_path = filedialog.askdirectory()
        print(savePath)
        filePath = Path(file_path)
        print(filePath)
        main.setDir(filePath, None, 0)

main()
'''
file_path = filedialog.askdirectory()
filePath = Path(file_path)
print(filePath)
#filePath = file_path.replace('/', '\\')
'''
main.setDir(savePath, None, 0)

def wait(event):
    print("wait")

root.mainloop()