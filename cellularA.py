def CA():

    numCells=64
    CA=[]
    for i in range(numCells):
        CA.append(0)
    CA[32]=1 # initial condition

    dic={0: '' , 1 : '*'}

    print(''.join([dic[e] for e in CA]))

    for step in range(32):
        caNew=[]
        for i in range (numCells):
            if CA[(i-1)%numCells]==CA[(i+1)%numCells]:
                caNew.append(0)
            else:
                caNew.append(1)
        print(''.join([dic[e] for e in caNew]))
        CA=caNew

if __name__=='__main__':
    CA()
