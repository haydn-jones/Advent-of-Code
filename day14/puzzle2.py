
def enumAddrs(addrs):
    c = addrs.count("X")

    ind = addrs.index("X")
    one, zero = addrs.copy(), addrs.copy()
    one[ind]  = "1"
    zero[ind] = "0"

    if c == 1:
        return [one, zero]

    return [*enumAddrs(one), *enumAddrs(zero)]

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

        manip_addr = [c for c in f'{addr:036b}']
        for i, c in enumerate(mask):
            if c == "0":
                continue
            
            manip_addr[i] = c
        
        addrs = enumAddrs(manip_addr)

        for a in addrs:
            ind = int("".join(a), 2)
            addr_space[ind] = "".join(binary)
    
    sum_ = 0
    for addr, val in addr_space.items():
        sum_ += int(val, 2)
