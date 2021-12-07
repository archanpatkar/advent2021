import sys
sys.path.append("..")
from common import *

def parse(d):
    return [int(n) for n in d.strip().split(",")]

data = aoci(parse)

print(data)

all = []
for pos in range(len(data)):
    sum = 0
    for crab in data:
       sum += abs(pos-crab)
    all.append(sum)
    
pprint(all)
print(min(all))