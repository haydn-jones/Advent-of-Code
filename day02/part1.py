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

    total += scores[m]
    if y == "A":
        if m == 'Y':
            total +=  res['w']
        elif m == 'Z':
            total +=  res['l']
        else:
            total += res['d']
    elif y == "B":
        if m == 'Z':
            total +=  res['w']
        elif m == 'X':
            total +=  res['l']
        else:
            total += res['d']
    elif y == "C":
        if m == 'X':
            total +=  res['w']
        elif m == 'Y':
            total +=  res['l']
        else:
            total += res['d']
print(total)