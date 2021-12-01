import sys
sys.path.append("..")
from common import *

def parse(d):
    return int(d)

data = fnl(parse)

# print(data)

total = 0
last = 0
for i in range(1,len(data)):
    if data[last] < data[i]:
        total += 1
    last = i
print(total)