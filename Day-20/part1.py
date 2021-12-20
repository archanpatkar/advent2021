import sys
sys.path.append("..")
from common import *

def parse(d):
    out = []
    lines = d.split("\n")
    out.append(lines[0])
    image = defaultdict(lambda: ".")
    total = 0
    lines = lines[2:]
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            image[(x,y)] = lines[y][x]
            total += 1
    return (out[0],image,len(lines),total)

str,image,const,total = aoci(parse)

pprint(image)

graph = {}
def nbs(pixel):
    if point in graph: return graph[pixel]
    graph[pixel] = n8(pixel)
    return graph[pixel]

index = lambda pixel: int("".join([image[n] for n in nbs(pixel)]).replace("#","1").replace(".","0"),base=2)
last = "."
default = {
    ".":"#",
    "#":"."
}

for i in range(2):
    print("i:",i)
    nextimage = defaultdict(lambda: default[last])
    last = default[last]
    done = set()
    notdone = []
    for pixel in [*image.keys()]:
        ch = str[index(pixel)]
        nextimage[pixel] = ch
        done.add(pixel)
        notdone.extend([n for n in nbs(pixel) if n not in done])
    while len(notdone) > 0:
        pixel = notdone.pop(0)
        if pixel not in done:
            i = index(pixel)
            done.add(pixel)
            if (last == "#" and i != 0) or (last == "." and i != 511):
                notdone.extend([n for n in nbs(pixel) if n not in done and n not in notdone])
            nextimage[pixel] = str[i]
    image = nextimage

pprint(sum([1 if image[p] == "#" else 0 for p in image]))