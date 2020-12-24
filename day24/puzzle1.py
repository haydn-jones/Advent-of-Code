import numpy as np
from collections import defaultdict

dirs = ["e", "se", "sw", "w", "nw", "ne"]

mapDirs = {
    "e"  : np.array([ 1,  0]),
    "se" : np.array([ 0.5, -1]), 
    "sw" : np.array([- 0.5, -1]), 
    "w"  : np.array([-1,  0]), 
    "nw" : np.array([- 0.5,  1]), 
    "ne" : np.array([  0.5,  1]),
}


def getPos(string):
    splits = []
    while len(string) > 0:
        two = string[:2]
        if two in dirs:
            splits.append(two)
            string = string[2:]
        else:
            splits.append(string[0])
            string = string[1:]

    pos = np.array([0.0, 0])
    for dir_ in splits:
        pos += mapDirs[dir_]

    return tuple(pos)

tiles = defaultdict(int)
with open("day24/input.txt", 'r') as f:
    data = f.read().strip().split("\n")
    for i in data:
        tiles[getPos(i)] += 1

black = 0
white = 0
for v in tiles.values():
    if v % 2 == 0:
        white += 1
    else:
        black += 1