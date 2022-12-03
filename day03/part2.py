import sys
sys.path.append(".")
from snippets import read_strip, groupify
import numpy as np

lines = read_strip(f"{sys.path[0]}/input.txt")

lines = np.array_split(lines, len(lines)//3)

lines = [(set(a),set(b),set(c)) for a, b, c in lines]
lines = [
    l[0].intersection(l[1]).intersection(l[2])
    for l in lines
]

sum_ = 0
for line in lines:
    char = list(line)[0]
    if char.islower():
        sum_ += 1 + ord(char) - 97
    else:
        sum_ += 1 + ord(char.lower()) - 97 + 26