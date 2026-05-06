from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1650x1000")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("gui.gif")#enter the gif address)
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("ironman_airborne.mp3")#enter the music file address)
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1650,1000))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.02)
    root.destroy()

play_gif()
root.mainloop()