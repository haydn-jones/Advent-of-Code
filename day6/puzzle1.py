data = []
with open("day6/input.txt", "r") as f:
    group = []
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            data.append(group)
            group = []
            continue

        group.append(line.strip())

    data.append(group)

count = 0
for group in data:
    ans = {}
    for person in group:
        for q in person:
            ans[q] = True
    
    count = count + len(ans.keys())

print(count)