import sys
import time
time.sleep(20)

def rule30(N):

    cells = range(-N, N+1)

    #initial conditions
    CA = {i: '0' for i in cells}
    CA[0] = '1'
    #padding
    CA[-(N+1)] = '0'
    CA[N+1] = '0'

    #Define rule 30
    rules = {'111':'0', '110':'0', '101':'0', '000':'0',
             '100':'1', '011':'1', '010':'1', '001':'1'}

    for step in range(N):

        #print current state
        for i in cells:
            if CA[i] == '1':
                sys.stdout.write(u'\u2588')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')

        #evolve it

        #3 digit
        patterns = {i: CA[i-1] + CA[i] + CA[i+1] for i in cells}

        #Next generation
        CA = {i: rules[patterns[i]] for i in cells}
        CA[-(N+1)]='0'
        CA[N+1]='0'
    
if __name__ == '__main__':
    rule30(40)
