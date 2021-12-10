import sys
sys.path.append("..")
from common import *

def parse(d):
    return d

data = fnl(parse)

start = ["(","<","{","["]
end = {
    "(":")",
    "<":">",
    "{":"}",
    "[":"]",
}

def iscorrupted(s):
    if s[0] in start:
        curr = s[0]
        s = s[1:]
        out = False
        while len(s) > 0 and s[0] in start:
            out,s = iscorrupted(s)
            if out and len(s) > 1:
                return (True,s)
        if len(s) == 0: return (False,"")
        if s[0] != end[curr] and len(s) > 1:
            return (True,s)
        return (False,s[1:])
    return (False,s)

def _ac(s,completed=[]):
    if s[0] in start:
        curr = s[0]
        s = s[1:]
        while len(s) > 0 and s[0] in start:
            s = _ac(s,completed)
        if len(s) == 0: 
            completed.append(end[curr])
            return ""
        elif s[0] == end[curr]: return s[1:]
    return s

def autocomplete(s,completed=[]):
    while len(s) > 0:
        s = _ac(s,completed)
    return completed

points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}

points2 = {
    ")":1,
    "]":2,
    "}":3,
    ">":4,
}

incomp = [data[i] for i in [ind for ind,o in enumerate([iscorrupted(l) for l in data]) if not o[0]]]
scores = [reduce(lambda acc,v: acc*5 + points2[v],autocomplete(line,[]),0) for line in incomp]
scores.sort()
print(scores[len(scores)//2])