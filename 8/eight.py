import numpy as np
import collections

input = open("data.txt", "r")

grid = np.zeros((6,50))

for line in input:
    if line.startswith("rect"):
        s = line.split(" ")
        a = s[1].split("x")
        for i in range(0, int(a[0])):
            for j in range(0, int(a[1])):
                grid[j][i] = 1
    else:
        s = line.split(" ")
        row_col = s[2].split("=")
        amount = s[4]
        if row_col[0] == "y":
            grid[int(row_col[1])] = np.roll(grid[int(row_col[1])], int(amount))
        else:
            grid[:,int(row_col[1])] = np.roll(grid[:,int(row_col[1])], int(amount))

f = open("output.txt","w")
print(grid, file=f)
f.close()
