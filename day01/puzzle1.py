with open("day1/input.txt", "r") as f:
    data = [int(line) for line in f.readlines()]

for i1 in range(len(data)):
    for i2 in range(i1+1, len(data)):
        if (data[i1] + data[i2]) == 2020:
            print(data[i1] * data[i2])
            exit()