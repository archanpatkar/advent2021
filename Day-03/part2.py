import sys
sys.path.append("..")
from common import *

def parse(d):
    return d

data = fnl(parse)

# print(data)

def most(data):
    total = [{"1":0, "0":0} for b in data[0]]
    for r in data:
        for i in range(len(r)):
            total[i][r[i]] += 1
    return total

i = 0
ogr = [*data]
while len(ogr) != 1:
    total = most(ogr)
    highest = ""    
    if(total[i]["0"] > total[i]["1"]): highest = "0"
    else: highest = "1"
    ogr = [n for n in ogr if n[i] == highest]
    i += 1

j = 0
co2 = [*data]
while len(co2) != 1:
    total = most(co2)
    lowest = ""    
    if(total[j]["0"] > total[j]["1"]): lowest = "1"
    else: lowest = "0"
    co2 = [n for n in co2 if n[j] == lowest]
    j += 1

print("oxygen generator rating:", ogr[0])
print("CO2 scrubber rating:", co2[0])
print(int(ogr[0],2) * int(co2[0],2))