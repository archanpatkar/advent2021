import sys
sys.path.append("..")
from common import *
from functools import lru_cache

#        - 1  
#       | 
# dice -|- 2
#       |
#        - 3

players = (6,1)
scores = [0,0]

rolls = defaultdict(int)

for i in range(1,4):
    for j in range(1,4): 
        for k in range(1,4): rolls[sum((i,j,k))] += 1

addt = lambda t1,t2: (t1[0]+t2[0],t1[1]+t2[1])

@lru_cache(maxsize=None)
def play(pos1,score1,pos2,score2):
    out = []
    for roll,count in rolls.items():
        np = (pos1 + roll) % 10
        if np == 0: np = 10
        ns = score1 + np
        if ns >= 21: out.append((count,0))
        else: out.append(tuple(map(lambda v: v*count,play(pos2,score2,np,ns)))[::-1])
    return reduce(addt,out)

print(max(play(players[0],0,players[1],0)))