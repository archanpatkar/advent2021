import sys
sys.path.append("..")
from common import *

def parse(d):
    return d

data = fnl(parse)

# print(data)

total = [{"1":0, "0":0}  for b in data[0]]

for r in data:
    for i in range(len(r)):
        total[i][r[i]] += 1

# print(total)

gamma = ""
epsilon = ""
for b in total:
    if(b["1"] > b["0"]):
        gamma +=  "1"
        epsilon +=  "0"
    else: 
        gamma +=  "0"
        epsilon +=  "1"

print("gamma:",gamma)
print("epsilon:",epsilon)
print(int(gamma,2) * int(epsilon,2))