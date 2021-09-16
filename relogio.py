from tkinter import *
import tkinter
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")

color1 = "#3d3d3d"
color2 = "#fafcff"
color3 = "#21c25c"
color4 = "#eb463b"
color5 = "#3080f0"

background = color1
color = color2

screen = Tk()
screen.title("Timer")
screen.geometry("460x200")
screen.resizable(width=True, height=True)
screen.configure(bg=background)


def watch():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    dayWeek = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")

    l1.config(text=hour)
    l1.after(200, watch)
    l2.config(text=dayWeek + ", " + str(day) +
              "/" + str(month)+"." + "/" + str(year))


l1 = Label(screen, text="", font=("digital-7 80"), bg=background, fg=color)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(screen, text="", font=("digital-7 20"), bg=background, fg=color)
l2.grid(row=1, column=0, sticky=NW, padx=5)

watch()
screen.mainloop()
