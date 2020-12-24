import numpy as np
from collections import defaultdict
from copy import deepcopy
from tqdm import trange

BLACK = False
WHITE = True

dirs = ["e", "se", "sw", "w", "nw", "ne"]

mapDirs = {
    "e"  : np.array([ 1,    0]),
    "se" : np.array([ 0.5, -1]), 
    "sw" : np.array([-0.5, -1]), 
    "w"  : np.array([-1,    0]), 
    "nw" : np.array([-0.5,  1]), 
    "ne" : np.array([ 0.5,  1]),
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
day = {}
for k, v in tiles.items():
    if v % 2 == 0:
        white += 1
    else:
        black += 1
        day[k] = BLACK

print("Black:", black)
print("White:", white)

def countNeighbors(tile, day):
    count = 0
    for dir_ in mapDirs.values():
        if tuple(tile+dir_) in day:
            count += 1

    return count

for i in trange(100):
    newDay = {}

    # Flip black tiles
    for tile in day.keys():
        count = countNeighbors(tile, day)
        if count in [1, 2]:
            newDay[tile] = BLACK
    
    # Find new black tiles
    for tile in day.keys():
        for dir_ in mapDirs.values():
            newPos = tuple(tile+dir_)
            if tuple(tile+dir_) in day: # Already black
                continue

            count = countNeighbors(newPos, day)
            if count == 2:
                newDay[newPos] = BLACK
    
    day = deepcopy(newDay)