import sys
sys.path.append("..")
from common import *

def parse(d):
    return tuple([tuple(map(int,e.split("=")[1].split(".."))) for e in d.split(":")[1].split(",")])

data = aoci(parse)

pprint(data)

def reached_target(x,y,target=data):
    if(x >= data[0][0] and
       x <= data[0][1] and 
       y >= data[1][0] and 
       y <= data[1][1]):
        return True
    return False

def crossed(x,y,target=data):
    return True if x > data[0][1] or y < data[1][1] else False
    
initials = []
for x_v in range(200):
    for y_v in range(-200,200):
        if x_v != 0 and y_v != 0:
            initial_x = x_v
            initial_y = y_v
            curr_x_v = x_v
            curr_y_v = y_v
            x = 0
            y = 0
            points = []
            while (not reached_target(x,y)) and ((not crossed(x,y)) or curr_x_v != 0):
                points.append((x,y))
                x += curr_x_v
                y += curr_y_v
                if curr_x_v == 0: curr_x_v = curr_x_v
                if curr_x_v < 0: curr_x_v += 1
                elif curr_x_v > 0: curr_x_v -= 1
                curr_y_v -= 1
            if reached_target(x,y): initials.append(((x,y),(initial_x,initial_y),points))
    

max_y = max([max([cp[1] for cp in p[2]]) for p in initials])
print(max_y)