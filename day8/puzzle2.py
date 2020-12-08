from copy import copy, deepcopy

instructions = []
with open("day8/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    for line in data:
        instr = line.split(" ")[0]
        num   = int(line.split(" ")[1])
        instructions.append([instr, num])


def test(instrs):
    acc = 0

    i = 0

    encountered = set()
    while i < len(instrs):
        if i in encountered:
            return None

        instr = instrs[i]
        encountered.add(i)

        if instr[0] == "jmp":
            i += instr[1]
            continue

        if instr[0] == "acc":
            acc += instr[1]
        i+=1
    
    return acc

for i in range(len(instructions)):
    tmp = deepcopy(instructions)
    if instructions[i][0] == "nop":
        tmp[i][0] = "jmp"
    elif instructions[i][0] == "jmp":
        tmp[i][0] = "nop"
    else:
        continue

    out = test(tmp)
    if out != None:
        print(out)
        break