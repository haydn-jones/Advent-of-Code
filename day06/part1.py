from collections import defaultdict
import numpy as np

with open("input.txt", "r") as f:
    line = f.readlines()[0]
    data = [int(x) for x in line.strip().split(",")]

fish = data
for day in range(80):
    newfish = []
    for fish in fish:
        fish -= 1

        if fish < 0:
            fish = 6
            newfish.append(8)
        newfish.append(fish)
    fish = newfish

    print(fish)
print(len(fish))