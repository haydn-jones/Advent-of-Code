import numpy as np

with open("day16/input.txt", "r") as f:
    data = f.read().split("\n\n")

    rules  = [l.strip() for l in data[0].split("\n")]
    ticket = [l.strip() for l in data[1].split("\n")][1]
    others = [l.strip() for l in data[2].split("\n")][1:-1]
    others = np.array([[int(v) for v in o.split(",")] for o in others])


ints = []
ruleRanges = {}
for rule in rules:
    name, ranges = rule.split(": ")
    ranges = ranges.split(" or ")

    fullRange = []
    for r in ranges:
        low = int(r.split("-")[0])
        high = int(r.split("-")[1])
        fullRange.extend(list(range(low, high+1)))
        ints.extend(list(range(low, high+1)))
    
    ruleRanges[name] = fullRange

invalid = 0
for i in range(others.shape[0]):
    bools = np.isin(others[i, :], ints)
    if False in bools:
        invalid += np.sum(others[i, :][bools == False])