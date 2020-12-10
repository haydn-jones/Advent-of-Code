from collections import defaultdict 

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
    ans = d = defaultdict(list) 
    for person in group:
        for q in person:
            ans[q].append(True)

    for k, v in ans.items():
        if len(v) == len(group):
            count += 1
    
print(count)