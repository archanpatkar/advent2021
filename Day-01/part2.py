import sys
sys.path.append("..")
from common import *

def parse(d):
    return int(d)

data = fnl(parse)

# print(data)

total = 0
lastsum = 0
for i in range(len(data)-2):
    print(data[i:i+3])
    currsum = sum(data[i:i+3])
    print(currsum)
    if (i != 0) and lastsum < currsum:
        total += 1
    lastsum = currsum
print(total)