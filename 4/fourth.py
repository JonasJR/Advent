import re
import collections
import string

alpha = "abcdefghijklmnopqrstuvwxyz"

input = open("data.txt", 'r').readlines()
def set_new_index(l,d):
    i = string.ascii_lowercase.index(l)
    for number in range(0,d):
        if i is not 25:
            i += 1
        else:
            i = 0
    return i

def real_name(s,d):
    new_string = ""
    for l in s:
        if l is not " ":
            new_string += new_string.join(alpha[set_new_index(l,d)])
        else:
            new_string += new_string.join(' ')
    return new_string


def most_frequent(s):
    counter = collections.Counter(s)
    most_common = sorted(counter.items(), key=lambda pair: (-pair[1], pair[0]))
    most_common = most_common[:5]
    check = ""
    for letter, count in most_common:
        check += check.join(letter)
    return check

def make_name(n):
    name = n.replace("-", "")
    return name

def make_name2(n):
    name = n.replace("-", " ")
    return name

def find_north(r):
    for room in r:
        name = real_name(room[0],room[1])
        print("{} - {}".format(name, room[1]))

def main():
    totalSum = 0
    realRooms = []
    for line in input:
        realRoom = []
        s = re.split(r'(^[^\d]+)', line)[1:]
        name = make_name(s[0])
        name2 = make_name2(s[0])
        realCheckSum = most_frequent(name)

        code = s[1].split("[")
        sectorID = code[0]
        checksum = code[1]
        checksum = checksum[:-2]

        if realCheckSum == checksum:
            realRoom.append(name2)
            realRoom.append(int(sectorID))
            realRoom.append(realCheckSum)
            realRooms.append(realRoom)
            totalSum += int(sectorID)
    find_north(realRooms)
    print(totalSum)
main()
