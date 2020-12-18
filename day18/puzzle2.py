import numpy as np

with open("day18/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]
    data = [l.replace(" ", "") for l in data]
    data = [[c for  c in l] for l in data]

def evaluate(l):
    if len(l) == 1:
        return int(l[0])

    tStack = [int(v) for v in l if v not in ["*", "+"]]
    ops    = [v for v in l if v in ["*", "+"]]

    if "+" not in ops:
        return np.prod(tStack)
    
    for i, v in enumerate(ops):
        if v == "+":
            res = tStack[i+0] + tStack[i+1]
            tStack[i+0] = 1
            tStack[i+1] = res

    return np.prod(tStack)

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