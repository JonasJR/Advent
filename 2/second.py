import sys
instructions = []
current = [2,2]
keypad = [['x', 'x', '1', 'x', 'x'],
       ['x', '2', '3', '4', 'x'],
       ['5', '6', '7', '8', '9'],
       ['x', 'A', 'B', 'C', 'x'],
       ['x', 'x', 'D', 'x', 'x'],]

def init():
    with open('data.txt') as f:
        for line in f:
            instructions.append(line)


def main():
    for line in instructions:
        l = list(line)
        for instruction in l:
            if instruction == 'U':
                goUp()
            elif instruction == 'R':
                goRight()
            elif instruction == 'D':
                goDown()
            elif instruction == 'L':
                goLeft()
        print(current)

def goDown():
    if current[0] is not 5:
        new_cur = current[0]+1
        
        current[0]+=1

def goRight():
    if current[1] is not 5:
        current[1]+=1

def goUp():
    if current[0] is not 1:
        current[0]-=1

def goLeft():
    if current[1] is not 1:
        current[1]-=1

init()
main()
