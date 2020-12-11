import numpy as np

with open("day11/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

data = np.array([[c for c in row] for row in data])

def run(inp):
    next_ = np.copy(inp)
    for r in range(inp.shape[0]):
        for c in range(inp.shape[1]):
            if inp[r, c] == ".":
                continue
                
            lMin = max(0, r-1)
            lMax = min(inp.shape[0], r+2)
            uMin = max(0, c-1)
            uMax = min(inp.shape[1], c+2)

            nOcc = (inp[lMin:lMax, uMin:uMax] == "#").sum()

            if inp[r, c] == "#":
                nOcc -= 1

            if nOcc >= 4:
                next_[r, c] = "L"
                continue
        
            if inp[r, c] == "L" and nOcc == 0:
                next_[r, c] = "#"

    return next_

prev = np.copy(data)
while True:
    next_ = run(prev)

    if np.array_equal(prev, next_):
        break
    else:
        prev = np.copy(next_)