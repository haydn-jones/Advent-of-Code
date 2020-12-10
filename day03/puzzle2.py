with open("day3/input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

mat = [[c for c in l] for l in lines]


def checkSlope(mat, right, down):
    width = len(mat[0])

    posR   = 0
    posC   = 0
    nTrees = 0
    
    posR = down
    posC = right
    while posR < len(mat):
        if mat[posR][posC] == "#":
            nTrees+=1

        posR = posR + down
        posC = (posC + right) % width

    return nTrees

slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

prod = 1
for slope in slopes:
    prod = prod * checkSlope(mat, *slope)

print(prod)