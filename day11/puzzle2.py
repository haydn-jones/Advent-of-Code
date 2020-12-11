import numpy as np

with open("day11/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

data = np.array([[c for c in row] for row in data])

def occupied(sl):
    if sl.size == 0:
        return 0

    return int(sl[(sl != ".").argmax()] == "#")

def run(inp):
    next_ = np.copy(inp)
    for r in range(inp.shape[0]):
        for c in range(inp.shape[1]):
            if inp[r, c] == ".":
                continue
            
            nOcc = 0
            nOcc += occupied(inp[r, c+1:])
            nOcc += occupied(inp[r, :c][::-1])
            nOcc += occupied(inp[:r, c][::-1])
            nOcc += occupied(inp[r+1:, c])
                
            diag1 = []
            tR = r+1
            tC = c+1
            while True:
                if tR >= inp.shape[0] or tC >= inp.shape[1]:
                    break
                diag1.append(inp[tR, tC])
                tR+=1
                tC+=1


            diag2 = []
            tR = r-1
            tC = c-1
            while True:
                if tR < 0 or tC < 0:
                    break
                diag2.append(inp[tR, tC])
                tR-=1
                tC-=1

            diag3 = []
            tR = r-1
            tC = c+1
            while True:
                if tR < 0 or tC >= inp.shape[1]:
                    break
                diag3.append(inp[tR, tC])
                tR-=1
                tC+=1

            diag4 = []
            tR = r+1
            tC = c-1
            while  True:
                if tR >= inp.shape[0] or tC < 0:
                    break
                diag4.append(inp[tR, tC])
                tR+=1
                tC-=1

            nOcc += occupied(np.array(diag1))
            nOcc += occupied(np.array(diag2))
            nOcc += occupied(np.array(diag3))
            nOcc += occupied(np.array(diag4))

            # if r == 4 and c == 0:
                # import pdb; pdb.set_trace()

            if nOcc >= 5:
                next_[r, c] = "L"
                continue
            
            if nOcc == 0:
                next_[r, c] = "#"

    return next_

prev = np.copy(data)
while True:
    next_ = run(prev)

    if np.array_equal(prev, next_):
        break
    else:
        prev = np.copy(next_)