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

oxy = np.array(mat)
co2 = np.array(mat)

col = 0
while oxy.shape[0] != 1:
    most = int(oxy[:, col].sum() >= (oxy.shape[0]/2))
    oxy  = oxy[oxy[:, col] == most, :]
    col += 1

col = 0
while co2.shape[0] != 1:
    most = int(co2[:, col].sum() < (co2.shape[0]/2))
    co2  = co2[co2[:, col] == most, :]
    col += 1

oxy = "".join([str(x) for x in np.squeeze(oxy)])
co2 = "".join([str(x) for x in np.squeeze(co2)])
print(int(oxy, 2) * int(co2, 2))