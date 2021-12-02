import sys
sys.path.append("..")
from common import *

def parse(d):
    temp = d.split(" ")
    return (temp[0],int(temp[1]))

data = fnl(parse)

# print(data)

hor = 0
dep = 0
for ins in data:
    if(ins[0] == "up"):
        dep -= ins[1]
    if(ins[0] == "down"):
        dep += ins[1]
    if(ins[0] == "forward"):
        hor += ins[1]
    # if(ins[0] == "backward"):
    #     dep += ins[1]

print(hor*dep)