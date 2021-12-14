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
# pprint(goal)
# pprint(ins)

def genpairs(str):
    pairs = defaultdict(int)
    ch = defaultdict(int)
    for i in range(len(str)-1):
        ch[str[i]] += 1
        pairs[str[i] + str[i+1]] += 1
    ch[str[i+1]] += 1
    return pairs,ch

pairs,ch = genpairs(goal)
steps = 40
for i in range(steps):
    print("step:",i)
    next = defaultdict(int)
    for p in [*pairs.keys()]:
        mid = ins[p]
        ch[mid] += pairs[p]
        next[p[0] + mid] += pairs[p]
        next[mid + p[1]] += pairs[p]
    pairs = next

pprint(pairs)
pprint(ch)
all = [ch[k] for k in ch]
print(max(all)-min(all))