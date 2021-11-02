import numpy as np

inputs = np.loadtxt('day3/input1.txt', dtype=str, delimiter=",")

paths = {}

for inp in inputs:
    row = 0
    col = 0

    for path in inp:
        dir_, dist = path[0], int(path[1:])

        for _ in range(dist):
            if dir_ == "U":
                col += 1
            elif dir_ == "D":
                col -= 1
            if dir_ == "L":
                row -= 1
            elif dir_ == "R":
                row += 1

            if (row, col) in paths:
                paths[(row, col)] += 1
            else:
                paths[(row, col)] = 1