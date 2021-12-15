import sys
from threading import currentThread
sys.path.append("..")
from common import *
from queue import PriorityQueue

def parse(d):
    return [int(n) for n in d]

data = fnl(parse)

final = []
for i in range(5):
    n = []
    for r in data:
        nr = []
        for j in range(5):
            nr.extend(map(lambda n: (n+i+j) if (n+i+j) <= 9 else ((n+i+j)%9),r))
        n.append(nr)
    final.extend(n)

data = final

adj = lambda x,y: [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
graph = defaultdict(lambda: [])
risk_map = defaultdict(int)
for y in range(len(data)):
    for x in range(len(data[0])):
        risk_map[(x,y)] = data[y][x]
        graph[(x,y)] = adj(x,y)

for n in graph: graph[n] = [n for n in graph[n] if n in risk_map]

def manhdis(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

start = (0,0)
end = (len(data[0])-1,len(data)-1)

queue = PriorityQueue()
queue.put((0,start))
distance = defaultdict(lambda: -1)
distance[start] = 0

while not queue.empty():
    priority,current = queue.get()
    if current[0] == end: break
    for next in graph[current]:
        cost = distance[current] + risk_map[next]
        if (not next in distance) or cost < distance[next]:
            distance[next] = cost
            priority = cost + manhdis(next,end)
            queue.put((priority,next))
print(distance[end])