import sys
sys.path.append("..")
from common import *

def parse(d):
    return [int(n) for n in d.strip()]

data = fnl(parse)

print(data)

xlen = len(data[0])
ylen = len(data)

adj = lambda x,y: [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]

points = []
count = 0
for y in range(ylen):
    for x in range(xlen):
        point = data[y][x]
        lcount = 0
        for p in adj(x,y):
            if(
                (p[0] < xlen) and (p[0] >= 0) and
                (p[1] < ylen) and (p[1] >= 0) and 
                (point < data[p[1]][p[0]])
            ): lcount += 1
        if (
            lcount == 4 or 
            (y == 0 and x == 0 and lcount == 2) or 
            (y == ylen-1 and x == xlen-1 and lcount == 2) or 
            (y == 0 and x == xlen-1 and lcount == 2) or 
            (y == ylen-1 and x == 0 and lcount == 2) or 
            (y == 0 and lcount == 3) or 
            (y == ylen-1 and lcount == 3) or 
            (x == 0 and lcount == 3) or 
            (x == xlen-1 and lcount == 3) 
        ):
            points.append((point,(x,y)))
            count += (point + 1)

# pprint(points)
# print(count)

def findbasin(point,visited={}):
    if point in visited: return 0
    x = point[0]
    y = point[1]
    visited[point] = True
    count = 1
    for p in adj(x,y):       
        if(
            (p[0] < xlen) and (p[0] >= 0) and
            (p[1] < ylen) and (p[1] >= 0) 
        ): 
            pval = data[p[1]][p[0]]
            if(pval != 9): count += findbasin(p,visited)
    return count

visited = {}
basins = [findbasin(p[1],visited) for p in points]
basins.sort()
print(mult(basins[-3:]))