import tkinter as tk
from tkinter import *

w = 600 #canvas width/height

root = tk.Tk()

win = tk.Canvas(root,width = w, height = w, background='blue')
win.pack(side = tk.LEFT)

frm = tk.Frame(root)
frm.pack(side = tk.RIGHT)

Label(frm,text='f(x)=ax(1-x) ',font=('Arial',20)).grid(row=0)

if __name__ == '__main__':
    root.mainloop()
    
