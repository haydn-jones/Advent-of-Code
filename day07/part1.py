from collections import defaultdict
import numpy as np

fname = "input.txt"
#fname = "ex.txt"
with open(fname, "r") as f:
    line = f.readlines()[0]
    data = [int(x) for x in line.strip().split(",")]

best = 1
best_fuel = np.inf 
for pos in data:
    fuel = 0
    for crab in data:
        fuel += abs(crab - pos)
    if fuel < best_fuel:
        best_fuel = fuel
        best = pos
print(best_fuel)