import turtle

iterations=input("Enter the number of generations :")
iterations=int(iterations)
startLength=200 #Length of generation 0 line (200 pixels)
#Pick up the pen and move the turtle over to the left
turtle.up()
turtle.setpos(-startLength*3/2, 0)
turtle.speed(0)
koch='F'
# make the final L system based on the number of iterations
for i in range(iterations):
    koch=koch.replace('F','FLFRFRFFLFLFRF')
turtle.down()
turtle.color('red','black')
turtle.begin_fill()
for move in koch:
    if move=='F':
        turtle.forward(startLength/(3**(iterations-1)))
    elif move=='R':
        turtle.right(90)
    elif move=='L':
        turtle.left(90)
turtle.end_fill()
