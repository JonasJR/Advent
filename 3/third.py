input = open("data.txt", 'r').readlines()

def part1():
    triangles = 0
    for sides in input:
        line = sides.split()
        t = [int(line[0]), int(line[1]), int(line[2])]
        t.sort()
        if ((t[0] + t[1]) > t[2]):
            triangles += 1
    print (triangles)

def part2():
    trigs = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    dimension = 0
    count = 0
    for sides in input:
        line = sides.split()
        for i in range(0, 3):
            trigs[i][dimension] = int(line[i])
        if dimension is not 2:
            dimension += 1
            continue
        else:
            dimension = 0
            for i in range(0, 3):
                t = trigs[i]
                if ((t[0] + t[1]) > t[2]):
                    count += 1
            trigs = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    print (count)
part2()
