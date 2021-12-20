import sys
sys.path.append("..")
from common import *
from random import choice

def parse(d):
    d = d.split("\n")
    scanners = []
    curr = []
    for l in d[1:]:
        if len(l) == 0:
            scanners.append(curr)
            curr = []
        elif not l.startswith("--- scanner"): curr.append(tuple(map(int,l.split(","))))
    scanners.append(curr)
    return scanners

data = aoci(parse)

copydata = list(data)

all_points = []
for p in data: all_points.extend(p)

pprint(data)
print(len(data))

pos = ["x","y","z","-x","-y","-z"]

variation = []
for c in permutations(pos,3):
    f = freq(c)
    x = f["x"] + f["-x"]
    y = f["y"] + f["-y"]
    z = f["z"] + f["-z"]
    if x == 1 and y == 1 and z == 1:
        variation.append(c)

axis_index = {
    "x":0,
    "y":1,
    "z":2
}

# ascii diagrams visually exploring rotations of scanners
#    t 
#    - b
# l | | r
# f  -
#    b

#    -z  y
#     \  |
# -x  - cube -  x
#        |  \ 
#       -y   z

def get_all_orients(scanner):
    scanner = data[scanner]
    orients = []
    for v in variation:
        all = []
        for beacon in scanner:
            nx = []
            for ch in v:
                if ch.startswith("-"): nx.append(-beacon[axis_index[ch[1]]])
                else: nx.append(beacon[axis_index[ch]])
            all.append(tuple(nx))
        orients.append(tuple(all))
    return orients

# scatter3d(x,y,z,"Beacons")

def manhdis(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

def eucdis(p1,p2):
    return sqrt(((p2[0]-p1[0]) ** 2) + ((p2[1]-p1[1]) ** 2) + ((p2[2]-p1[2]) ** 2))

def subpoint(p1,p2):
    return (p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2])

def addpoint(p1,p2):
    return (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2])


def find_next_scanner(curr,done=set()):
    print("overlaps")
    isdone = []
    done.add(curr)
    for o1 in [data[curr]]:
        for i in range(len(data)):
            if i not in done:
                for o2 in get_all_orients(i):
                    dmap = defaultdict(lambda: [])
                    for p1 in o1:
                        for p2 in o2:
                            dis = eucdis(p1,p2)
                            dmap[dis].append((p1,p2))
                    match = [p for p in dmap if len(dmap[p]) >= 12]
                    if len(match) > 0: isdone.append((None,dmap[match[0]],o1,o2,i))
    if len(isdone) > 0:
        output = []
        for dones in isdone:
            real = {}
            common = set()
            remove = set()
            for a in dones[1]:
                real[a[1]] = a[0]
                common.add(a[0])
                remove.add(a[1])
            modified = set(dones[3]).difference(remove)
            p = choice(list(remove))
            fromorigin = set()
            for n in modified:
                diff = subpoint(n,p)
                fromorigin.add(addpoint(real[p],diff))
            scanner_pos = addpoint(real[p],subpoint((0,0,0),p))
            output.append((dones[4],scanner_pos,list(fromorigin.union(common))))
        return output
    return False

# part 1
scanners = [0]
all_beacons = set(data[0])
done = set([0])
scanner_positions = {0:(0,0,0)}
while True:
    if len(scanners) == 0: break
    pprint(scanner_positions)
    s = scanners.pop(0)
    out = find_next_scanner(s,done=done)
    if out:
        done.add(s)
        for o in out:
            curr,pos,points = o
            if curr not in scanners and curr not in done:
                scanners.append(curr)
                data[curr] = points
                all_beacons.update(points)
                scanner_positions[curr] = pos
print(len(all_beacons)) 

scanner_dis = []
for s1 in scanner_positions:
    for s2 in scanner_positions:
        if s1 != s2:
            scanner_dis.append(manhdis(scanner_positions[s1],scanner_positions[s2]))
print(max(scanner_dis))