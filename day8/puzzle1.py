instrs = []
with open("day8/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    for line in data:
        instr = line.split(" ")[0]
        num   = int(line.split(" ")[1])
        instrs.append([instr, num])

acc = 0
i = 0

encountered = set()
while i < len(instrs):
    if i in encountered:
        print(acc)
        exit(0)

    instr = instrs[i]
    encountered.add(i)

    if instr[0] == "jmp":
        i += instr[1]
        continue

    if instr[0] == "acc":
        acc += instr[1]
    i+=1