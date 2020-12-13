with open("day13/input.txt", "r") as f:
    data = [line.strip()for line in f.readlines()]
    num = int(data[0])
    vals = data[1].split(",")
    vals = [val for val in vals if val != "x"]

min_time = float("inf")
min_id   = float("inf")
for bus in vals:
    time = 0
    while time < num:
        time += int(bus)
    if time < min_time:
        min_time = time
        min_id = bus
print((min_time - num)*int(min_id))