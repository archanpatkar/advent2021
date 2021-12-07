import sys
sys.path.append("..")
from common import *

def parse(d):
    return [int(n) for n in d.strip().split(",")]

data = aoci(parse)

print(data)

def calc(n):
    return (n*(n+1))//2

all = []
for pos in range(len(data)):
    sum = 0
    for crab in data:
       sum += calc(abs(pos-crab))
    all.append(sum)
    
pprint(all)
print(min(filter(lambda x: x != 0,all)))