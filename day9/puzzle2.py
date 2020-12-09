with open("day9/input.txt", "r") as f:
    data = [int(line.strip()) for line in f.readlines()]

target = 1504371145

inds = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if target == sum(data[i:j]):
            print(min(data[i:j])+ max(data[i:j]))