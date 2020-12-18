import numpy as np

with open("day18/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]
    data = [l.replace(" ", "") for l in data]
    data = [[c for  c in l] for l in data]

def evaluate(l):
    if len(l) == 1:
        return int(l[0])
    tStack = [int(v) for v in l if v not in ["*", "+"]]
    ops   = [v for v in l if v in ["*", "+"]]
    for op in ops:
        a = tStack.pop(0)
        b = tStack.pop(0)
        if op == "+":
            tStack.insert(0, a+b)
        else:
            tStack.insert(0, a*b)
    
    return tStack[0]

results = []
for line in data:
    stack = []
    for c in line:
        if c == "(":
            stack.append(None)
        elif c == ")":
            fInd = len(stack) - stack[::-1].index(None) - 1
            toEval = stack[fInd+1:]
            
            stack  = stack[:fInd]
            stack.append(evaluate(toEval))
        else:
            stack.append(c)

    results.append(evaluate(stack))