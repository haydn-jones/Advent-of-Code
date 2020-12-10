with open("day1/input.txt", "r") as f:
    data = [int(line) for line in f.readlines()]

for i1 in range(len(data)):
    for i2 in range(i1+1, len(data)):
        for i3 in range(i2+1, len(data)):
            if (data[i1] + data[i2] + data[i3]) == 2020:
                print(data[i1] * data[i2] * data[i3])
