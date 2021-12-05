from collections import defaultdict

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    data = [x for x in data if x != ""]

    clean = []
    for line in data:
        l, r = line.split(" -> ")
        a,b  = l.split(",")
        c,d  = r.split(",")
        clean.append([(int(a), int(b)), (int(c), int(d))])

pos = defaultdict(int)

for line in clean:
    x1, y1 = line[0]
    x2, y2 = line[1]
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)

    if x1 != x2 and y1 != y2:
        continue

    for c in range(minx, maxx+1):
        for r in range(miny, maxy+1):
            pos[(c, r)] += 1

print(sum(map(lambda x: x > 1, pos.values())))