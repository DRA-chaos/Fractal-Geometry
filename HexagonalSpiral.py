#Hexagonal spiral
from turtle import*
color=['red' , 'blue' , 'green' , 'yellow' , 'pink']
bgcolor('black')
speed(0)
for x in range(100):
    pencolor(color[x%5])
    forward(x)
    left(60)


