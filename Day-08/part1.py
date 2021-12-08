import sys
sys.path.append("..")
from common import *

def parse(d):
    return tuple([p.strip().split(" ") for p in d.strip().split("|")])

data = fnl(parse)

print(data)

ns = [2,3,4,7]

count = 0
for rec in data:
    for output in rec[1]:
        l = len(output) 
        if l in ns:
            count += 1

print(count)