addr_space = {}

with open("day14/input.txt", "r") as f:
    mask = None
    for i, line in enumerate(f.readlines()):
        line = [v.strip() for v in line.split(" = ")]

        if line[0] == 'mask':
            mask = line[1]
            continue

        addr = int(line[0][4:-1])
        val = int(line[1])
        binary =  [c for c in f'{val:036b}']

        for i in range(len(mask)):
            if mask[i] == "X":
                continue

            binary[i] = mask[i]

        addr_space[addr] = "".join(binary)

    sum_ = 0
    for addr, val in addr_space.items():
        sum_ += int(val, 2)
