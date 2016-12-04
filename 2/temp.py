import sys
instructions = []
current = (0,2)
keypad = [['x', 'x', '1', 'x', 'x'],
       ['x', '2', '3', '4', 'x'],
       ['5', '6', '7', '8', '9'],
       ['x', 'A', 'B', 'C', 'x'],
       ['x', 'x', 'D', 'x', 'x'],]

limits = {"U": (0, -1), "D": (0, 1),
         "L": (-1, 0), "R": (1, 0),
         }

def init():
    with open('data.txt') as f:
        for line in f:
            instructions.append(line)


def main():
    global current
    for line in instructions:
        l = list(line)
        for instruction in l:
            if instruction is not '\n':
                new_cur = (max(0, min(current[0] + limits[instruction][0], 4)),
                       max(0, min(current[1] + limits[instruction][1], 4)))
                if keypad[new_cur[1]][new_cur[0]] is not 'x':
                    current=new_cur
        print(current)

init()
main()
