import sys
sys.path.append("..")
from common import *

def parse(d):
    return [int(n) for n in d]

data = fnl(parse)

pprint(data)

adj = lambda x,y: [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
graph = defaultdict(lambda: [])
risk_map = defaultdict(int)
for y in range(len(data)):
    for x in range(len(data[0])):
        risk_map[(x,y)] = data[y][x]
        graph[(x,y)] = adj(x,y)

for n in graph: graph[n] = [n for n in graph[n] if n in risk_map]

# pprint(risk_map)
# pprint(graph)

def manhdis(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

start = (0,0)
end = (len(data[0])-1,len(data)-1)

distance = defaultdict(lambda: -1)
distance[start] = 0
# path = []
queue = [(0,start)]

i = 0
while len(queue) > 0:
    cost,curr = queue.pop(0)
    print("i:",i)
    for next in graph[curr]:
        ncost = cost + risk_map[next]
        if not next in distance or distance[next] > ncost:
            distance[next] = ncost
            # path.append(next)
            queue.append((ncost,next))
    if(end in distance): break
    queue.sort(key=lambda t: t[0])
    i += 1

print(distance[end])


