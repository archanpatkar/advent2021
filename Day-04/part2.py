import sys
sys.path.append("..")
from common import *


def parse(d):
    temp = d.strip().split("\n")
    first = tuple([int(n) for n in temp[0].strip().split(",")])
    second = []
    temp2 = []
    print(temp)
    for r in temp[1:]:
        # print(r)
        if(len(r) == 0):
            second.append(tuple(temp2))
            temp2 = []
        else:
            temp2.append(tuple([int(n) for n in r.split(" ") if(len(n) > 0)]))
    second.append(tuple(temp2))
    print(first)
    print(second)
    return (first,second)

data = aoci(parse)

boards = [b for b in data[1] if len(b) > 0]
print("boards")
print(boards)
print("-----------------------------")
pos = {b:{} for b in boards}
winners = []
winners2 = []
winner = None
i = 0
draw = None
found = None
for draw in data[0]:
    print("Draw:",draw)
    for board in boards:
        for l in range(len(board)):
            if draw in board[l]:
                if not pos[board].get((l,board[l].index(draw))):
                    pos[board][(l,board[l].index(draw))] = []
                pos[board][(l,board[l].index(draw))] = draw
    nd = {b:{} for b in pos}
    for b in boards:
        if(not(b in winners2)):
            for i in range(5):
                nd[b][(i,0)] = 0
                nd[b][(0,i)] = 0
            nd[b][(0,0,"C")] = 0
            for k in pos[b]:
                nd[b][(k[0],0)] += 1
                if(k[1] == 0):
                    nd[b][(0,0,"C")] += 1
                else: nd[b][(0,k[1])] += 1
            for s in nd[b]:
                if(nd[b][s] >= 5):
                    found = (b,nd[b],pos[b],draw)
                    winners.append(found)
                    winners2.append(b)
                    break
    if len(winners) == len(boards): 
        break

if(winner == None):
    winner = winners[-1]

pprint(winner,indent=4)

sum = 0
for i in range(5):
    for j in range(5):
        if not((i,j) in winner[2]):
            print(winner[0][i][j])
            sum += winner[0][i][j]
print("output")
print(sum)
print(draw)
print(sum * winner[-1])