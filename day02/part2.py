with open("input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    data = [x for x in data if x != ""]

horiz = 0
verti = 0
aim   = 0

for line in data:
    dir, amnt = line.split(" ")
    amnt = int(amnt)
    if dir == "forward":
        horiz += amnt
        verti += aim * amnt
    elif dir == "down":
        aim += amnt 
    elif dir == "up":
        aim -= amnt 

print(horiz * verti)