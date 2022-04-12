from tkinter import *

import tkinter.messagebox

root = Tk()

def func(label):
    tkinter.messagebox.askquestion("Information", "you have selected: {}".format(label))


mymenu = Menu(root)
root.config(menu = mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="file", menu=submenu)
submenu.add_command(label="project", command=lambda: func("project"))
submenu.add_command(label= "save", command=lambda: func("save"))
submenu.add_separator()
submenu.add_command(label="exit", command=lambda: func("exit"))

root.mainloop()
