import sys
sys.path.append("..")
from common import *

def parse(d):
    return [int(n) for n in d]

data = fnl(parse)

octos = {}
for y,line in enumerate(data):
    for x,o in enumerate(line): 
        octos[(x,y)] = o

adj = lambda x,y: [
    (x,y-1),(x,y+1),(x-1,y),
    (x+1,y),(x+1,y-1),(x-1,y+1),
    (x+1,y+1),(x-1,y-1)
]

flashes = 0
step = 1
while True:
    for o in octos: 
        octos[o] += 1
    flashed = []
    toflash = [o for o in octos if octos[o] > 9]
    while len(toflash) != 0: 
        o = toflash.pop(0)
        flashed.append(o)
        flashes += 1
        octos[o] = 0
        surr = adj(o[0],o[1])
        for s in surr:
            if (s in octos) and octos[s] != 0 and octos[s] <= 9:
                octos[s] += 1
                if octos[s] > 9: toflash.append(s)
    for o in flashed: octos[o] = 0
    if(len(flashed) == len(octos.keys())): break
    step += 1
print(step)