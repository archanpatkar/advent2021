import sys
sys.path.append("..")
from common import *

def parse(d):
    return [int(n) for n in d.strip().split(",")]

data = fnl(parse)[0]
school = data
print(data)

days = 256
rate = 7
track = [0 for i in range(rate+2)]

for fish in range(len(school)):
    track[school[fish]] += 1
    
pprint(track)

for day in range(days):
    day0 = track[0]
    track = track[1:]
    track.append(0)
    if(day0 >= 1):
        track[8] += day0
        track[6] += day0

print(sum(track))