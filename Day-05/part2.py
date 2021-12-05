import sys
sys.path.append("..")
from common import *

def parse(d):
    return tuple([tuple([int(p) for p in n.strip().split(",")]) for n in d.strip().split("->")])

data = fnl(parse)

lines = data

points = defaultdict(int)
for seg in lines:
    x1 = seg[0][0]
    y1 = seg[0][1]
    x2 = seg[1][0]
    y2 = seg[1][1]
    if((x1 > x2 and y1 > y2) or (x2 > x1 and y2 > y1)):
        if(x1 > x2): x1, x2 = x2, x1
        if(y1 > y2): y1, y2 = y2, y1
        for i in range(x2-x1+1):
            points[(x1+i,y1+i)] += 1
    elif((x1 > x2 and y2 < y1) or (x1 < x2 and y1 > y2)):
        if(x1 > x2): x1, x2 = x2, x1
        for i in range(x2-x1+1):
            points[(x1+i,y1-i)] += 1
    elif((x1 > x2 and y1 < y2) or (x2 > x1 and y2 < y1)):
        if(x1 < x2): x1, x2 = x2, x1
        if(y1 > y2): y1, y2 = y2, y1  
        for i in range(x1-x2+1):
            points[(x1-i,y1+i)] += 1
    elif(x1 == x2):
        if(y1 > y2): y1, y2 = y2, y1
        for r in range(y1,y2+1):
            points[(x1,r)] += 1
    elif(y1 == y2):
        if(x1 > x2): x1, x2 = x2, x1
        for r in range(x1,x2+1):
            points[(r,y1)] += 1

print(sum([1 for k in points if points[k] >= 2]))