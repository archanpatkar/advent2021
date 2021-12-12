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

def findpath(start,end,g,path=[],twice=""):
    if(start == end): return [(*path,start)]
    paths=[]
    if(len(twice) == 0):
        double = [n for n in g[start] if n.islower() and n != "start" and n != "end"]
        for d in double:
            paths.extend(list(filter(lambda p: len(p) > 0, findpath(start,end,caves,path,d))))
    for n in g[start]:
        curr = (*path,start)
        times = freq(path)
        if (not n in path) or (not n.islower()) or (n == twice and times[n] < 2):
            paths.extend(list(filter(lambda p: len(p) > 0, findpath(n,end,caves,curr,twice))))
    return paths    

paths = set(findpath("start","end",caves))
# pprint(paths)
pprint(len(paths))
