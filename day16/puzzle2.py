from collections import defaultdict
import numpy as np

with open("day16/input.txt", "r") as f:
    data = f.read().split("\n\n")

    rules  = [l.strip() for l in data[0].split("\n")]
    ticket = np.fromstring(data[1].split("\n")[1], sep=",")
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

valid = []
for i in range(others.shape[0]):
    bools = np.isin(others[i, :], ints)
    if False not in bools:
        valid.append(i)

others = others[valid]

possibilities = defaultdict(list)
for k in ruleRanges.keys():
    for i in range(len(ticket)):
        if False not in np.isin(others[:, i], ruleRanges[k]):
            possibilities[k].append(i)
    
indices = {}
unmatched = list(range(len(ticket)))
while len(unmatched) != 0:
    for k, v in possibilities.items():
        if len(v) == 1:
            found = v[0]
            indices[k] = found
            for k_, v_ in possibilities.items():
                if found in v_:
                    v_.remove(found)
            unmatched.remove(found)

prod = 1
for k, v in indices.items():
    if "departure" not in k:
        continue
    
    prod = prod * ticket[v]