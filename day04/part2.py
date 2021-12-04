import numpy as np

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    nums = [int(x) for x in data[0].split(",") if x != ""]

    i = 2
    boards = []
    curboard = []
    while i < len(data):
        if data[i] == "":
            boards.append(np.array(curboard))
            curboard = []
        else:
            curboard.append([int(x) for x in data[i].split(" ") if x != ""])
        i += 1

boards  = np.stack(boards)
targets = np.zeros_like(boards)

for num in nums:
    targets[boards == num] = 1

    wins = ~((targets.sum(axis=1) == 5).max(axis=-1) | (targets.sum(axis=2) == 5).max(axis=-1))
    if boards.shape[0] == 1 and False in wins:
        break
    boards  = boards[wins]
    targets = targets[wins]

print(((targets == 0) * boards).sum() * num)