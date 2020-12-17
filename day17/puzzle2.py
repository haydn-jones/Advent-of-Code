import numpy as np
from copy import deepcopy

with open("day17/input.txt", "r") as f:
    data = [[c for c in l.strip()] for l in f.readlines()]
    data = np.array(data)

space = {}
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        if data[y, x] == "#":
            space[(x, y, 0, 0)] = data[y, x]

for _ in range(6):
    next_gen = {}
    mins = np.minimum.reduce(list(space.keys())) - 1
    maxs = np.maximum.reduce(list(space.keys())) + 1
    for x in range(mins[0], maxs[0]+1):
        for y in range(mins[1], maxs[1]+1):
            for z in range(mins[2], maxs[2]+1):
                for w in range(mins[3], maxs[3]+1):
                    active = 0
                    for i in range(x-1, x+2):
                        for j in range(y-1, y+2):
                            for k in range(z-1, z+2):
                                for l in range(w-1, w+2):
                                    if (i, j, k, l) not in space:
                                        continue

                                    if space[(i, j, k, l)] == "#":
                                        active += 1
                    
                    if (x, y, z, w) in space.keys():
                        active -= space[(x, y, z, w)] == "#"
                        state = space[(x, y, z, w)]
                    else:
                        state = "."
                    
                    if state == "#" and active in [2, 3]:
                        next_gen[(x, y, z, w)] = "#"
                    elif state == "." and active == 3:
                        next_gen[(x, y, z, w)] = "#"
    
    space = next_gen

print(sum([1 for i in next_gen.values() if i == "#"]))