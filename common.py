from pprint import pprint
from functools import *
from collections import *
from math import *
from itertools import *
from graphviz import Graph, Digraph
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import seaborn as sns; sns.set_theme()

def scatter3d(x,y,z,name,xl="X",yl="Y",zl="Z"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.set_zlabel(zl)
    ax.scatter3D(x,y,z)
    plt.title(name)
    plt.savefig('{}.png'.format(name))

def barchart(c,d,name,xl="Sections",yl="Freq"):
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid(True)
    plt.bar(c,d)
    plt.title(name)
    plt.savefig('{}.png'.format(name))

def scatterplot(x,y,name,xl="X",yl="Y"):
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid(True)
    plt.scatter(x,y)
    plt.title(name)
    plt.savefig('{}.png'.format(name))

def piechart(x,name,labels,des="%d"):
    plt.grid(True)
    plt.pie(x,labels=labels,autopct=des)
    plt.title(name)
    plt.savefig('{}.png'.format(name))

def p(str):
    pprint(str,indent=4)

def kvd(data,sep=" ",s=":"):
    kv = data.strip().split(sep);
    p = {}
    for e in kv:
        temp = e.split(s)
        p[temp[0]] = temp[1]
    return p

def kvl(data,sep=" ",s=":"):
    kv = data.strip().split(sep);
    p = []
    for e in kv:
        temp = e.split(s)
        p.append((temp[0],temp[1]))
    return p

def lval(data,sep=","):
    return data.split(sep);

def periodic(data,pd=lambda x:not len(x),sep="\n",app=" "):
    lines = data.split(sep);
    u = []
    buff = ""
    for l in lines:
        if pd(l):
            u.append(buff)
            buff = ""
        else:
            buff += "{}{}".format(app,l.strip())
    u.append(buff)
    return u

def freq(str):
    l = {}
    for c in str: 
        if c in l: l[c] += 1
        else: l[c] = 1
    return l

point = namedtuple("Point2D",["x", "y"]);

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
LUD = (-1,-1)
RUD = (1,-1)
LLD = (-1,1)
RLD = (1,1)

n4l = [
            UP,  
    LEFT,          RIGHT, 
            DOWN  
]

n8l = [
    (-1,-1), UP,  (1,-1), 
    LEFT,         RIGHT, 
    (-1,1), DOWN, (1,1)
]

ng = lambda ns: lambda p: tuple((point(p.x+d[0],p.y+d[1]) for d in ns))
n4 = ng(n4l)
n8 = ng(n8l)

def drawgrid(points,xs,ys,pc="*",em=".",jo="\n"):
    strmap = []
    for y in range(ys):
        cr = []
        for x in range(xs):
            if (x,y) in points:
                cr.append(pc)
            else: cr.append(em)
        strmap.append(cr)
    return strmap.join(jo)

def eucdis(p1,p2):
    return sqrt(((p2.x-p1.x) ** 2) + ((p2.y-p1.y) ** 2))

def chebdis(p1,p2):
    return max(abs(p2.x-p1.x),abs(p2.y-p1.y))

def manhdis(p1,p2):
    return abs(p1.x-p2.x) + abs(p1.y-p2.y)

def a(list,index):
    if index < len(list): return list[index]
    print("beyond {} list boundary!".format(index))

def m(list,index):
    return list[index % len(index)]

def add(list):
    return reduce(lambda acc,v: acc+v,list,0)

def mult(list):
    return reduce(lambda acc,v: acc*v,list,1)

def ew(str,e):
    return str.endswith(e)

def sw(str,e):
    return str.startswith(e)

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

nums = ["0","1","2","3","4","5","6","7","8","9"]

def ks(dict):
    k = list(dict.keys())
    if " " in k: return len(k)-1;
    return len(k)

def alpha(str,cutoff="z",start="a"):
    n = ord(str)
    return (n >= ord(start) and n <= ord(cutoff)) or (n >= ord(start.capitalize()) and n <= ord(cutoff.capitalize()))

def minl(l,n):
    return len(l) >= n

def maxl(l,n):
    return len(l) <= n

def el(l,n):
    return len(l) == n

def bi(v,s,e):
    return v >= s and v <= e;

def be(v,s,e):
    return v > s and v < e;

def bf(v,s,e):
    return v >= s and v < e;

def bs(v,s,e):
    return v > s and v <= e;

def checkeg(ns,xlen,ylen,ch=bf):
    print(ns)
    return tuple(filter(lambda p: ch(p.x,0,xlen) and ch(p.y,0,ylen), ns))

def forall(l,f):
    return reduce(lambda acc,v: acc and f(v),l,True)

def exists(l,f):
    return reduce(lambda acc,v: acc or f(v),l,False)

def intl(l,sep=","):
    if(isinstance(l,str)):
        return [int(v) for v in str.split(sep)]
    return [int(v) for v in l]

def flol(l,sep=","):
    if(isinstance(l,str)):
        return [float(v) for v in str.split(sep)]
    return [float(v) for v in l]

iden = lambda x: x

def grid(data,sep=""):
    return list(map(lambda l: l.split(sep),data.split("\n")));

def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - (b // a) * y, y) 
  
# modular inverse driver function 
def modinv(a, m): 
    g, x, y = extended_euclidean(a, m) 
    return x % m 

# wip
# assume l[n][1] is mod
def crt(l):
    ms = [m[1] for m in l]
    k = len(ms)
    N = mult(ms)
    y = [N/m for m in ms]
    z = [modinv(y[i],ms[i]) for i in range(k)]
    x = [l[i][0]*y[i]*z[i] for i in range(k)]
    return (add(x)%N,N)

def unionfind(*lists):
    ss = enumerate(map(lambda l: set(l),lists))
    ops = map(lambda p: set(map(lambda e: (e,p[0]),p[1])), ss)
    return reduce(lambda acc,v: acc.union(v),ops,set())
    
def bfs(graph,start):
    visited = {start:0}
    parents = {start:-1}
    q = [start]
    while len(q) != 0:
        curr = q.pop(0)
        p(curr)
        for adj in graph.get(curr):
            if not(adj in visited):
                q.append(adj);
                visited[adj] = visited[curr] + 1
                parents[adj] = curr
    return (visited,parents)

def dfs(graph,start,cb=lambda p,c:(p,c),visited={}):
    visited[start] = 1
    for adj in graph[start]:
        if not visited.get(adj):
            cb(start,adj)
            dfs(graph,adj,cb,visited)

# shortest path bfs
def spbfs(graph,start,end):
    visited, parents = bfs(graph,start)
    if(end in visited):
        path = []
        curr = end
        while curr != start:
            path.append(curr)
            curr = parents[curr]
        path.append(start)
        path.reverse()
        return path
    print("No path!")

def toposort(graph):
    visited = {}
    ts = []
    for n in graph:
        if not(n in visited):
            dfs(graph,n,lambda p,c:ts.append((p,c)),visited)
    return ts

def drawGraph(path,graph,process=iden,format="svg"):
    g = Graph(format=format,name=path)
    for n in graph:
        for e in graph[n]:
            g.edge(process(n),process(e))
    g.render(cleanup=True)

def drawDGraph(path,graph,process=iden,format="svg",**attrs):
    g = Digraph(format=format,name=path,filename=path)
    if attrs:
        g.attr(**attrs)
    for n in graph:
        for e in graph[n]:
            t = process(e)
            if isinstance(t,tuple):
                g.edge(process(n),t[1],label=str(t[0]))
            else:
                g.edge(process(n),t)
    g.render(cleanup=True)

def comb(base,d,start,process=lambda x:"".join(x)):
    done = [start]
    q = []
    for k in d[start]:
        var = list(base)
        var[start] = k
        q.append(var)
    for o in d:
        if not o in done:
            next = []
            while len(q) != 0:
                e = q.pop(0)
                for k in d[o]:
                    var = list(e)
                    var[o] = k
                    next.append(process(var))
            q = next
            done.append(o)
    return q

def all_poss_var(l,marker,values):
    d = {}
    for e in range(len(l)):
        if l[e] == marker: d[e] = values
    return comb(list(l),d,list(d.keys())[0])
    
def aoci(func=iden):
    return func(open("input.txt","r").read());

def fnl(func=iden):
    return [func(l) for l in aoci(lambda data: data.split("\n"))]