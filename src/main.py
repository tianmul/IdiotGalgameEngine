import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter!")
path = "./main.jpg"
logo = ImageTk.PhotoImage(Image.open(path))

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()
