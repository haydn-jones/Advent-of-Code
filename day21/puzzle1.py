from collections import defaultdict

with open("day21/input.txt", "r") as f:
    data = f.read().strip().split("\n")

lines = []
for line in data:
    ing, allg = line.split("(")
    ing = ing.strip().split(" ")
    allg = allg[9:-1].split(", ")
    lines.append([ing, allg])

aCount = defaultdict(lambda: [0, defaultdict(int)])
for ingredients, allergens in lines:
    for allg in allergens:
        aCount[allg][0] += 1

        for ing in ingredients:
            aCount[allg][1][ing] += 1


found = set()
for allg, counts in aCount.items():
    max_ = 0
    max_ing = None
    for ing, count in counts[1].items():
        if ing in found:
            continue
        if count > max_:
            max_ = count
            max_ing = ing
    
    found.add(max_ing)

count = 0
for line in lines:
    ingredients = line[0]
    for ing in ingredients:
        if ing in found:
            continue
        count += 1