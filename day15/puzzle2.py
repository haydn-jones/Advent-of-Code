with open("day15/input.txt", "r") as f:
    data = [int(i) for i in f.readline().split(",")]

spoken = {}

turn = 1
for speak in data:
    spoken[speak] = turn
    turn += 1

last_spoken = data[-1]
while turn <= 30000000:
    if last_spoken not in spoken.keys():
        speak = 0
    else:
        speak = turn-1 - spoken[last_spoken]

    spoken[last_spoken] = turn-1
    last_spoken = speak
    turn += 1
