import os
os.system('cmd /c "pip install playsound wheel pillow"')

from tkinter import *
import time
import random
from playsound import playsound
from PIL import Image, ImageTk

windows = []
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.overrideredirect(True)
root.resizable(False, False)
root.geometry("+-100+0")
root.geometry(str(width+500)+"x"+str(height+500))

labels = []

sfx = ["AMOGUS", "AMONGUS", "BRUH", "CRAP", "DUNNNN", "E", "WHENTHEIMPOSTREISUS"]
imgs = ["AMOGUS", "AMONGUS", "SUSJERMA"]

while True:
    rng = random.randrange(1, len(sfx)+1, 1)

    windows.append(Toplevel())
    windows[len(windows)-1].geometry("+"+str(random.randrange(1, width, 1))+"+"+str(random.randrange(1, height, 1)))
    windows[len(windows)-1].wm_attributes("-topmost", 1)
        
    img = Image.open("images/"+imgs[random.randrange(1, len(imgs), 1)]+".png")
    tkimage = ImageTk.PhotoImage(img)
    labels.append(Label(windows[len(windows)-1],image=tkimage))
    labels[len(labels)-1].pack()
    root.update_idletasks()
    root.update()
    windows[len(windows)-1].update_idletasks()
    windows[len(windows)-1].update()
    
    playsound("sounds/"+sfx[rng-1]+".mp3", False)
