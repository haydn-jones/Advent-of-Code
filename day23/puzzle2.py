labels = [4, 1, 8, 9, 7, 6, 2, 3, 5]
labels.extend(range(max(labels)+1, 1_000_000+1))
n = len(labels)

cups = {}
for i, label in enumerate(labels):
    cups[label] = labels[(i+1)%len(labels)]
cur = labels[0]

for i in range(10000000):
    pick = [cups[cur], cups[cups[cur]], cups[cups[cups[cur]]]]

    cups[cur] = cups[cups[cups[cups[cur]]]]

    dest = cur-1 if cur != 1 else n
    while dest in pick:
        dest = dest-1 if (dest-1) != 0 else n
    
    cups[pick[-1]] = cups[dest]
    cups[dest] = pick[0]

    cur = cups[cur]

print(cups[1] * cups[cups[1]])