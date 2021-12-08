import sys
sys.path.append("..")
from common import *

def parse(d):
    return tuple([p.strip().split(" ") for p in d.strip().split("|")])

data = fnl(parse)

print(data)

snum = {
    0: set(["t1","l1","l2","r1","r2","t3"]),
    1: set(["r1","r2"]),
    2: set(["t1","r1","t2","l2","t3"]),
    3: set(["t1","r1","t2","r2","t3"]),
    4: set(["l1","r1","t2","r2"]),
    5: set(["t1","l1","t2","r2","t3"]),
    6: set(["t1","l1","t2","r2","l2","t3"]),
    7: set(["t1","r1","r2"]),
    8: set(["t1","l1","l2","t2","r1","r2","t3"]),
    9: set(["t1","l1","t2","r1","r2","t3"]),
}

count = 0
for rec in data:
    numbers = {}
    segments = {}
    segments2 = {}
    sixes = []
    fives = [] 
    for output in rec[0]:
        l = len(output) 
        if l == 2: numbers[1] = output
        elif l == 3: numbers[7] = output
        elif l == 4: numbers[4] = output
        elif l == 7: numbers[8] = output
        elif l == 5: fives.append(output)
        elif l == 6: sixes.append(output)
    for ch in numbers[1]:
        if sum([1 for f in sixes if not ch in f]) == 1:
            segments[ch] = "r1"
            segments2["r1"] = ch
        else:
            segments[ch] = "r2"
            segments2["r2"] = ch
    a = list(filter(lambda ch: not ch in segments,numbers[7]))[0]
    segments[a] = "t1"
    segments2["t1"] = a
    for ch in numbers[4]:
        if not ch in segments:
            if sum([1 for f in fives if ch in f]) == 3:
                segments[ch] = "t2"
                segments2["t2"] = ch
            else:
                segments[ch] = "l1"
                segments2["l1"] = ch
    for ch in numbers[8]:
        if not ch in segments:
            if sum([1 for f in sixes if not ch in f]) == 1:
                segments[ch] = "l2"
                segments2["l2"] = ch
            else:
                segments[ch] = "t3"
                segments2["t3"] = ch
    conv = [set([segments[s] for s in n]) for n in rec[1]]
    str = ""
    for c in conv:
        for n in snum:
            if c == snum[n]:
                str += "{}".format(n)
    count += int(str)
    print(str)

print(count)