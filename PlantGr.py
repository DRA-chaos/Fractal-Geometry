import turtle

def setTurtle(myTuple):
    t.up()
    t.setx(myTuple[0])
    t.sety(myTuple[1])
    t.setheading(myTuple[2])
    t.down()

def make_fractal(length,langle,rangle,iterations,axiom,target,replace,target2,replace2):
    state = axiom
    turtleState=[]
    
    #make the L-System we want to process
    for i in range(iterations):
        nextState=''
        for character in state:
            if character == target:
                nextState += replace
            elif character == target2:
                nextState += replace2
            else:
                nextState += character
        state = nextState

    for move in state: 
        if move == '[':
            turtleState.append((t.xcor(),t.ycor(),t.heading()))
        elif move == ']':
            setTurtle(turtleState.pop())
        elif move == "F":
            t.forward(length)
        elif move == "L":
            t.left(langle)
        elif move == "R":
            t.right(rangle)

if __name__ == '__main__':
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))
    t = turtle.Turtle()
    t.speed(0)
    turtle.bgcolor('black')
    t.color('green','black')
    setTurtle((0,-250,90))

    #Simple plant
    make_fractal(myLen,25,25,iterations,'B','F','FF','B','F[RB]F[LB]RB')

   
