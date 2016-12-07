import re

input = open("data.txt", 'r').readlines()

def find_double(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))

def find_ssl(sn, hn):
    return any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:]))
def split_line(s):
    parts = re.split(r'\[([^\]]+)\]', s)
    sn = ' '.join(parts[::2])
    hn = ' '.join(parts[1::2])
    return sn, hn

def main():
    supports = 0
    ssl = 0
    for line in input:
        sn, hn = split_line(line)
        if find_double(sn) and not find_double(hn):
            supports += 1
        if find_ssl(sn, hn):
            ssl += 1
    print(supports)
    print(ssl)
main()
