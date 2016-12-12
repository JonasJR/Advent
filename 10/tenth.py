from collections import defaultdict

with open("data.txt", "r") as fp:
    data = fp.read().strip()

bots = defaultdict(defaultdict)
outputs = defaultdict(list)

def deliver(botn):
    lt, lv = bots[botn]["low"]
    ht, hv = bots[botn]["high"]
    low, high = (min(bots[botn]["holds"]), max(bots[botn]["holds"]))
    bots[botn]["holds"] = []

    if 17 == low and 61 == high:
        print "Answer #1:", botn

    if lt == "bot":
        if "holds" not in bots[lv]: bots[lv]["holds"] = []
        bots[lv]["holds"].append(low)
        if len(bots[lv]["holds"]) == 2:
            deliver(lv)
    else:
        outputs[lv].append(low)

    if ht == "bot":
        if "holds" not in bots[hv]: bots[hv]["holds"] = []
        bots[hv]["holds"].append(high)
        if len(bots[hv]["holds"]) == 2:
            deliver(hv)
    else:
        outputs[hv].append(high)

for line in data.split("\n"):
    args = line.split()
    if args[0] == "bot":
        botn = int(args[1])
        bots[botn]["low"] = (args[5], int(args[6]))
        bots[botn]["high"] = (args[10], int(args[11]))
    else:
        botn = int(args[5])
        if "holds" not in bots[botn]: bots[botn]["holds"] = []
        bots[botn]["holds"].append(int(args[1]))

for botn in bots.iterkeys():
    if "holds" in bots[botn] and len(bots[botn]["holds"]) == 2:
        deliver(botn)

print "Answer #2:", outputs[0][0] * outputs[1][0] * outputs[2][0]
