data = open("data.txt", "r")
lines = []
registres = {"a":0,"b":0,"c":1,"d":0}
count = 0

for line in data:
    lines.append(line)

def reg_or_num(x):
    try:
        return int(x)
    except:
        return registres[x]

def main():
    count = 0
    while True:
        if count >= len(lines):
            break
        instr = lines[count].split()
        if instr[0] == "cpy":
            registres[instr[2]] = reg_or_num(instr[1])
        elif instr[0] == "inc":
            registres[instr[1]] += 1
        elif instr[0] == "dec":
            registres[instr[1]] -= 1
        elif instr[0] == "jnz":
            if reg_or_num(instr[1]) != 0:
                count += reg_or_num(instr[2])
                count -= 1
        count += 1
main()
print(registres["a"])
