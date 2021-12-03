import numpy as np

with open("input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    data = [x for x in data if x != ""]

mat = []
for line in data:
    row = []
    for char in line:
        row.append(int(char))
    mat.append(row)

data = np.array(mat)
gamma = []
epsilon = []
for i in range(data.shape[1]):
    if data[:, i].sum() > 500:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)
gamma = int("".join([str(x) for x in gamma]), 2)
epsilon = int("".join([str(x) for x in epsilon]), 2)
print(gamma*epsilon)