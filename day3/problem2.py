import numpy as np

inputs = np.loadtxt('day3/input2.txt', dtype=str, delimiter=",")

paths = {} # (row, col): [visited_by, steps, [steps]]

for wire_num, inp in enumerate(inputs):
    row = 0
    col = 0

    total_dist = 0
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

            total_dist += 1

            if (row, col) not in paths:
                paths[(row, col)] = [(wire_num, total_dist)]
            else:
                value = paths[(row, col)]
                visited_by = [tup[0] for tup in value]

                if wire_num in visited_by:
                    continue
                    
                value.append([wire_num, total_dist])
                paths[(row, col)] = value

ints = [value for value in paths.values() if len(value) == 2]
ints = sorted(ints, key=lambda v: v[0][1] + v[1][1])