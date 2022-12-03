import sys
sys.path.append(".")
from snippets import read_strip, groupify

lines = read_strip(f"{sys.path[0]}/input.txt")

lines = [
    (string[:len(string)//2], string[len(string)//2:])
    for string in lines
]

lines = [(set(a),set(b)) for a, b in lines]
lines = [a.intersection(b) for a, b in lines]

sum_ = 0
for line in lines:
    char = list(line)[0]
    if char.islower():
        sum_ += 1 + ord(char) - 97
    else:
        sum_ += 1 + ord(char.lower()) - 97 + 26