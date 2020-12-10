with open("day3/input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

mat = [[c for c in l] for l in lines]

right = 3
down  = 1
width = len(mat[0])

posR   = 0
posC   = 0
nTrees = 0
for i in range(len(mat)-1):
    posR = (posR + down)
    posC = (posC + right) % width

    if mat[posR][posC] == "#":
        nTrees+=1

print(nTrees)