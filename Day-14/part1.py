import sys
sys.path.append("..")
from common import *

def parse(d):
    d = d.split("\n")
    goal = d[0]
    gens = {}
    for i in d[2:]:
        t = i.split("->")
        gens[t[0].strip()] = t[1].strip()
    return (goal,gens)

goal,ins = aoci(parse)
pprint(goal)
pprint(ins)

start = goal
steps = 40
for i in range(steps):
    print("step:",i)
    next = ""
    for i in range(len(start)-1):
        next += start[i]
        if start[i] + start[i+1] in ins:    
            next += ins[start[i] + start[i+1]]
    next += start[-1]
    start = next

nch = freq(start)
pprint(nch)
all = [nch[k] for k in nch]
print(max(all)-min(all))