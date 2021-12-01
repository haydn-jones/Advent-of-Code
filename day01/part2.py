import numpy as np

with open("input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    data = [int(x) for x in data if x != ""]

count = 0
for i in range(len(data)):
    A = sum(data[i:i+3])
    B = sum(data[i+1:i+4])
    if B > A:
        count +=1 
print(count)
