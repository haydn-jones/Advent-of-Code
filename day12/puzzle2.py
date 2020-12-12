import numpy as np

with open("day12/input.txt", "r") as f:
    data = [line.strip()for line in f.readlines()]
    data = [(a[0], int(a[1:])) for a in data]

dirs = {
    "N": np.array([0,  1]),
    "S": np.array([0, -1]),
    "E": np.array([1,  0]),
    "W": np.array([-1, 0]),
}

shipPos  = np.array([0, 0])
wayPoint = np.array([10, 1])
tmp = np.array(wayPoint)

for line in data:
    if line[0] == "F":
        shipPos += line[1] * wayPoint
        continue

    if line[0] in dirs.keys():
        wayPoint += line[1] * dirs[line[0]]
        continue
        
    if line[0] == "L":
        angle = np.radians(line[1])
    else:
        angle = np.radians(line[0] == "L" * 360 - line[1])

    tmp[0] = round(wayPoint[0] * np.cos(angle) - wayPoint[1] * np.sin(angle))
    tmp[1] = round(wayPoint[0] * np.sin(angle) + wayPoint[1] * np.cos(angle))

    wayPoint = np.copy(tmp)