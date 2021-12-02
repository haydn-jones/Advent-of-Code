import numpy as np

with open("input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    #data = [int(x) for x in data if x != ""]
    data = [x for x in data if x != ""]

horiz = 0
verti = 0

for line in data:
    dir, amnt = line.split(" ")
    amnt = int(amnt)
    if dir == "forward":
        horiz += amnt
    elif dir == "down":
        verti += amnt 
    elif dir == "up":
        verti -= amnt 

print(horiz * verti)