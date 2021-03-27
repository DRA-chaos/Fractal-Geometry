def cantor_set(x,y,l):
    if l>1:
        win.create_line(x,y,x+1,y)
        y=y+50
        cantor_set(x,y,l/3)
        cantor_set(x+2/3*l,y,l/3)
from tkinter import *
w,h=1500,500
win=Canvas(Tk(),width=w,height=h)
win.pack()
cantor_set(10,10,w-20)
