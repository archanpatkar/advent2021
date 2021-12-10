import sys
sys.path.append("..")
from common import *

def iscorrupted(d):
    return d

data = fnl(iscorrupted)

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

points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}

print(sum([points[e[1][0]] for e in [iscorrupted(l) for l in data] if e[0]]))