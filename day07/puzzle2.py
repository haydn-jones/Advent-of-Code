import string
from collections import defaultdict

data = []

with open("day7/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

rules = {}
counts = defaultdict(lambda: defaultdict(int))
exclude = set(string.punctuation)
for line in data:
    color = line.split(" contain ")[0][:-1]
    color_rule =  line.split(" contain ")[1].split(", ")

    out = []
    for c in color_rule:
        c = ''.join(ch for ch in c if ch not in exclude) 
        if c == "no other bags":
            out.append(c)
        else:
            if c[0] == "1":
                out.append(c[2:])
                counts[color][c[2:]] = 1
            else:
                counts[color][c[2:-1]] = int(c[0])
                out.append(c[2:-1])

    rules[color] = out

def countColor(color):
    print(f"Checking color: {color} | Contains: {counts[color]}")
    if "no other bags" in rules[color]:
        return 0
    
    c = 0
    for k, v in counts[color].items():
        c += v * (countColor(k) + 1)

    return c

print(countColor("shiny gold bag"))