import sys
sys.path.append("..")
from common import *

def parse(d):
    d = d.split("\n")
    points = []
    i = 0
    for p in d:
        if len(p) == 0: break
        points.append(tuple(map(int,p.split(","))))
        i += 1
    folds = []
    for j in range(i+1,len(d)):
        j = d[j]
        j = j.split(" ")[2].split("=")
        j[1] = int(j[1])
        folds.append(tuple(j))
    return (points,folds)

points,folds = aoci(parse)

paper = {}
for p in points:
    if not(p in paper):
        paper[p] = 0
    paper[p] += 1

xmax = max([p[0] for p in points])
ymax = max([p[1] for p in points])
# pprint(paper)
# print("xmax:",xmax)
# print("ymax:",ymax)

for fold in folds:
    if fold[0] == "x":
        np = {}
        for p in paper:
            if p[0] > fold[1]: 
                np[(fold[1]-(p[0]-fold[1]),p[1])] = 1
            else: np[p] = paper[p]
        paper = np
    elif fold[0] == "y":
        np = {}
        for p in paper:
            if p[1] > fold[1]: 
                np[(p[0],fold[1]-(p[1]-fold[1]))] = 1
            else: np[p] = paper[p]
        paper = np
    xmax = []
    ymax = []
    for p in paper:
        xmax.append(p[0])
        ymax.append(p[1])
    xmax = max(xmax)
    ymax = max(ymax)

output = ""
for y in range(ymax+1):
    curr = ""
    for x in range(xmax+1):
        if (x,y) in paper: 
            curr += "*"
        else: curr += " "
    output += curr + "\n"

print(output)