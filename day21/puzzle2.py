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

found = {}
for allg, counts in aCount.items():
    cnts = counts[1]
    max_ = max(cnts.values())
    max_ings = [k for k, v in cnts.items() if v == max_]
    found[allg] = max_ings

true = {}
while len(found) > 0:
    for alg, ings in found.items():
        if len(ings) == 1:
            true[alg] = ings[0]
            break
    else:

    del found[alg]

    for k, v in found.items():
        if ings[0] in v:
            found[k].remove(ings[0])

true = sorted(true.items(), key=lambda item: item[0])
true = [t[1] for t in true]
print(f"'{','.join(true)}'")