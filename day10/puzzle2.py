with open("day10/input.txt", "r") as f:
    data = [int(line.strip()) for line in f.readlines()]

data.insert(0, 0)
data = sorted(data)

oneFlips = []
for i in range(1, len(data)-1):
    if abs(data[i-1] - data[i+1]) <= 3:
        oneFlips.append(1)
    else:
        oneFlips.append(0)

i = 0
prod = 1
while i < len(oneFlips):
    if oneFlips[i:i+3] == [1, 1, 1]:
        prod = prod * 7
        i += 3
    elif oneFlips[i:i+2] == [1, 1]:
        prod = prod * 4
        i += 2
    elif oneFlips[i] == 1:
        prod = prod * 2
        i += 1
    else:
        i += 1