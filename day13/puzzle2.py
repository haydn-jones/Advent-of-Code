with open("day13/input.txt", "r") as f:
    vals = [line.strip()for line in f.readlines()][1].split(",")
    inds = [i for i, j in enumerate(vals) if j != 'x']
    vals = [int(v) for v in vals if v!="x"]

met  = 0
time = 0
step = 1
while met != len(vals):
    time += step

    if (time + inds[met]) % vals[met] == 0:
        step = step * vals[met]
        met += 1