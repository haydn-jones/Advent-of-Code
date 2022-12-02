import sys
sys.path.append(".")
from snippets import read_strip, groupify

lines = read_strip(f"{sys.path[0]}/input.txt")


scores = {
    'X': 1, # R
    'Y': 2, # P
    'Z': 3, # S
}

res = {
    'w': 6,
    'd': 3,
    'l': 0,
}

total = 0
for game in lines:
    y, m = game.split(" ")

    if m == 'X':
        total += res['l']
        if y == "A":
            total += scores['Z']
        if y == "B":
            total += scores['X']
        if y == "C":
            total += scores['Y']
    elif m == 'Y':
        total += res['d']
        if y == "A":
            total += scores['X']
        if y == "B":
            total += scores['Y']
        if y == "C":
            total += scores['Z']
    elif m == 'Z':
        total += res['w']
        if y == "A":
            total += scores['Y']
        if y == "B":
            total += scores['Z']
        if y == "C":
            total += scores['X']

print(total)
