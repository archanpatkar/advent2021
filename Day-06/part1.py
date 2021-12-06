import sys
sys.path.append("..")
from common import *

def parse(d):
    return [int(n) for n in d.strip().split(",")]

data = fnl(parse)[0]
school = data
print(school)

days = 80

for day in range(days):
    for fish in range(len(school)):
        if(school[fish] == 0): 
            school[fish] = 6
            school.append(8)
        else: school[fish] -= 1
    
print(len(school))