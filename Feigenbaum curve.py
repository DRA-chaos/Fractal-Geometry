import tkinter as tk
from tkinter import *
import random

root=Tk()

w = 600
win = Canvas(root,height=w,width=w)
win.grid(row=0,columnspan=2)

def f(a,x):
    return a * x * (1-x)


Label(root,text='aMin=',font=('Arial',16)).grid(row=1)
minA_Input=StringVar()
e1=Entry(root,textvariable=minA_Input)
e1.grid(row=1,column=1)
minA_Input.set(0)

Label(root,text='aMax=',font=('Arial',16)).grid(row=2)
maxA_Input=StringVar()
e2=Entry(root,textvariable=maxA_Input)
e2.grid(row=2,column=1)
maxA_Input.set(4)

Label(root,text='Iterations=',font=('Arial',16)).grid(row=3)
iter_Input=StringVar()
e3=Entry(root,textvariable=iter_Input)
e3.grid(row=3,column=1)
iter_Input.set(100)

def _draw():
    win.delete('all')
    minA=float(minA_Input.get())
    maxA=float(maxA_Input.get())
    maxIts =int(iter_Input.get())

    a=minA

    while a <= maxA:
        x = random.random()#random number between 0 and 1
        plotX = (a-minA)*w/(maxA-minA)
        for numit in range(maxIts):
            if numit > 0.5 * maxIts or numit > 100:
                win.create_line(plotX,w-w*x,plotX+1,w-w*x+1)
            x = f(a,x)    
        a += (maxA-minA)/w



btn = Button(root,text='Draw',command=_draw,font=('Arial',16))
btn.grid(row=4)


if __name__ == '__main__':
    root.mainloop()

    
    

    
