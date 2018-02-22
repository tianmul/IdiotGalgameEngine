from tkinter import *
from PIL import ImageTk, Image


class MenuPage(Frame):
    def __init__(self, master, picLoc, *pargs):
        
        Frame.__init__(self, master, *pargs)
        
        #set button 1
        self.but1_image = Image.open("./firstBut.png")
        self.but1_image_copy = self.but1_image.copy()        
        #self.but1_image = self.but1_image_copy.resize((150, 50))
        self.but1_bg_image = ImageTk.PhotoImage(self.but1_image)
        
        self.b1 = Button(master,
                         bd = 0,
                         text="Game Start",
                         image=self.but1_bg_image,
                         compound="center", height=40, width=140,
                         relief = "sunken",
                         command = self.bt1)
        self.b1.place(relx=.25, rely=.85, anchor="c")
        
        
        #set background 1
        self.image = Image.open(picLoc)
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
        
        
    def bt1(self):
        print("Game Start")
        

