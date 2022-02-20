from tkinter import *
import time, random
time.sleep(3)

#Global variables
gridSize = 10 #side length of each square in grid, in pixel
screenSize = 1000
numCells = int(screenSize/gridSize)

win = Canvas(Tk(),width = screenSize, height = screenSize)

#This is my CA matrix
CA = [[0 for x in range(numCells)] for y in range(numCells)]


#Clear the canvas object, redraw grid
def InitCanvas():
    win.delete('all')

    #draw grid
    for i in range(numCells):
        win.create_line(0,gridSize * i, screenSize, gridSize * i)
        win.create_line(gridSize * i, 0, gridSize * i, screenSize)
    win.pack()

def RefreshGrid():
    global CA

    InitCanvas()

    #Just going to paint the live cells in the CA
    for i in range(numCells):
        for j in range(numCells):
            if CA[i][j] == 1:
                x1 = gridSize * i
                y1 = gridSize * j
                win.create_rectangle(x1,y1,x1+gridSize,y1+gridSize,fill='black')
    win.update()

def MRule():
    global CA

    CAnext = [[0 for x in range(numCells)] for y in range(numCells)]

    for i in range(numCells):
        for j in range(numCells):
            lives = 0

            if CA[(i+0)%numCells][(j+1)%numCells] == 1:
                lives += 1
            if CA[(i+0)%numCells][(j-1)%numCells] == 1:
                lives += 1
            if CA[(i+1)%numCells][(j+0)%numCells] == 1:
                lives += 1
            if CA[(i-1)%numCells][(j+0)%numCells] == 1:
                lives += 1
            if CA[(i+1)%numCells][(j+1)%numCells] == 1:
                lives += 1
            if CA[(i+1)%numCells][(j-1)%numCells] == 1:
                lives += 1
            if CA[(i-1)%numCells][(j+1)%numCells] == 1:
                lives += 1
            if CA[(i-1)%numCells][(j-1)%numCells] == 1:
                lives += 1
            if CA[(i+0)%numCells][(j+0)%numCells] == 1:
                lives += 1

            if lives >= 5:
                CAnext[i][j] = 1
            else:
                CAnext[i][j] = CA[i][j]


            
    CA = CAnext
    RefreshGrid()
            

                
if __name__ == '__main__':

    #Randomly seed the board
    for i in range(numCells):
        for j in range(numCells):
            if random.randint(1,100) < 33:
                CA[i][j] = 1
            else:
                CA[i][j] = 0

    RefreshGrid()

    generations = 1000

    for i in range(generations):
        #time.sleep(0.1)
        MRule()
