with open("day10/input.txt", "r") as f:
    data = [int(line.strip()) for line in f.readlines()]


data = sorted(data)

prev = 0
three = 1
one= 0
for adapt in data:
    if abs(prev - adapt) == 1:
        prev = adapt
        one+=1
    elif abs(prev - adapt) == 3:
        prev = adapt
        three+=1
    elif abs(prev - adapt) <= 3:
        prev = adapt
    else:
        break