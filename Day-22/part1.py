import sys
sys.path.append("..")
from common import *

def parse(d):
    d = d.split(" ")
    cords = dict()
    for c in d[1].split(","):
        c = c.split("=")
        cords[c[0]] = tuple(map(int,c[1].split("..")))
    return (d[0],cords)

data = fnl(parse)

opp = {
"on":"off",
"off":"on"
}

cubemap = defaultdict(int)
duplicates = 0
for cuboid in data:
    for x in range(cuboid[1]["x"][0],cuboid[1]["x"][1]+1):
        if x >= -50 and x <= 50:
            for y in range(cuboid[1]["y"][0],cuboid[1]["y"][1]+1):
                if y >= -50 and y <= 50:
                    for z in range(cuboid[1]["z"][0],cuboid[1]["z"][1]+1):
                        if z >= -50 and z <= 50:
                            cubemap[(x,y,z)] = 1 if cuboid[0] == "on" else 0

print(sum([cubemap[c] for c in cubemap]))