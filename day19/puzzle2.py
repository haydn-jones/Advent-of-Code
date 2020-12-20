from tqdm import tqdm

with open("day19/example.txt", "r") as f:
    rules, inp = f.read().split("\n\n")
    rules = [l.strip() for l in rules.split("\n")]
    rules = sorted(rules, key=lambda x: int(x.split(": ")[0]))

    inp = [list(l.strip()) for l in inp.split("\n")]

dRules = {}
lrules = []
for rule in rules:
    r, oR = rule.split(": ")
    oR = oR.split(" | ")

    args = []
    for o in oR:
        ins = [v.replace('"', '') for v in o.split(" ")]
        lrules.append((r, ins))
        args.append(ins)
    dRules[r] = args

CNF = []
for k, v in lrules:
    if len(v) == 1 and v not in [['a'], ['b']]:
        for opt in dRules[v[0]]:
            CNF.append((k, opt))
        continue

    CNF.append((k, v))

def matchRule(string, rule):
    return [i for i in range(len(string)) if string[i:i+len(rule)] == rule]

def parse(string):
    n = len(string)
    arr = [list(list() for j in range(n)) for i in range(n)]

    for i in range(n):
        for k, v in CNF:
            if i in matchRule(string, v):
                arr[0][i].append(k)

    for rt in range(1, n):
        for ct in range(0, n-rt):
            for ll in range(rt):
                for k, v in CNF:
                    if v[0] in arr[ll][ct] and v[1] in arr[rt-1-ll][ct+ll+1]:
                        arr[rt][ct].append(k)

    return '0' in arr[-1][0]

count = 0
for i in tqdm(inp):
    ret = parse(i)
    count +=ret
    tqdm.write(f"{'Parses' if ret else 'Fails'}\t count: {count}" )

print(count)
