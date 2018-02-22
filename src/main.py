# -*- coding: utf-8 -*- 
from tkinter import *
from PIL import ImageTk, Image
from menuPage import *

root = Tk()
root.title("MyGalgame")
root.geometry('1280x720')

mP = MenuPage(root, "./main.jpg")
mP.pack(fill=BOTH, expand=YES)

root.resizable(0, 0)
root.mainloop()