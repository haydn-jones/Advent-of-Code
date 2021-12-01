import numpy as np

with open("input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    data = [int(x) for x in data if x != ""]

count = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        count += 1
print(count)
