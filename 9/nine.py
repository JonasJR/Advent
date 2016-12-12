import re
import sys

input = open("data.txt", "r").read().strip()
lines = input.strip()
part2 = False

def count_len(l):
    count = 0
    while True:
        try:
            ind = l.index(")")
        except:
            break

        a, b = map(int, re.findall(r'\d+', l[:ind]))

        seg = l[ind + 1:ind + 1 + a]

        if seg.startswith("(") and part2:
            count += count_len(seg) * b
        else:
            count += (a * b)
        l = l[ind + 1 + a:]
    return count

print(count_len(lines))
part2 = True
print(count_len(lines))
