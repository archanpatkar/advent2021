import sys
sys.path.append("..")
from common import *

def parse(d):
    if(len(d)> 0):
        temp = d.split(" ")
        return (temp[0],int(temp[1]))
    return ("",0)

data = fnl(parse)

# print(data)

hor = 0
dep = 0
aim = 0
for ins in data:
    if(ins[0] == "up"):
        aim -= ins[1]
    if(ins[0] == "down"):
        aim += ins[1]
    if(ins[0] == "forward"):
        hor += ins[1]
        dep += (aim * ins[1])
    # if(ins[0] == "backward"):
    #     dep += ins[1]

print(hor*dep)