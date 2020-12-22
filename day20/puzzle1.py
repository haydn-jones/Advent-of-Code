import numpy as np
from collections import defaultdict

with open("day20/input.txt", "r") as f:
    tiles = f.read().split("\n\n")
    tiles = [t.split("\n") for t in tiles][:-1]

#           Left               Right               Top                Bottom
sides = [(slice(None), 0), (slice(None), -1), (0, slice(None)), (-1, slice(None))]

tileDict = {}
for tile in tiles:
    id_  = tile[0]
    id_  = id_.split(" ")[1][:-1]
    fTile = np.array([np.array(list(l)) for l in tile[1:]])

    tileDict[id_] = fTile

matches = defaultdict(list)
for id1, tile1 in tileDict.items():
    for id2, tile2 in tileDict.items():
        if id1 == id2:
            continue
        
        for i1, s1 in enumerate(sides):
            for i2, s2 in enumerate(sides):
                if np.array_equal(tile1[s1[0], s1[1]], tile2[s2[0], s2[1]]):
                    matches[id1].append((i1, id2, i2, False))
                if np.array_equal(tile1[s1[0], s1[1]], tile2[s2[0], s2[1]][::-1]):
                    matches[id1].append((i1, id2, i2, True))

sideLen = int(np.sqrt(len(tileDict)))

arr = np.full((sideLen, sideLen), -1)

prod = 1
for k, v in matches.items():
    if len(v) == 2:
        print(k, v)
        prod *= int(k)