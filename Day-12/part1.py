import sys
sys.path.append("..")
from common import *

def parse(d):
    return tuple(d.split("-"))

data = fnl(parse)

caves = defaultdict(lambda: [])

for c in data:
    caves[c[0]].append(c[1])
    caves[c[1]].append(c[0])

pprint(caves)

def findpath(start,end,g,path=[]):
    if(start == end): return [[*path,start]]
    paths=[]
    for n in g[start]:
        curr = [*path,start]
        if not n in path or (not n.islower()):
            paths.extend(list(filter(lambda p: len(p) > 0, findpath(n,end,caves,curr))))
    return paths

paths = findpath("start","end",caves)
# pprint(paths)
pprint(len(paths))