import sys
sys.path.append("..")
from common import *
import json

def parse(d):
    return json.loads(d)

data = fnl(parse)

id = 0
def createtree(l,depth=0,right=False):
    global id
    if isinstance(l,int): return l
    if isinstance(l,list):
        node = {}
        node["l"] = createtree(l[0],depth+1)
        node["r"] = createtree(l[1],depth+1,True)
        node["id"] = id
        id += 1
        node["level"] = depth
        return node

nodes = [createtree(n) for n in data]

def _split(tree,leafs=[]):
    global id
    if isinstance(tree,int): return False
    if isinstance(tree["l"],int) and tree["l"] >= 10:
        leafs.append((tree["l"],tree,"l",{ "l":floor(tree["l"]/2), "r":ceil(tree["l"]/2), "level":tree["level"]+1 }))
    elif isinstance(tree["l"],dict): _split(tree["l"],leafs)
    if isinstance(tree["r"],int) and tree["r"] >= 10:
        leafs.append((tree["r"],tree,"r",{ "l":floor(tree["r"]/2), "r":ceil(tree["r"]/2), "level":tree["level"]+1 }))  
    elif isinstance(tree["r"],dict): return _split(tree["r"],leafs)
    return leafs

def split(tree):
    out = _split(tree,[])
    if len(out) > 0:
        n,parent,orient,value = out[0]
        parent[orient] = value
        return True
    return False

def convert(n):
    if isinstance(n,dict): return [convert(n["l"]),convert(n["r"])]
    return n

def allleafs(node,leafs=[]):
    if isinstance(node["l"],int): leafs.append((node["l"],"l",node))
    elif isinstance(node["l"],dict): allleafs(node["l"],leafs)
    if isinstance(node["r"],int): leafs.append((node["r"],"r",node))
    elif isinstance(node["r"],dict): allleafs(node["r"],leafs)
    return leafs

def new_replace(root,curr,orient,parent):
    leafs = allleafs(root,[])
    inds = [l for l in range(len(leafs)) if leafs[l][2] == curr]
    if len(inds) > 0:
        if (inds[0] - 1) >= 0:
            adj = inds[0]-1
            pos = leafs[adj][1]
            value = leafs[inds[0]][0]
            leafs[adj][2][pos] = leafs[adj][2][pos] + value
        if (inds[1] + 1) < len(leafs):
            adj = inds[1]+1
            pos = leafs[adj][1]
            value = leafs[inds[1]][0]
            leafs[adj][2][pos] = leafs[adj][2][pos] + value
        parent[orient] = 0
        return True
    return False

def find_node(tree,level = 4,leafs = []):
    if isinstance(tree,int): return leafs
    if tree["level"] == level-1:
        if isinstance(tree["l"],dict): leafs.append((tree["l"],"l",tree))
        if isinstance(tree["r"],dict): leafs.append((tree["r"],"r",tree))
    find_node(tree["l"],level,leafs)
    find_node(tree["r"],level,leafs)
    return leafs

def explode(node):
    out = find_node(node,level=4,leafs=[])
    if len(out) > 0: 
        curr,orient,parent = out[0]
        return new_replace(node,curr,orient,parent)
    return False

def magnitude(tree):
    if isinstance(tree,int): return tree
    if isinstance(tree,dict):
        return magnitude(tree["l"]) * 3 + magnitude(tree["r"]) * 2

def add(l1,l2):
    return [l1,l2]

nodes = data

prev = nodes[0]
for i in range(1,len(nodes)):
    curr = createtree(add(prev,nodes[i]))
    while True:
        count = 0
        out = explode(curr)
        if out: continue
        out = split(curr)
        if out: continue
        break
    prev = convert(curr)
print(magnitude(createtree(prev)))