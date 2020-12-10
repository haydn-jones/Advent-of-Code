import string

data = []

with open("day7/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

rules = {}
exclude = set(string.punctuation)
for line in data:
    color = line.split(" contain ")[0]
    color_rule =  line.split(" contain ")[1].split(", ")

    out = []
    for c in color_rule:
        c = ''.join(ch for ch in c if ch not in exclude) 
        if c.isalpha():
            out.append(c)
        else:
            if c[0] == "1":
                out.append(c[2:])
            else:
                out.append(c[2:-1])

    rules[color[:-1]] = out

def checkColor(color):
    if " other bag" in rules[color]:
        return False

    if "shiny gold bag" in rules[color]:
        return True

    for contains in rules[color]:
        if checkColor(contains) == True:
            return True
    
    return False


count = 0
for color in rules.keys():
    if checkColor(color) == True:
        count += 1

print(count)