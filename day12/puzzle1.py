import numpy as np

with open("day12/input.txt", "r") as f:
    data = [line.strip()for line in f.readlines()]
    data = [(a[0], int(a[1:])) for a in data]

curDirs = ["N", "E", "S", "W"]

dirs = {
    "N": np.array([0,  1]),
    "S": np.array([0, -1]),
    "E": np.array([1,  0]),
    "W": np.array([-1, 0]),
}

pos = np.array([0, 0])

curDir = 1 # east
for line in data:
    if line[0] in dirs.keys():
        pos += line[1] * dirs[line[0]]
    elif line[0] in ("L", "R"):
        sign = -1 if line[0] == "L" else 1
        curDir = (curDir + sign* line[1] // 2) % 4
    else:
        pos += line[1] * dirs[curDirs[curDir]]
