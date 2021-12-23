import sys
sys.path.append("..")
from common import *

dice = 1
count = 0
def throw_dice():
    global dice
    global count
    rolls = []
    for i in range(3):
        rolls.append(dice)
        dice += 1
        if dice == 101: dice = 1
        count += 1
    return rolls

players = [6,1]
scores = [0,0]

i = 0
done = False
while not done:
    for p in range(len(players)):
        n = sum(throw_dice())
        print("pos:",players[p])
        players[p] = (players[p] + n) % 10
        if players[p] == 0: players[p] = 10
        scores[p] += players[p]
        if scores[p] >= 1000:
            done = True
            break
    print(scores)

print(min(scores)*count)